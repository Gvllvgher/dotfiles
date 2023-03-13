from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.colors import palette
import re
import subprocess

bar_opacity = 0.9

machine_info = subprocess.check_output(["hostnamectl", "status"], universal_newlines=True)
m = re.search('Chassis: (.+?)\n', machine_info)
chassis_type = m.group(1)

if 'laptop' in chassis_type:
    widgets = [
        separator,
        groupbox,
        separator_large,
        widget.Prompt(),
        widget.Spacer(length=5),
        windowname,
        widget.Spacer(),
        clock,
        widget.Spacer(),
        chord,
        currentlayout,
        checkupdates,
        systray,
        separator_medium,
        volume, 
        separator_medium,
        backlight_icon,
        backlight,
        separator_medium,
        bluetooth,
        separator_medium,
        line,
        processor,
        line,
        memory,
        line,
        network,
        line,   
        battery,
        separator_large,
        power,
        separator_large
    ]
else:
    widgets = [   
        separator,
        groupbox,
        separator,
        widget.Prompt(),
        widget.Spacer(length=5),
        windowname,
        widget.Spacer(),
        clock,
        widget.Spacer(),
        chord,
        currentlayout,
        checkupdates,
        systray,
        separator_medium,
        volume, 
        separator_medium,
        separator_medium,
        bluetooth,
        separator_medium,
        line,
        processor,
        line,
        memory,
        line,
        network,
        line,
        separator_large,
        power,
        separator_large
    ]

screens = [
    Screen(
        top=bar.Bar(
            widgets,
            32,  # height in px
            background=palette["dark_background"],  # background color
            opacity=bar_opacity, # Was 0.8
            margin=[
                10,
                10,
                2,
                10
            ]
        ),
    ),
]
