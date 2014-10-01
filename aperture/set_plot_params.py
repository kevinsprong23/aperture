"""
callable plot themes in lieu of modifying rc file
"""

import matplotlib as mpl

def set_plot_params():
    """
    set plot parameters for session, as an alternative to
    manipulating RC file
    """

    mpl.rcParams['lines.linewidth'] = 2.0     # line width in points
    mpl.rcParams['font.size'] = 18.0
    mpl.rcParams['text.color'] = "777777"
    mpl.rcParams['axes.facecolor'] = 'f7f7f5'
    mpl.rcParams['axes.edgecolor'] = '111111'   # axes edge color
    mpl.rcParams['axes.grid'] = 'True'   # display grid or not
    mpl.rcParams['axes.titlesize'] = 18   # fontsize of the axes title
    mpl.rcParams['axes.labelsize'] = 18  # fontsize of the x any y labels
    mpl.rcParams['axes.labelcolor'] = '777777'
    mpl.rcParams['axes.color_cycle'] = ('268bd2, dc322f, 859900, ' +
                                       'b58900, d33682, 2aa198, ' +
                                       'cb4b16, 002b36')
    mpl.rcParams['xtick.color'] = '777777'  # color of the tick labels
    mpl.rcParams['ytick.color'] = '777777'  # color of the tick labels
    mpl.rcParams['grid.color'] = '777777'  # grid color
    mpl.rcParams['legend.fontsize'] = 18
    mpl.rcParams['figure.figsize'] = 11, 8  # figure size in inches
    mpl.rcParams['figure.facecolor'] = 'f7f7f5'  # figure facecolor
    mpl.rcParams['figure.edgecolor'] = 'None'  # figure edgecolor
    mpl.rcParams['savefig.facecolor'] = 'f7f7f5'  # figure facecolor saving
    mpl.rcParams['savefig.edgecolor'] = 'None'  # figure edgecolor saving
