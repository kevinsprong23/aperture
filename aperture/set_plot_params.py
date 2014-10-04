"""
callable plot themes in lieu of modifying rc file
"""

import matplotlib as mpl

def set_plot_params(theme=None):
    """
    set plot parameters for session, as an alternative to
    manipulating RC file
    """
    
    # set solarized color progression no matter what
    mpl.rcParams['axes.color_cycle'] = ('268bd2, dc322f, 859900, ' +
                                       'b58900, d33682, 2aa198, ' +
                                       'cb4b16, 002b36')
    
    
    # non-color options are independent as well
    mpl.rcParams['figure.figsize'] = 11, 8  # figure size in inches
    mpl.rcParams['lines.linewidth'] = 2.0     # line width in points
    mpl.rcParams['axes.grid'] = 'True'   # display grid or not
    
    mpl.rcParams['font.size'] = 18.0
    mpl.rcParams['axes.titlesize'] = 18   # fontsize of the axes title
    mpl.rcParams['axes.labelsize'] = 18  # fontsize of the x any y labels
    mpl.rcParams['legend.fontsize'] = 18
    
    mpl.rcParams['figure.edgecolor'] = 'None'  # figure edgecolor
    mpl.rcParams['savefig.edgecolor'] = 'None'  # figure edgecolor saving

    # color by theme
    if theme == 'dark':
        mpl.rcParams['text.color'] = "bbbbbb"
        mpl.rcParams['axes.facecolor'] = '333333'
        mpl.rcParams['axes.edgecolor'] = '999999'   # axes edge color
        mpl.rcParams['axes.labelcolor'] = 'bbbbbb'
        mpl.rcParams['xtick.color'] = 'bbbbbb'  # color of the tick labels
        mpl.rcParams['ytick.color'] = 'bbbbbb'  # color of the tick labels
        mpl.rcParams['grid.color'] = 'bbbbbb'  # grid color
        mpl.rcParams['figure.facecolor'] = '333333'  # figure facecolor
        mpl.rcParams['savefig.facecolor'] = '333333'  # figure facecolor saving
        
    elif theme == 'white':
        mpl.rcParams['text.color'] = "111111"
        mpl.rcParams['axes.facecolor'] = 'ffffff'
        mpl.rcParams['axes.edgecolor'] = '111111'   # axes edge color
        mpl.rcParams['axes.labelcolor'] = '111111'
        mpl.rcParams['xtick.color'] = '111111'  # color of the tick labels
        mpl.rcParams['ytick.color'] = '111111'  # color of the tick labels
        mpl.rcParams['grid.color'] = '111111'  # grid color
        mpl.rcParams['figure.facecolor'] = 'ffffff'  # figure facecolor
        mpl.rcParams['savefig.facecolor'] = 'ffffff'  # figure facecolor saving   
        
    else:
        mpl.rcParams['text.color'] = "777777"
        mpl.rcParams['axes.facecolor'] = 'f7f7f5'
        mpl.rcParams['axes.edgecolor'] = '111111'   # axes edge color
        mpl.rcParams['axes.labelcolor'] = '777777'
        mpl.rcParams['xtick.color'] = '777777'  # color of the tick labels
        mpl.rcParams['ytick.color'] = '777777'  # color of the tick labels
        mpl.rcParams['grid.color'] = '777777'  # grid color
        mpl.rcParams['figure.facecolor'] = 'f7f7f5'  # figure facecolor
        mpl.rcParams['savefig.facecolor'] = 'f7f7f5'  # figure facecolor saving
    