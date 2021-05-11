#!/bin/bash
# ~/.bashrc
#
export TERM="xterm-256color"
export EDITOR="vim"
export HISTCONTROL=ignoredups:erasedups
export MANPAGER='/bin/bash -c "vim -MRn -c \"set buftype=nofile showtabline=0 ft=man ts=8 nomod nolist norelativenumber nonu noma\" -c \"normal L\" -c \"nmap q :qa<CR>\"</dev/tty <(col -b)"'



[[ $- != *i* ]] && return

# SHOPT
shopt -s autocd
shopt -s cdspell
shopt -s cmdhist
shopt -s dotglob
shopt -s extglob
shopt -s histappend
shopt -s expand_aliases
shopt -s checkwinsize

#TAB COMPLETION INGORE CASE
bind "set completion-ignore-case on"

#EXTRACTION HELPER
ex() {
  if [ -f "$1" ]; then
    case "$1" in
      *.tar.bz2)  tar xjf "$1"                      ;;
      *.tar.gz)   tar xzf "$1"                      ;;
      *.bz2)      bunzip2 "$1"                      ;;
      *.rar)      unrar x "$1"                      ;;
      *.gz)       gunzip "$1"                       ;;
      *.tar)      tar xf "$1"                       ;;
      *.tbz2)     tar xjf "$1"                      ;;
      *.tgz)      tar xzf "$1"                      ;;
      *.zip)      unzip "$1"                        ;;
      *.Z)        uncompress "$1"                   ;;
      *.7z)       7z x "$1"                         ;;
      *.deb)      ar x "$1"                         ;;
      *.tar.xz)   tar xf "$1"                       ;;
      *.tar.zst)  unzstd "$1"                       ;;
      *)          echo "'$1' can't be extracted"  ;;
    esac
  elif [ -d "$1" ]; then
    echo "'$1' is a directory"
  else
    echo "'$1' doesn't exist"
  fi
}

#NAVIGATION HELPER
up() {
  local d=""
  local limit="$1"

  if [ -n "${limit##+([0-9])}" ]; then
    echo "Limit has to be an integer."
    return 1
  fi

  if [ -z "$limit" ] || [ "$limit" -le 0 ]; then
    limit=1
  fi

  for i in $(seq 1 $limit); do
    d="../$d"
  done

  if ! cd "$d"; then
    echo "Couldn't go up $limit directories.";
  fi
}

#ALIASES
alias svim='sudo vim'
alias cd..='cd ..'
alias cd....='cd ../../'
alias ..='cd ..'
alias ls='exa --color=always --group-directories-first'
alias ll='exa -l --color=always --group-directories-first'
alias lla='exa -la --color=always --group-directories-first'
alias la='exa -a --color=always --group-directories-first'
alias back='cd $OLDPWD'
alias c='clear'
alias fucking='sudo'
alias please='sudo'
alias g='git'
alias gc='git clone'
alias ga='git add'
alias gcm='git commit'
alias gp='git push'
alias nf='neofetch | lolcat'
alias orphan='sudo pacman -Rns $(pacman -Qtdq)'
alias install='sudo pacman -S'
alias uninstall='sudo pacman -Rnsc'
alias update='sudo pacman -Sy'
alias upgrade='sudo pacman -Syu'
alias mirror='sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist'
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='egrep --color=auto'
alias df='df -h'
alias free='free -m'
alias jctl='journalctl -p 3 -xb'
alias rr='curl -s -L https://raw.githubusercontent.com/keroserene/rickrollrc/master/roll.sh | bash'
alias q='exit'
alias :q='exit'
alias quit='exit'
alias rr='rm -rf'
alias speedtest='curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python -'
alias weather='curl wttr.in'
alias bc='bc -q'
alias yay='paru'




# CHECK DISPLAY AND TTY
if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
  exec startx
elif [ "${DISPLAY}" == ":0" ]; then
  export PS1="\[$(tput bold)\]\[$(tput setaf 1)\][\[$(tput setaf 3)\]\u\[$(tput setaf 2)\]@\[$(tput setaf 4)\]\h \[$(tput setaf 5)\]\w\[$(tput setaf 1)\]]\[$(tput setaf 7)\]\\$ \[$(tput sgr0)\]"
  setxkbmap br
else
  export PS1="\[$(tput bold)\]\[$(tput setaf 1)\][\[$(tput setaf 3)\]\u\[$(tput setaf 2)\]@\[$(tput setaf 4)\]\l \[$(tput setaf 5)\]\w\[$(tput setaf 1)\]]\[$(tput setaf 7)\]\\$ \[$(tput sgr0)\]"
fi
