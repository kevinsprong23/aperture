"""
functions to make pretty heatmaps
"""

import matplotlib.pyplot as plt
from aperture import util

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
        #print(str(x0) + ", " + str(y0))
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

def init_heatmap(x_vec, y_vec, hist_matrix, fig, 
                 colormap='Blues', grid=False, colorbar=True):
    """
    convenience function to initialize a standard colormap in a figure
    """
    plt.figure(fig.number)
    ax = fig.gca()
    
    plt.imshow(hist_matrix, cmap=plt.get_cmap(colormap), origin='lower',
               extent=[min(x_vec), max(x_vec), min(y_vec), max(y_vec)])

    if colorbar:
        plt.colorbar()
    
    if not grid:
        ax.grid(False, which="majorminor")

def make_heatmap(x, y, step=None, min_pt=None, max_pt=None, 
                 colormap='Blues', grid=False, colorbar=True):
    """
    function to take vectors x and y and hist them
    """
    (x_vec, y_vec, hist_matrix) = calc_2d_hist(x, y, step, min_pt, max_pt)
    
    fig = plt.figure()
    init_heatmap(x_vec, y_vec, hist_matrix, fig, 
                 colormap=colormap, grid=grid, colorbar=colorbar)
    
    return fig