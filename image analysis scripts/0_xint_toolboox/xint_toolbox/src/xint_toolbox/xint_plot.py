import matplotlib as mpl
import math
import numpy as np
import matplotlib.pyplot as plt

def shaded_cmap(color="tab:blue", shade_range=[.2, .8]):
    import colorsys
    num = 1024
    color_rgb = mpl.colors.to_rgb(color)
    color_hls = colorsys.rgb_to_hls(color_rgb[0], color_rgb[1], color_rgb[2])
    shading = np.linspace(shade_range[0], shade_range[1], num)
    gamma = math.log(0.5) / math.log(color_hls[1])
    shading_conversion = np.exp(np.log(shading)/gamma)
    shaded_cmap = []
    for i in range(num):
        shaded_color = colorsys.hls_to_rgb(color_hls[0], shading_conversion[i], color_hls[2])
        shaded_cmap.append(shaded_color)
    
    # _,ax=plt.subplots(figsize=(3,2))
    # ax.scatter(range(num), shading_conversion, color=shaded_cmap)
    # ax.scatter((num-1)/2, color_hls[1], color=color, s=200)
    # ax.set_ylim(0,1)
    # ax.set_ylabel('Lightness')
    # plt.show()

    shaded_cmap = mpl.colors.ListedColormap(shaded_cmap)
    return shaded_cmap


def colored_line(x,y,c,ax, vmin='auto', vmax='auto', **lc_kwargs):
    
    from matplotlib.collections import LineCollection
    default_kwargs = {"capstyle": "butt"}
    default_kwargs.update(lc_kwargs)

    # c = (c-np.nanmin(c)) / (np.nanmax(c) - np.nanmin(c))
    # c = (c-vmin) / (vmax-vmin)
    # colors = plt.colormaps[cmap](c)

    x = np.asarray(x)
    y = np.asarray(y)
    x_midpts = np.hstack((x[0], 0.5 * (x[1:] + x[:-1]), x[-1]))
    y_midpts = np.hstack((y[0], 0.5 * (y[1:] + y[:-1]), y[-1]))

    coord_start = np.column_stack((x_midpts[:-1], y_midpts[:-1]))[:, np.newaxis, :]
    coord_mid = np.column_stack((x, y))[:, np.newaxis, :]
    coord_end = np.column_stack((x_midpts[1:], y_midpts[1:]))[:, np.newaxis, :]
    segments = np.concatenate((coord_start, coord_mid, coord_end), axis=1)

    if vmin == 'auto':
        vmin = c.min()
    if vmax == 'auto':
        vmax = c.max()

    lc = LineCollection(segments, **default_kwargs)
    if (vmin==0) and (vmax ==1):
        lc.set_array(c)
    else:
        lc.set_array(c)
        lc.set(clim=(vmin, vmax))

    return ax.add_collection(lc)

# if __main__:
#     a = np.linspace(0, 20, 100)
#     b = np.sin(a)
#     fig,ax=plt.subplots()
#     ax.plot(a,b)
#     colored_line(x=a, y=b, c=b, cmap=shaded_cmap(color="tab:blue", shade_range=[0.1, .9]), ax=ax)
#     ax.set_aspect(1)
#     plt.show()


def adjust_lightness(color, factor=0.7):
    """
    Adjust lightness of a Matplotlib color using HLS space.

    Parameters
    ----------
    color : str or tuple
        Any Matplotlib-valid color.
    factor : float
        Lightness multiplier.
        1.0 = original
        <1  = darker
        >1  = lighter

    Returns
    -------
    tuple
        RGB tuple with adjusted lightness
    """
    import colorsys

    r, g, b = color
    h, l, s = colorsys.rgb_to_hls(r, g, b)

    l = max(0, min(1, l * factor))  # keep in [0,1]

    r_new, g_new, b_new = colorsys.hls_to_rgb(h, l, s)
    return (r_new, g_new, b_new)