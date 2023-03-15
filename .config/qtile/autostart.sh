#!/bin/sh

WALL=~/.config/background.png

# Setting wallpapers
feh --bg-scale $WALL & disown
betterlockscreen -u $WALL & disown

hostnamectl status | grep 'Chassis' | grep 'vm' &> /dev/null # Grep looks for VMware OR Other chassis-type to determine if VM or not
if [[ $? == 0 ]]; then
  # Should prevent screen tearing on most setups if needed
  # if a VM
  picom --no-vsync & disown 
else
  # if not a VM
  picom --vsync & disown 
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
