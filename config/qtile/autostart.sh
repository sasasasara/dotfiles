#!/bin/sh
#nitrogen --restore &
ckb-next -b &
hsetroot -solid '#000000' &
picom -b &
xbindkeys &
dunst &
setxkbmap br &
nvidia-settings -a "GpuPowerMizerMode=1" &
autokey-qt &
mpc random &
