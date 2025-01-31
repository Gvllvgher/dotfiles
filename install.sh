#!/bin/bash

# Define any files that need to be linked
linkFiles=( \
    ".gitconfig" \
    ".vimrc" \
    ".zshrc" \
    ".Xresources" \
    ".gtkrc-2.0" \
    ".config/background.png" \
    ".config/fish/config.fish" \
    ".config/gtk-3.0/settings.ini" \
    ".config/neofetch/config.conf" \
    ".config/xfce4/terminal/terminalrc" \
    ".config/picom/picom.conf" \
    ".config/dunst/dunstrc" \
    ".config/starship.toml" \
    ".config/flameshot/flameshot.ini" \
    ".config/kitty/kitty.conf" \
    ".config/onlyoffice/DesktopEditors.conf" \
    ".config/pulse/client.conf" \
    ".config/pulse/default.pa" \
    ".config/pulse/system.pa" \
    ".config/pulse/daemon.conf" \
    ".local/share/code-server/User/settings.json" \
)

# Define any directories that need to be linked
linkDirs=( \
    ".config/qtile" \
    ".config/rofi" \
    ".config/alacritty" \
    ".config/ranger" \
    ".config/nvim" \
    ".config/betterlockscreen" \
)

# Defines the current script directory
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]:-$0}";     )" &> /dev/null && pwd 2> /dev/null;     )";

# Loop through the linkFiles list
for file in ${linkFiles[@]}; do
    # Delete the file if it exists
    rm ~/$file &> /dev/null
    
    # Check if the $file variable contains '/' to
    # determine if it goes into a subdirectory of ~
    if [[ "$file" == *"/"* ]]; then
        # Create the subdirectory if it doesn't exist
        mkdir -p ~/${file%/*}
    fi
    
    # Link the file
    ln -sf $SCRIPT_DIR/$file ~/$file
done

# Loop through the linkDirs list
for dir in ${linkDirs[@]}; do
    # Delete the directory if it exists
    rm -rf ~/$dir

    # Link the directory
    ln -sfT $SCRIPT_DIR/$dir ~/$dir
done

# Configure ZSH
$SCRIPT_DIR/setup-zsh.sh

# Sudo check
command -v sudo >/dev/null 2>&1 || { echo >&2 "I require sudo but it's not installed.  Aborting."; exit 0; }

# Docker check - for coder workspaces
if [ -f /.dockerenv ]; then
    echo "Inside docker container, exiting."
    sudo chsh coder -s /usr/bin/zsh
    exit 0;
fi

# For root user
userHome=~
sudo su<<EOF
set -e
cp -r $userHome/.zsh ~/
cp $userHome/.zshrc ~/
exit
EOF

# Configure Firefox
$SCRIPT_DIR/.config/firefox/configure-firefox.sh
