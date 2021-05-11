# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen 
from libqtile.lazy import lazy
from libqtile.command import lazy
import os
import subprocess


mod1 = "mod1" # LAlt key
mod = "mod4" # Super key

keys = [

    # Switch groups
    Key([mod], "period", lazy.screen.next_group()),
    Key([mod], "comma", lazy.screen.prev_group()),

    # Switch window focus to other panes
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    
    # Toggle between different layouts 
    Key([mod], "Tab", lazy.next_layout()), 
    Key([mod, "shift"], "Tab", lazy.prev_layout()),

    # Manage Qtile
    Key([mod, "shift"], "r", lazy.restart()), 
    Key([mod, "shift"], "q", lazy.shutdown()),

    # Spawns 
    Key([mod], "b", lazy.spawn("qutebrowser")),
    Key([mod], "Return", lazy.spawn("alacritty")), 
    Key([mod], "e", lazy.spawn("pcmanfm")),
    Key([mod], "a", lazy.spawn("alacritty -e ncpamixer")),
    Key([mod], "t", lazy.spawn("alacritty -e htop")),
    Key([mod], "c", lazy.spawn("alacritty -e nvim /home/sara/.dotfiles/.config/")),
    Key([mod], "d", lazy.spawn("dmenu_run")),
    
    # Screenshots
    Key([], "Print", lazy.spawn("scrot '%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$(xdg-user-dir PICTURES)'")),
    Key([mod], "Print", lazy.spawn("scrot -s '%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$(xdg-user-dir PICTURES)'")),
    Key([mod, "control"], "Print", lazy.spawn("scrot -u '%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$(xdg-user-dir PICTURES)'")),

    # Window stuff
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_floating()),
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "s", lazy.layout.toggle_split()),
    Key([mod, "control"], "n", lazy.layout.normalize()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

]

# Define groups
groups = [Group(i) for i in "1234567890"]
for i in groups:

    keys.extend([
        # Change to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        
        # Change window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),

    ])

# Global theme settings
layout_theme = {"border_width": 2,
                "margin": 20,
                "border_focus": "d5c4a1",
                "border_normal": "584945"
                }

# Active layouts
layouts = [
    layout.Columns(**layout_theme),
    layout.Floating(**layout_theme),
]

# Global widget settings
widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# Top bar
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(foreground='ebdbb2'),
                widget.GroupBox(inactive='797979'),
                widget.WindowName(foreground='ebdbb2'),
                widget.Spacer(length=bar.STRETCH),
                widget.Systray(),
                widget.CheckUpdates(foreground='ebdbb2', display_format='{updates} updates', execute="alacritty -e sudo pacman -Syu"),
                widget.Sep(),
                widget.Volume(foreground='ebdbb2'),
                widget.Image(filename='~/.config/qtile/baricons/vol.png'),
                widget.Sep(),
                widget.Clock(foreground='ebdbb2', format='%A, %H:%M:%S %m/%d/%y'), 
            ],
            19,
            opacity=1,
            background="32302f",
            margin=[20, 20, -15, 20],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[

    # Floating rules
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
    {'wmclass': 'lutris'},  
    {'wmclass': 'Steam'},  
    {'wmclass': 'spotify'},  
    {'wmclass': 'leagueclient.exe'},  
    {'wmclass': 'Wine'},  
    {'wmclass': 'leagueclientux.exe'},  
    {'wmclass': 'bauh'},  
    {'wmclass': 'minecraft-launcher'},  
    {'wmclass': 'gimp-2.10'},  
    {'wmclass': 'riotclientux.exe'},  
    {'wmclass': 'florence'},  
    

])
auto_fullscreen = True
focus_on_window_activation = "smart"

# Deceiving some java apps into working
wmname = "LG3D"

# Startup script
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])
