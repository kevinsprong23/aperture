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
    if isinstance(step, (list,tuple)):
        x_acc = step[0]
        y_acc = step[1]
    elif isinstance(step, (int,float)):
        x_acc = step
        y_acc = step
    else:
        x_acc = 1
        y_acc = 1
    
    # set data boundary defaults
    minx = util.floor_nearest(min(x), x_acc)
    maxx = util.ceil_nearest(max(x), x_acc)
    miny = util.floor_nearest(min(y), y_acc)
    maxy = util.ceil_nearest(max(y), y_acc)

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
    x_vec = [n for n in util.frange(min_pt[0], max_pt[0], step[0])]
    y_vec = [n for n in util.frange(min_pt[1], max_pt[1], step[1])]

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


def init_heatmap(x_vec, y_vec, hist_matrix, fig, colormap='Blues',
                 alpha=1, grid=False, colorbar=True, 
                 auto_aspect=True):
    """
    convenience function to initialize a standard colormap in a figure
    """
    plt.figure(fig.number)
    ax = fig.gca()
    
    asp = 'auto' if auto_aspect else 1

    # set vmax and vmin
    mat_max = [max(row) for row in hist_matrix]
    mat_max = max(mat_max)
    
    mat_min = [min(row) for row in hist_matrix]
    mat_min = min(mat_min)
    
    vma = mat_max
    vmi = mat_min
    
    # an error check
    if vma == vmi:
        vma = vmi + 1

    plt.imshow(hist_matrix, cmap=plt.get_cmap(colormap), 
               origin='lower', aspect=asp, alpha=alpha,
               extent=[min(x_vec), max(x_vec), min(y_vec), max(y_vec)],
               vmax=vma, vmin=vmi)

    if colorbar:
        plt.colorbar()
    
    if not grid:
        ax.grid(False)


def make_heatmap(x, y, step=None, min_pt=None, max_pt=None, colormap='Blues',
                 alpha=1, grid=False, colorbar=True, auto_aspect=True):
    """
    function to take vectors x and y and hist them
    """
    (x_vec, y_vec, hist_matrix) = calc_2d_hist(x, y, step, min_pt, max_pt)
    
    fig = plt.figure()
    init_heatmap(x_vec, y_vec, hist_matrix, fig, colormap=colormap,
                 alpha=alpha, grid=grid, colorbar=colorbar,
                 auto_aspect=auto_aspect)
    
    return fig



