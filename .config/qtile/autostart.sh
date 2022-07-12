#!/bin/sh

WALL=~/.config/qtile/blue_firewatch.png

feh --bg-scale $WALL & disown
betterlockscreen -u $WALL & disown
picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Display Settings
#xrandr --auto & disown

# Power Manager
#xfce4-power-manager --no-daemon
xfce4-power-manager & disown
#exec --no-startup-id sleep 3 && xfce4-power-manager

# Themes
xfconf-query -c xsettings -p /Net/IconThemeName -s 'Papirus-Dark'
xfconf-query -c xsettings -p /Net/ThemeName -s 'Arc-Dark'

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
