# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
setopt autocd extendedglob nomatch
unsetopt beep notify
bindkey -e
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/justin/.zshrc'

autoload -Uz compinit
zstyle ':completion:*' menu select
zmodload zsh/complist
compinit
_comp_options+=(globdots)
# End of lines added by compinstall

# Disable the 'r' command
# 'r' evaluates to fc -e, which basically recalls the last command.
# This can be an issue for several reasons, but for me, I just want
# to use 'r' as an alias for ranger.
disable r

# Keybinds
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word
bindkey "^[[3~" delete-char
bindkey '^[[Z' autosuggest-accept # Shift + Tab to accept autocomplete suggestions

# Simple Prompt
PROMPT='%n@%m %1~%(!.#.$) '

# Alias Functions
gitHubClone() {
    git clone "https://github.com/$1"
}
fastGitPush() {
    if [[ -z $1 ]]; then
        git push
    else
        git add -A && git commit -m $1 && git push
    fi
}

# Alias
#clear
alias q="clear"
alias qr="reset"
# ls
alias ls="ls --color"
alias la="ls -a --color"
alias ll="ls -lah --color"
# WSL
alias wsl="cd /mnt/c/Users/Justin"
# rm
alias rd="rm -r"
# xclip
alias clip="xclip -selection clipboard"
# Editor
export EDITOR="nvim"
alias vi="$EDITOR"
alias vim="$EDITOR"
alias v="$EDITOR"
# Ranger
alias r="ranger"
alias ra='ranger --cmd="set show_hidden true"'
# Package managers
alias paci="sudo pacman -S"
alias yayi="yay -S"
alias pipi="pip install"
# Git
alias gc="git clone"
alias gh=gitHubClone
alias ga="git add"
alias gA="git add -A"
alias gc="git commit -m"
alias gp=fastGitPush
alias gl="git pull"
alias gs="git status"
# Directories
alias d="cd ~/Documents"
alias D="cd ~/Downloads"
alias c="cd ~/.config"
alias h="cd ~"
alias g="cd ~/git"
# Python
alias py="python3"
alias python="python3"
# Random applications
# uxplay is an AirPlay server application
alias uxplay="uxplay -fps 120 -n $(hostname) -nh"
# Plugins
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
source ~/.zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source ~/.zsh/catppuccin-zsh-syntax-highlighting/themes/catppuccin_mocha-zsh-syntax-highlighting.zsh
# Start Starship
eval "$(starship init zsh)"
