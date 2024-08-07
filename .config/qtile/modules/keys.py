from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
#terminal = "xfce4-terminal"
terminal = "kitty"
alt_terminal = "alacritty"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "r", lazy.spawn("rofi -show run"), desc="spawn run menu"),
    Key([mod], "a", lazy.spawn("rofi -show drun"), desc="spawn apps"),
    Key([mod], "x", lazy.spawn("sh -c ~/.config/rofi/powermenu.sh"), desc="power menu"),

    # Switch between groups
    Key([mod], "Right", lazy.screen.next_group(),
        desc="Switch to next group"),

    Key([mod], "Left", lazy.screen.prev_group(),
        desc="Switch to previous group"),

    # Open temp terminal
    Key([mod], "s", lazy.group["0"].dropdown_toggle("term")),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.spawn(alt_terminal), desc="Launch alt terminal"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    
    # Qtile commands
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    # Volume
    Key([], "XF86AudioRaiseVolume",lazy.spawn("amixer set Master 3%+")),
    Key([], "XF86AudioLowerVolume",lazy.spawn("amixer set Master 3%-")),
    Key([], "XF86AudioMute",lazy.spawn("amixer set Master toggle")),

    # Custom keybinds
    Key([], "Home", lazy.spawn("flameshot gui")),
    Key([mod], "f", lazy.spawn("firefox")),
    Key([mod], "q", lazy.spawn("betterlockscreen -l --display 1"), desc="lock screen"),
    Key([mod], "b", lazy.spawn("rofi-bluetooth"), desc="bluetooth menu"),
    Key([mod, "shift"], "n", lazy.spawn(alt_terminal + " -e nmtui"), desc="network menu"),
]
