from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
from modules.colors import palette
import os

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0),
                widget.GroupBox(
                                highlight_method='line',
                                this_screen_border="#5294e2",
                                this_current_screen_border="#5294e2",
                                active="#ffffff",
                                inactive="#848e96"),
                widget.Sep(padding=5, linewidth=0),
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(foreground='#99c0de',fmt='{}'),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(scale=0.75),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_yay",
                    display_format="{updates} Updates",
                    foreground="#ffffff",
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')
                        }
                    ),
                widget.Systray(icon_size = 20),
                widget.Sep(padding=4, linewidth=0),
                volume, 
                widget.Sep(padding=4, linewidth=0),
                widget.Clock(format=' %Y-%m-%d %a %H:%M:%S',
                    foreground='#99c0de'),
                widget.Sep(padding=5, linewidth=0),
                widget.TextBox(
                    text='',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground='#e39378'
                ),
                widget.Sep(padding=5, linewidth=0)
                
            ],
            30,  # height in px
            background=palette[1],  # background color
            opacity=0.9,
            margin=[
                10,
                10,
                2,
                10
            ]
        ), ),
]
