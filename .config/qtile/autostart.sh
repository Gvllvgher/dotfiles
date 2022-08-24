#!/bin/sh

WALL=~/.config/qtile/moraine-lake-ab-canada.png

# Setting wallpapers
feh --bg-scale $WALL & disown
betterlockscreen -u $WALL & disown

# Picom
picom & disown

# Should prevent screen tearing on most setups if needed
#picom --experimental-backends --vsync & disown 

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
