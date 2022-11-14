set fish_greeting

function gitHubClone
    git clone "https://github.com/$argv"
end

function fastGitPush
    if test $argv = ""
        git push
    else
        git add -A
        git commit -m $argv
        git push
    end
end

# Alias
# ls
alias ls="ls --color"
alias la="ls -a --color"
alias ll="ls -lah --color"
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

if status is-interactive
    # Commands to run in interactive sessions can go here
end

starship init fish | source
