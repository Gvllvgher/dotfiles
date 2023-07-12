#!/bin/bash

# Extensions to install
extensions=( \
  "vscodevim.vim" \
  "Catppuccin.catppuccin-vsc" \
  "Catppuccin.catppuccin-vsc-icons" \
)

# Install the extensions
for extension in ${extensions[@]}; do
  code-server --install-extension $extension --force
done
