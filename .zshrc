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

bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word

PROMPT='%n@%m %1~%(!.#.$) '
