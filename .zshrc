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
compinit
# End of lines added by compinstall

# Variables
export EDITOR="nvim"
export WALL="~/.config/qtile/blue_firewatch.png"

# Disable the 'r' command
# 'r' evaluates to fc -e, which basically recalls the last command.
# This can be an issue for several reasons, but for me, I just want
# to use 'r' as an alias for ranger.
disable r

# Keybinds
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word
bindkey "^[[3~" delete-char

# Simple Prompt
PROMPT='%n@%m %1~%(!.#.$) '

# Alias

alias ls="exa --git"
alias la="exa -a --git"
alias ll="exa -a --long --git"
alias lh="exa -a --long --header --git"
alias vi="$EDITOR"
alias vim="$EDITOR"
alias v="$EDITOR"
alias r="ranger"
eval $(thefuck --alias)

# Plugins
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
source ~/.zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# Start Starship
eval "$(starship init zsh)"
