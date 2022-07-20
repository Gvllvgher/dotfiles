#/bin/bash

# Setting environment variables
export EDITOR="nvim"
export WALL="~/.config/qtile/blue_firewatch.png"

# Checking if we have sudo password saved
if sudo -n true 2&>/dev/null; then
    echo "Sudo password saved, no prompt required."
else
    echo "Need sudo privledge, please enter sudo password"
    sudo touch /etc &> /dev/null
fi

# Setting User full name
echo "Please enter your full name:"
read fullName
sudo chfn -f "$fullName" $(whoami)

# Setting password
echo "Please set your password."
passwd

# Setting root password
echo "Would you like to set the root account password? [y/N]"
read setRootPrompt

if [[ "$setRootPrompt" == "y" ]]; then
    sudo passwd
    echo "Done setting root password"
fi

# Running link.sh to link dot files
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]:-$0}";     )" &> /dev/null && pwd 2>/dev/null;     )";
$SCRIPT_DIR/link.sh

# Setting betterlockscreen as the lock command
xfconf-query -c xfce4-session -p /general/LockCommand -s "betterlockscreen -l" --create -t string
