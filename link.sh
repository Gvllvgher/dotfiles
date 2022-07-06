#!/usr/bin/env bash

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]:-$0}";     )" &> /dev/null && pwd 2> /dev/null;     )";

# Git
ln -sf $SCRIPT_DIR/.gitconfig ~/.gitconfig

# VIM
ln -sf $SCRIPT_DIR/.vimrc ~/.vimrc

# ZSH
ln -sf $SCRIPT_DIR/.zshrc ~/.zshrc

# GTK Themes
ln -sf $SCRIPT_DIR/.gtkrc-2.0 ~/.gtkrc-2.0 # GTK 2
mkdir -p ~/.config/gtk-3.0 # GTK 3
ln -sf $SCRIPT_DIR/.config/gtk-3.0/settings.ini ~/.config/gtk-3.0/settings.ini # GTK 3

# Qtile
rm -rf ~/.config/qtile
ln -sfT $SCRIPT_DIR/.config/qtile ~/.config/qtile

# Neofetch
rm -rf ~/.config/neofetch
mkdir -p .config/neofetch
ln -sf $SCRIPT_DIR/.config/neofetch/config.conf ~/.config/neofetch/config.conf

# XFCE Terminal
mkdir -p ~/.config/xfce4/terminal
ln -sf $SCRIPT_DIR/.config/xfce4/terminal/terminalrc ~/.config/xfce4/terminal/terminalrc

# Picom
ln -sf $SCRIPT_DIR/.config/picom.conf ~/.config/picom.conf
