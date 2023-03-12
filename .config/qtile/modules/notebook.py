from re import fullmatch
from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal, alt_terminal
from modules.colors import palette
from catppuccin import Flavour
import os

mocha = Flavour.mocha()

notebook_screen = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0),
                widget.GroupBox(
                                highlight_method='line',
                                padding=2,
                                spacing=2,
                                margin=5,
                                #hide_unused=True,
                                rounded=False,
                                center_aligned=True,
                                font='JetBrainsMono Nerd Font',
                                fontsize=14,
                                this_screen_border=mocha.blue.hex,
                                this_current_screen_border=mocha.blue.hex,
                                active=mocha.subtext1.hex,
                                inactive=mocha.surface1.hex),
                widget.Sep(padding=5, linewidth=0),
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(foreground=mocha.subtext1.hex,fmt='{}'),
                widget.Spacer(),
                widget.Clock(format='%H:%M:%S - %m/%d/%y',
                    foreground=mocha.subtext1.hex),
                widget.Spacer(),
                widget.Chord(
                    chords_colors={
                        'launch': (mocha.red.hex, mocha.subtext1.hex),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(
                    scale=0.6,
                    foreground=mocha.subtext1.hex
                    ),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_yay",
                    display_format="{updates} Updates",
                    foreground=mocha.subtext1.hex,
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(alt_terminal + ' -e yay -Syu')
                        }
                    ),
                widget.Systray(icon_size = 20),
                widget.Sep(padding=4, linewidth=0),
                volume, 
                widget.Sep(padding=4, linewidth=0),
                widget.TextBox(
                    #text='盛',
                    text='',
                    fontsize=14,
                    foreground=mocha.subtext1.hex,
                    ),
                widget.Backlight(
                    brightness_file='/sys/class/backlight/intel_backlight/brightness',
                    max_brightness_file='/sys/class/backlight/intel_backlight/max_brightness',
                    foreground=mocha.subtext1.hex,
                    ),
                widget.Sep(padding=4, linewidth=0),
                widget.TextBox(
                    text='',
                    foreground=mocha.subtext1.hex,
                    mouse_callbacks = {
                        'Button1':
                        lambda: qtile.cmd_spawn("rofi-bluetooth")
                        }
                    ),
                widget.Sep(padding=4, linewidth=0),
                widget.TextBox(
                    text='|',
                    foreground=mocha.subtext1.hex
                    ),
                widget.CPU(
                    format='{freq_current}GHz {load_percent}%',
                    foreground=mocha.subtext1.hex,
                    mouse_callbacks = {
                        'Button1':
                        lambda: qtile.cmd_spawn(alt_terminal + ' -e htop -s PERCENT_CPU')
                        }
                    ),
                widget.TextBox(
                    text='|',
                    foreground=mocha.subtext1.hex
                    ),
                widget.Memory(
                    foreground=mocha.subtext1.hex,
                    mouse_callbacks = {
                        'Button1':
                        lambda: qtile.cmd_spawn(alt_terminal + ' -e htop -s PERCENT_MEM')
                        }
                    ),
                widget.TextBox(
                    text='|',
                    foreground=mocha.subtext1.hex
                    ),
                widget.Net(
                    format='{down} ↓↑ {up}',
                    foreground=mocha.subtext1.hex,
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(alt_terminal + ' -e nmtui')
                        }
                    ),
                widget.TextBox(
                    text='|',
                    foreground=mocha.subtext1.hex
                    ),
                widget.Battery (
                    foreground=mocha.subtext1.hex,
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn("xfce4-power-manager-settings")
                        }
                    ),
                widget.Sep(padding=5, linewidth=0),
                widget.TextBox(
                    text='',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground=mocha.red.hex
                ),
                widget.Sep(padding=5, linewidth=0)
                
            ],
            32,  # height in px
            background=mocha.base.hex,  # background color
            opacity=1, # Was 0.8
            margin=[
                10,
                10,
                2,
                10
            ]
        ), ),
]
