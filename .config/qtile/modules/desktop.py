from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal, alt_terminal
from modules.colors import palette
import os

desktop_screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0),
                widget.GroupBox(
                                highlight_method='line',
                                padding=3,
                                spacing=5,
                                margin=5,
                                #hide_unused=True,
                                rounded=False,
                                center_aligned=True,
                                font='JetBrainsMono Nerd Font',
                                fontsize=14,
                                this_screen_border="#5294e2",
                                this_current_screen_border="#5294e2",
                                active="#ffffff",
                                inactive="#848e96"),
                widget.Sep(padding=5, linewidth=0),
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(foreground='#99c0de',fmt='{}'),
                widget.Spacer(),
                widget.Clock(format='%H:%M:%S - %m/%d/%y',
                    foreground='#99c0de'),
                widget.Spacer(),
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
                        lambda: qtile.cmd_spawn(alt_terminal + ' -e yay -Syu')
                        }
                    ),
                widget.Systray(icon_size = 20),
                widget.Sep(padding=4, linewidth=0),
                volume, 
                widget.Sep(padding=4, linewidth=0),
                widget.Sep(padding=4, linewidth=0),
                widget.TextBox(
                    text='',
                    foreground='#99c0de',
                    mouse_callbacks = {
                        'Button1':
                        lambda: qtile.cmd_spawn("rofi-bluetooth")
                        }
                    ),
                widget.Sep(padding=4, linewidth=0),
                widget.TextBox(
                    text='|',
                    foreground='#99c0de'
                    ),
                widget.CPU(
                    format='{freq_current}GHz {load_percent}%',
                    foreground='#99c0de',
                    mouse_callbacks = {
                        'Button1':
                        lambda: qtile.cmd_spawn(alt_terminal + ' -e htop -s PERCENT_CPU')
                        }
                    ),
                widget.TextBox(
                    text='|',
                    foreground='#99c0de'
                    ),
                widget.Memory(
                    foreground='#99c0de',
                    mouse_callbacks = {
                        'Button1':
                        lambda: qtile.cmd_spawn(alt_terminal + ' -e htop -s PERCENT_MEM')
                        }
                    ),
                widget.TextBox(
                    text='|',
                    foreground='#99c0de'
                    ),
                widget.Net(
                    format='{down} ↓↑ {up}',
                    foreground='#99c0de',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(alt_terminal + ' -e nmtui')
                        }
                    ),
                widget.TextBox(
                    text='|',
                    foreground='#99c0de'
                    ),
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
            32,  # height in px
            background=palette[1],  # background color
            opacity=0.8,
            margin=[
                10,
                10,
                2,
                10
            ]
        ), ),
]
