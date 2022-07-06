#!/bin/bash

# Define any files that need to be linked
linkFiles=( \
    ".gitconfig" \
    ".vimrc" \
    ".zshrc" \
    ".gtkrc-2.0" \
    ".config/gtk-3.0/settings.ini" \
    ".config/neofetch/config.conf" \
    ".config/xfce4/terminal/terminalrc" \
    ".config/picom.conf" \
)

# Define any directories that need to be linked
linkDirs=( \
    ".config/qtile" \
)

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
    rm -rf ~/$dir & > /dev/null
    
    # Create the parent directory(ies) if it/they don't exist
    mkdir -p ~/${dir%/*}

    # Link the directory
    ln -sfT $SCRIPT_DIR/$dir ~/$dir
done
