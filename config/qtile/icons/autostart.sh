#!/bin/sh
nitrogen --restore &
picom --config $HOME/.dotfiles/.config/picom.conf &
ckb-next -b &
xbindkeys -f /home/sara/.xbindkeysrc &
dunst &
setxkbmap br &
