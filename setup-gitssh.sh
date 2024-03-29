#! /bin/bash

if [ ! -f ~/.ssh/id_rsa ]; then
  read -p "Enter github email: " email
  ssh-keygen -t ed25519 -C "$email" -f ~/.ssh/id_rsa
  ssh-add ~/.ssh/id_rsa
fi

ssh-keyscan -t ed25519 github.com >> ~/.ssh/known_hosts
pub=`cat ~/.ssh/id_rsa.pub`
read -p "Enter github username: " githubuser
read -s -p "Enter github token for user $githubuser: " githubpass
echo curl -u "$githubuser:$githubpass" -X POST -d "{\"title\":\"$(cat /etc/hostname)-$(date +%m-%d-%Y_%H-%M)\",\"key\":\"$pub\"}" https://api.github.com/user/keys
