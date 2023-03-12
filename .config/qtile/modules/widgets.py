from libqtile import widget
from libqtile import qtile
from catppuccin import Flavour

mocha = Flavour.mocha()

colors = [
	      ["#282c34", "#282c34"], # panel background
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#4f76c7", "#4f76c7"], # color for the 'even widgets'
          ["#e1acff", "#e1acff"], # window name
          ["#ecbbfb", "#ecbbfb"]  # backbround for inactive screens
] 


widget_defaults = dict(
    font='JetBrainsMono Nerd Font Regular',
    fontsize=13,
    padding=3,
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
    fontsize=13,
    foreground=mocha.subtext1.hex,
    font='JetBrainsMono Nerd Font Regular',
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
)
