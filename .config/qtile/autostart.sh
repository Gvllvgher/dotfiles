#!/bin/sh

WALL=~/.config/qtile/blue_firewatch.png

# Setting wallpapers
feh --bg-scale $WALL & disown
betterlockscreen -u $WALL & disown

dmidecode -s system-product-name | grep 'VMware' &> /dev/null
if [[$? == 0 ]]; then
    picom & disown
else
    picom --experimental-backends --vsync & disown # should prevent screen tearing on most setups if needed
fi

# Display Settings
#xrandr --auto & disown

# Power Manager
xfce4-power-manager & disown

# Start flameshot
flameshot & disown

# Themes
xfconf-query -c xsettings -p /Net/IconThemeName -s 'Papirus-Dark'
xfconf-query -c xsettings -p /Net/ThemeName -s 'Arc-Dark'

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
