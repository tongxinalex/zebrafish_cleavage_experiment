import numpy as np
import scipy

# Write a function to calculate the nematic order
def nematic_order_filter(image, qmin=3, qmax=12):
    ys, xs = image.shape
    image_fft = scipy.fft.fft2(image)
    image_fft = scipy.fft.fftshift(image_fft)
    normalized_squared_modulus = (np.absolute(image_fft))**2
    
    # polar coordinates
    qx, qy = np.meshgrid(np.arange(ys)-(ys-1)/2, np.arange(xs)-(xs-1)/2)
    q = np.sqrt(qx**2 + qy**2)
    theta = np.arctan2(qy, qx)
    
    theta_bins = np.linspace(-np.pi, np.pi, 25)
    # theta_bin_centers = np.unique(theta)

    h_theta = []
    for i in range(24):
        theta_condition = np.logical_and(theta>=theta_bins[i], theta<=theta_bins[i+1] )
        q_condition = np.logical_and(q>=qmin, q<=qmax)
        conditions = np.logical_and(theta_condition, q_condition)
        h_theta.append(np.sum(normalized_squared_modulus[conditions]))
        
    theta_bin_centers = (theta_bins[1:] + theta_bins[:-1])/2
    h_theta = np.array(h_theta)
    h_theta = h_theta/np.sum(h_theta)
    q_xx = -np.sum(h_theta * (np.cos(theta_bin_centers)**2 - 1/2))
    q_xy = -np.sum(h_theta * np.cos(theta_bin_centers) * np.sin(theta_bin_centers))
    
    return [q_xx, q_xy]

# Write a function of applying the nematic order filter to full image
def nematic_order_of_full_image(image, windowsize=30, qmin=3, qmax=12, print_minmax=False):
    ys, xs = image.shape
    regions = {'y':windowsize, 'x':windowsize}
    nematic_order_shape = [ys//regions['y'], xs//regions['x']]

    boundaries = [ys%regions['y'], xs%regions['x']]
    boundary_starts = [int(boundaries[0]/2), int(boundaries[1]/2)]

    nematic_order_q_xx = np.empty(nematic_order_shape)
    nematic_order_q_xy = np.empty(nematic_order_shape)
    nematic_order_x = np.empty(nematic_order_shape)
    nematic_order_y = np.empty(nematic_order_shape)
    
    for j in range(nematic_order_shape[0]):
        for i in range(nematic_order_shape[1]):
            region = image[(boundary_starts[0]+j*regions['y']):(boundary_starts[0]+(j+1)*regions['y']),
                           (boundary_starts[1]+i*regions['x']):(boundary_starts[1]+(i+1)*regions['x'])]
            nematic_order_q_xx[j,i] = nematic_order_filter(region, qmin, qmax)[0]
            nematic_order_q_xy[j,i] = nematic_order_filter(region, qmin, qmax)[1]
            nematic_order_y[j,i] = ((boundary_starts[0]+j*regions['y']) + (boundary_starts[0]+(j+1)*regions['y'])) / 2
            nematic_order_x[j,i] = ((boundary_starts[1]+i*regions['x']) + (boundary_starts[1]+(i+1)*regions['x'])) / 2 

    if print_minmax:
        print('qxx range:', np.nanmin(nematic_order_q_xx), '~', np.nanmax(nematic_order_q_xx))
        print('qxy range:', np.nanmin(nematic_order_q_xy), '~', np.nanmax(nematic_order_q_xy))

    return [nematic_order_x, nematic_order_y, nematic_order_q_xx, nematic_order_q_xy]


# nematic order to angle
def nematic_to_vector(Q, q):
    theta = np.arctan2(q, Q)/2
    s = np.sqrt(q**2 + Q**2)
    n = [s*np.cos(theta), s*np.sin(theta)]
    return [s, np.array(n)]