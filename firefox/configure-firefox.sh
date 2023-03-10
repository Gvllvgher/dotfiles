#!/bin/bash

linkFile="policies.json"

# Defines the current script directory
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]:-$0}";     )" &> /dev/null && pwd 2> /dev/null;     )";


if sudo -n true 2&>/dev/null; then
  echo "sudo password saved, configuring firefox"
else
  echo "Enter sudo password to configure firefox"
  sudo touch /etc &> /dev/null
fi

sudo ln -sf $SCRIPT_DIR/$linkFile /usr/lib/firefox/distribution/$linkFile
