"""
package for some plotting wrappers and formatting
"""

import .util
import matplotlib as mpl
import matplotlib.pyplot as plt

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
    mpl.rcParams['axes.grid'] = True   # display grid or not
    mpl.rcParams['axes.titlesize'] = 18   # fontsize of the axes title
    mpl.rcParams['axes.labelsize'] = 18  # fontsize of the x any y labels
    mpl.rcParams['axes.labelcolor'] = '777777'
    mpl.rcParams['axes.color_cycle'] = '268bd2, dc322f, 859900, b58900, d33682, 2aa198, cb4b16, 002b36'
    mpl.rcParams['xtick.color'] = '777777'      # color of the tick labels
    mpl.rcParams['ytick.color'] = '777777'      # color of the tick labels
    mpl.rcParams['grid.color'] = '777777'   # grid color
    mpl.rcParams['legend.fontsize'] = 18
    mpl.rcParams['figure.figsize'] = 11, 8    # figure size in inches
    mpl.rcParams['figure.facecolor'] = 'f7f7f5'    # figure facecolor; 0.75 is scalar gray
    mpl.rcParams['figure.edgecolor'] = None   # figure edgecolor
    mpl.rcParams['savefig.facecolor'] = 'f7f7f5'    # figure facecolor when saving
    mpl.rcParams['savefig.edgecolor'] = None   # figure edgecolor when saving


def make_heatmap(x_vec, y_vec, hist_matrix, fig, 
                 colormap='Blues', grid=False, colorbar=True):
    """
    convenience function to make a standard colormap in a figure
    """
    plt.figure(fig.number)
    ax = fig.gca()
    
    plt.imshow(hist_matrix, cmap=plt.get_cmap(colormap), origin='lower',
               extent=[min(x_vec), max(x_vec), min(y_vec), max(y_vec)])

    if colorbar:
        plt.colorbar()
    
    if not grid:
        ax.grid(False, which="majorminor")
        

def calc_2d_hist(x, y, step=None, min_pt=None, max_pt=None):
    """
    given two vectors x and y, calculate a 2-d histogram matrix
    x = data list
    y = data list
    step = either a scalar dx/dy, or a tuple (dx,dy)
    min = tuple for lower left of bounding box (minx, miny)
    max = tuple for upper right of bounding box

    returns: a tuple (x_vec, y_vec, hist_matrix)
    """

    # parse args
    minx = min(x)
    maxx = max(x)
    miny = min(y)
    maxy = max(y)

    # step
    if step is None:
        default_bins = 100
        default_steps = [1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 
                         1, 10, 100, 1000, 1e4, 1e5, 1e6] 
        
        stepx_raw = (maxx - minx)/default_bins
        stepx = min(default_steps, key=lambda x:abs(x - stepx_raw))

        stepy_raw = (maxy - miny)/default_bins
        stepy = min(default_steps, key=lambda x:abs(x - stepy_raw))
        
        step = (stepx, stepy)
    elif not isinstance(step, (list, tuple)):
        step = (step, step)

    # min and max pt
    if min_pt is None:
        min_pt = (minx, miny)


    if max_pt is None:
        max_pt = (maxx, maxy)

    # use output dict to store bin values
    bin_dict = {}
    for x0, y0 in zip(x, y):
        x0 = util.floor_nearest(x0, step[0])
        y0 = util.floor_nearest(y0, step[1])
        print(str(x0) + ", " + str(y0))
        util.increment(bin_dict, (x0, y0))

    # turn dict into matrix
    x_vec = [n for n in util.frange(minx, maxx, step[0])]
    y_vec = [n for n in util.frange(miny, maxy, step[1])]

    hist_matrix = []
 
    for xj in x_vec:
        row = []
        for yi in y_vec:
            key = (xj, yi)
            if key in bin_dict:
                row.append(bin_dict[key])
            else:
                row.append(0)
        hist_matrix.append(row)

    # return matrix
    return (x_vec, y_vec, hist_matrix)