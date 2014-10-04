#Aperture

Yet another set of wrappers, settings, and added features for Python/matplotlib plotting

###Example function:
    # make a density map out of two vectors x and y
    def make_heatmap(x, y, step=None, min_pt=None, max_pt=None, 
                 colormap='Blues', grid=False, colorbar=True, auto_aspect=True)
               
###Example usage:               
    import matplotlib.pyplot as plt
    import numpy as np

    mean = [0,0]
    cov = [[1,4],[4,10]]
    npts = 10000

    x,y = np.random.multivariate_normal(mean,cov,npts).T

    # look how easy this is
    import aperture as ap

    ap.set_plot_params()  # better defaults
    fig = ap.make_heatmap(x, y)
    plt.show()
    
The result:
![Image here](http://kevinsprong.com/images/projects/aperture/aperture_example.png)

There is also some customizability:

    fig = ap.make_heatmap(x, y, step=0.5, colormap='Greens')    

![Image here](http://kevinsprong.com/images/projects/aperture/aperture_example2.png)
