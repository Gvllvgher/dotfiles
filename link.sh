#!/usr/bin/env bash

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]:-$0}";     )" &> /dev/null && pwd 2> /dev/null;     )";

ln -s $SCRIPT_DIR/.gitconfig ~/.gitconfig

ln -s $SCRIPT_DIR/.vimrc ~/.vimrc

ln -s $SCRIPT_DIR/.zshrc ~/.zshrc
