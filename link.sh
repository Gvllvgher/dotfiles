#!/usr/bin/env bash

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]:-$0}";     )" &> /dev/null && pwd 2> /dev/null;     )";

ln -sf $SCRIPT_DIR/.gitconfig ~/.gitconfig

ln -sf $SCRIPT_DIR/.vimrc ~/.vimrc

ln -sf $SCRIPT_DIR/.zshrc ~/.zshrc

ln -sf $SCRIPT_DIR/qtile ~/.config/
