#!/bin/bash

# Defines the current script directory
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]:-$0}";     )" &> /dev/null && pwd 2> /dev/null;     )";


if sudo -n true 2&>/dev/null; then
  echo "sudo password saved, configuring firefox"
else
  echo "Enter sudo password to configure firefox"
  sudo touch /etc &> /dev/null
fi

# Requires policies.json to be in the same folder as this script
sudo ln -sf $SCRIPT_DIR/policies.json /usr/lib/firefox/distribution/policies.json
