#!/bin/sh
#feh --bg-scale /usr/share/backgrounds/Community-Wallpapers/eos_wallpapers_community/Endy_vector_satelliet.png
feh --bg-scale ~/.config/qtile/nordic.jpg
picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Power Manager
#xfce4-power-manager --no-daemon
xfce4-power-manager & disown
#exec --no-startup-id sleep 3 && xfce4-power-manager

# Low battery notifier
~/.config/qtile/scripts/check_battery.sh & disown

# Start welcome
#eos-welcome & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
