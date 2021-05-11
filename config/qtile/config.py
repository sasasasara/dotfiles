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
from libqtile.config import Click, Drag, Group, Key, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.command import lazy

import os
import subprocess

mod = "mod4" # Super key
term = "alacritty"

keys = [

    # Switch window focus to other panes
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

    # Monitors
    #Key([mod, "control"], "Tab", lazy.next_screen()),
    #Key([mod, "control", "shift"], "Tab", lazy.prev_screen()),
    
    # Toggle between different layouts 
    Key([mod], "Tab", lazy.next_layout()), 
    Key([mod, "shift"], "Tab", lazy.prev_layout()),

    # Manage Qtile
    Key([mod, "shift"], "r", lazy.restart()), 
    Key([mod, "shift"], "q", lazy.shutdown()),

    # Spawns 
    Key([mod], "b", lazy.spawn("qutebrowser")),
    Key([mod], "Return", lazy.spawn(term)), 
    Key([mod], "e", lazy.spawn("pcmanfm")),
    Key([mod], "a", lazy.spawn(term+" -e ncpamixer")),
    Key([mod], "g", lazy.spawn(term+" -e gotop")), 
    Key([mod], "d", lazy.spawn("dmenu_run")),
    Key([mod], "v", lazy.spawn(term+" -e nvim")),
    Key([mod], "z", lazy.spawn(term+" -e chancli")),

    # Window stuff
    Key([mod], "w", lazy.window.kill()),
    Key([mod], "f", lazy.window.toggle_floating()),
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "control"], "j", lazy.layout.grow_down(), lazy.layout.shrink()),
    Key([mod, "control"], "k", lazy.layout.grow_up(), lazy.layout.grow()),
    Key([mod, "control"], "h", lazy.layout.grow_left()), 
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "n", lazy.layout.normalize(), lazy.layout.reset()),
    Key([mod, "control"], "f", lazy.layout.flip()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

    # Dmenu scripts
    KeyChord([mod], "m", [
            Key([], "p", lazy.spawn("dm-music -q")),
            Key([], "s", lazy.spawn("dm-music -p")),
            Key([], "m", lazy.spawn("dm-music")),
        ]),
    Key([], "Print", lazy.spawn("dm-scrot")),
    Key([mod], "p", lazy.spawn("passmenu")),
    Key([mod], "c", lazy.spawn("dm-conf")),
    Key([mod], "t", lazy.spawn("dm-kill")),
    Key([mod], "q", lazy.spawn("dm-logout")),
    Key([mod, "shift"], "p", lazy.spawn("dm-pacman")),
    Key([mod], "s", lazy.spawn("dm-hub")),
    Key([mod, "shift"], "e", lazy.spawn("dm-browse")),
    KeyChord([mod], "u", [
            Key([], "m", lazy.spawn("dm-usbmount -m")),
            Key([], "u", lazy.spawn("dm-usbmount -u")),
        ]),
]

# Define groups
group_names = [("1", {'layout': 'monadtall'}),
               ("2", {'layout': 'monadtall'}),
               ("3", {'layout': 'monadtall'}),
               ("4", {'layout': 'monadtall'}),
               ("5", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group



# Global theme settings
layout_theme = {"border_width": 2,
                "margin": 20,
                "border_focus": "d5c4a1",
                "border_normal": "584945"
                }

# Active layouts
layouts = [
    layout.MonadTall(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Floating(**layout_theme),
]

# Global widget settings
widget_defaults = dict(
    font='AvantGarde Book',
    fontsize=13,
    padding=3,
    foreground='ebdbb2',
)
extension_defaults = widget_defaults.copy()

# Bars
def init_widgets_list():
    widgets_list = [
        widget.CurrentLayoutIcon(),
        widget.GroupBox(fontsize=12, inactive='797979', active='ebdbb2', borderwidth=2, disable_drag=True, this_current_screen_border='d5c4a1', other_current_screen_border='d5c4a1', this_screen_border='404040'),
        widget.TaskList(border='d5c4a1', borderwidth=1, margin=1, rounded=False, padding=2, txt_floating='🗗 ', txt_maximized='🗖 ', txt_minimized='🗕 '),
        widget.Spacer(length=bar.STRETCH),
        widget.Systray(),
        widget.CheckUpdates(execute='sudo pacman -Syu --noconfirm', update_interval=60, colour_have_updates='ebdbb2', distro='Arch_checkupdates'),
        widget.Sep(),
        widget.CPU(format='{freq_current}GHz {load_percent}%', update_interval=5.0),
        widget.Image(filename='~/.config/qtile/baricons/cpu.png'),
        widget.Sep(),
        widget.Memory(format='{MemUsed}/{MemTotal}M', update_interval=5),
        widget.Image(filename='~/.config/qtile/baricons/mem.png'),
        widget.Sep(),
        widget.Net(format='{down} ↓↑ {up}', update_interval=5),
        widget.Image(filename='~/.config/qtile/baricons/net.png'),
        widget.Sep(),
        widget.Volume(update_interval=0.05),
        widget.Image(filename='~/.config/qtile/baricons/vol.png'),
        widget.Sep(),
        widget.Clock(format='%A, %H:%M:%S %m/%d/%y'), 
        ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

#def init_widgets_screen2():
    #widgets_screen2 = init_widgets_list()
    #return widgets_screen2

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1, size=19, background="32302f", margin=[20, 20, -15, 20]))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    #widgets_screen2 = init_widgets_screen2()

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
    {'wmclass': 'leagueclient.exe'},  
    {'wmclass': 'Wine'},  
    {'wmclass': 'leagueclientux.exe'},  
    {'wmclass': 'bauh'},  
    {'wmclass': 'minecraft-launcher'},  
    {'wmclass': 'riotclientux.exe'},  
    {'wmclass': 'pinentry-gtk-2'},
    {'wmclass': 'QtPass'},
    {'wmclass': 'yad'},
    {'wmclass': 'origin.exe'},
    {'wmclass': 'ftb-app'},
    {'wmclass': 'net-technicpack-launcher-LauncherMain'},
    {'wmclass': 'fantome.exe'},
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
