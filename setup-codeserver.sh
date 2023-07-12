#!/bin/bash

# Extensions to install
extensions=( \
  "ms-python.python" \
  "esbenp.prettier-vscode" \
  "eamodio.gitlens" \
  "ms-azuretools.vscode-docker" \
  "redhat.vscode-yaml" \
  "redhat.vscode-xml" \
  "yzhang.markdown-all-in-one" \
  "hashicorp.terraform" \
  "vscodevim.vim" \
  "Catppuccin.catppuccin-vsc" \
  "Catppuccin.catppuccin-vsc-icons" \
)

# Install the extensions
for extension in ${extensions[@]}; do
  code-server --install-extension $extension --force
done
