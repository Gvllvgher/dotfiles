from libqtile import widget
from libqtile import qtile
from modules.keys import terminal, alt_terminal
from modules.colors import palette
import os

widget_defaults = dict(
    font='JetBrainsMono Nerd Font',
    foreground=palette["text"],
    fontsize=13,
    padding=2,
)

extension_defaults = widget_defaults.copy()

class MyVolume(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        
        if self.volume <= 0:
            self.text = ''
        else:
            self.text = ' ' + str(self.volume) + "%"
       
       # drawing here crashes Wayland

    def _update_drawer(self, wob=False):
        if self.volume <= 0:
            self.text = ''
        else:
            self.text = ' ' + str(self.volume) + "%"
        
        self.draw()
        
        if wob:
            with open(self.wob, 'a') as f:
                f.write(str(self.volume) + "\n")

volume = MyVolume(
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")},
    **widget_defaults
    )

separator = widget.Sep(
    linewidth=0,
    padding=3
    )

separator_medium = widget.Sep(
    linewidth=0,
    padding=4
    )

separator_large = widget.Sep(
    linewidth=0,
    padding=5
    )

line = widget.TextBox(
    text='|',
    **widget_defaults
    )

groupbox = widget.GroupBox(
    highlight_method='line',
    spacing=2,
    margin=5,
    #hide_unused=True,
    rounded=False,
    center_aligned=True,
    this_screen_border=palette["blue"],
    this_current_screen_border=palette["blue"],
    active=palette["text"],
    inactive=palette["light_background"],
    **widget_defaults
    )

windowname = widget.WindowName(
    fmt='{}',
    **widget_defaults
    )

clock = widget.Clock(
    format='%H:%M:%S - %m/%d/%y',
    **widget_defaults 
    )

chord = widget.Chord(
    chords_colors={
        'launch': ("#ff0000", "#ffffff"),
    },
    name_transform=lambda name: name.upper(),
    **widget_defaults
    )

currentlayout = widget.CurrentLayoutIcon(
    scale=0.75,
    **widget_defaults
    )

checkupdates = widget.CheckUpdates(
    update_interval=1800,
    distro="Arch_yay",
    display_format="{updates} Updates",
    mouse_callbacks={
        'Button1':
        lambda: qtile.cmd_spawn(alt_terminal + ' -e yay -Syu')
        },
    **widget_defaults
    )

systray = widget.Systray(
    icon_size=20,
    **widget_defaults
    )

backlight_icon = widget.TextBox(
    #text='盛',
    text='',
    **widget_defaults
    )

backlight = widget.Backlight(
    brightness_file='/sys/class/backlight/intel_backlight/brightness',
    max_brightness_file='/sys/class/backlight/intel_backlight/max_brightness',
    **widget_defaults
    )

battery = widget.Battery(
    mouse_callbacks= {
        'Button1':
        lambda: qtile.cmd_spawn("xfce4-power-manager-settings")
        },
    **widget_defaults
    )

bluetooth = widget.TextBox(
    text='',
    mouse_callbacks = {
        'Button1':
        lambda: qtile.cmd_spawn("rofi-bluetooth")
        },
    **widget_defaults
    )

processor = widget.CPU(
    format='{freq_current}GHz {load_percent}%',
    mouse_callbacks = {
        'Button1':
        lambda: qtile.cmd_spawn(alt_terminal + ' -e htop -s PERCENT_CPU')
        },
    **widget_defaults
    )

memory = widget.Memory(
    mouse_callbacks = {
        'Button1':
        lambda: qtile.cmd_spawn(alt_terminal + ' -e htop -s PERCENT_MEM')
        },
    **widget_defaults
    )

network = widget.Net(
    format='{down} ↓↑ {up}',
    mouse_callbacks= {
        'Button1':
        lambda: qtile.cmd_spawn(alt_terminal + ' -e nmtui')
        },
    **widget_defaults
    )

power = widget.TextBox(
    text='',
    mouse_callbacks= {
        'Button1':
        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
    },
    foreground=palette["red"]
)
