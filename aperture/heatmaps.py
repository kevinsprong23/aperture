"""
functions to make pretty heatmaps
"""

from math import log10
import numpy as np
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

    # rough data boundary    
    minx = min(x)    
    maxx = max(x)
    miny = min(y)
    maxy = max(y)         
    
    # step
    if step is None:
        default_bins = 100
        default_steps = [1e-6, 1e-5, 1e-4, 1e-3, 1e-2,
                         1, 10, 100, 1000, 1e4, 1e5, 1e6]

        stepx_raw = (maxx - minx)/default_bins
        stepx = min(default_steps, key=lambda x: abs(x - stepx_raw))

        stepy_raw = (maxy - miny)/default_bins
        stepy = min(default_steps, key=lambda x: abs(x - stepy_raw))
    
        step = (stepx, stepy)
    elif isinstance(step, (int, float)):  
        step = (step, step)
    
    # set rounding accuracy for min/max
    x_acc = step[0]
    y_acc = step[1]
    
    # set real data boundary defaults
    minx = util.floor_nearest(minx, x_acc)
    maxx = util.ceil_nearest(maxx, x_acc)
    miny = util.floor_nearest(miny, y_acc)
    maxy = util.ceil_nearest(maxy, y_acc)
    
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
        util.increment(bin_dict, (x0, y0))

    # turn dict into matrix
    x_vec = [n for n in util.frange(min_pt[0], max_pt[0], step[0])]
    y_vec = [n for n in util.frange(min_pt[1], max_pt[1], step[1])]

    hist_matrix = []

    for yi in y_vec:
        row = []
        for xj in x_vec:
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
                 vmax='auto', vmin='auto', crop=True):
    """
    convenience function to initialize a standard colormap in a figure
    """
    plt.figure(fig.number)
    ax = fig.gca()

    # set vmax and vmin
    vma = np.amax(hist_matrix) if vmax == 'auto' else vmax
    vmi = np.amin(hist_matrix) if vmin == 'auto' else vmin

    # an error check
    if vma <= vmi:
        vma = vmi + 1

    # grid the space for pcolormesh
    x_grid, y_grid = np.meshgrid(x_vec, y_vec)

    hmap = ax.pcolormesh(x_grid, y_grid, np.array(hist_matrix),
               cmap=colormap, alpha=alpha, shading='gouraud',
               vmax=vma, vmin=vmi)

    if colorbar:
        plt.colorbar(hmap)

    if not grid:
        ax.grid(False)

    if crop:
        ax.set_xlim([x_vec[0], x_vec[-1]])
        ax.set_ylim([y_vec[0], y_vec[-1]])


def make_heatmap(x, y, step=None, min_pt=None, max_pt=None,
                 colormap='Blues', alpha=1, grid=False,
                 colorbar=True, scale='lin',
                 vmax='auto', vmin='auto', crop=True):
    """
    function to take vectors x and y and hist them
    """
    (x_vec, y_vec, hist_matrix) = calc_2d_hist(x, y, step, min_pt, max_pt)

    # simple in this case because it is positive counts
    if scale == 'log':
        for row in hist_matrix:
            for i, el in enumerate(row):
                row[i] = 0 if row[i] == 0 else log10(row[i])

    # plot
    fig = plt.figure()
    init_heatmap(x_vec, y_vec, hist_matrix, fig, colormap=colormap,
                 alpha=alpha, grid=grid, colorbar=colorbar,
                 vmax=vmax, vmin=vmin, crop=crop)

    return fig



