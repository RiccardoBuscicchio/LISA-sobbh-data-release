import numpy as np
from matplotlib.legend_handler import HandlerTuple
import matplotlib.lines as mlines
from matplotlib.lines import Line2D
from matplotlib.legend_handler import HandlerTuple, HandlerBase
import matplotlib.pyplot as plt

fig_width_pt = 2*246.0  
inches_per_pt = 1.0 / 72.27
golden_mean = (np.sqrt(5) - 1.0) / 2.0
fig_width = fig_width_pt * inches_per_pt
fig_height = fig_width * golden_mean
square_size = [fig_width, fig_width]
rect_size = [fig_width, fig_height]

rc_params = {'axes.labelsize': 18,
          'axes.titlesize': 24,
          'font.size': 18,
          'legend.fontsize': 18,
          'font.family': 'serif',
          'font.sans-serif': ['Bitstream Vera Sans'],
          'font.serif': ['Bitstream Vera'],
          'xtick.labelsize': 18,
          'ytick.labelsize': 18,
          'text.usetex': True,
          'text.latex.preamble': r"""\usepackage{amsmath} \usepackage{amssymb} \usepackage{amsfonts}""",
          'figure.figsize': rect_size,
         }

class HandlerVerticalLines(HandlerTuple):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans):
        line1, line2,line3 = orig_handle
        y_offset = height/1.5
        line1_artist = super().create_artists(legend, (line1,), xdescent, ydescent + y_offset, width, height, fontsize, trans)[0]
        line2_artist = super().create_artists(legend, (line2,), xdescent, ydescent, width, height, fontsize, trans)[0]
        line3_artist = super().create_artists(legend, (line3,), xdescent, ydescent - y_offset, width, height, fontsize, trans)[0]        
        return [line1_artist, line2_artist, line3_artist]

