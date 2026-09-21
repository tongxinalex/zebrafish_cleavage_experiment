import numpy as np

def calculate_curve_length(points):
    """
    Calculate the length of a 3D curve given as an (N, 3) NumPy array.
    
    Parameters:
        points (np.ndarray): An array of shape (N, 3) representing the curve.
    
    Returns:
        float: The total arc length of the curve.
    """
    diffs = np.diff(points, axis=0)
    segment_lengths = np.linalg.norm(diffs, axis=1)
    return np.sum(segment_lengths)

def find_zero_crossings(arr):
    arr = np.asarray(arr)
    zero_crossings = []

    for i in range(1, len(arr)):
        if arr[i - 1] * arr[i] < 0:
            # Linear interpolation to estimate the zero-crossing point
            x0 = i - 1
            y0 = arr[i - 1]
            y1 = arr[i]
            x_cross = x0 - y0 * (1 / (y1 - y0))  # solving y=0 between y0 and y1
            zero_crossings.append(x_cross)

    return zero_crossings

def find_closest(array, target):
    array = np.array(array)
    if isinstance(target, int) or isinstance(target, float):
        idx = np.abs(array - target).argmin()
        outcome = array[idx]
        return [outcome, idx]
    else:
        target = np.array(target)
        idx_s = []
        for each_target in target.flatten():
            idx = np.abs(array - each_target).argmin()
            idx_s.append(idx)
        idx_s = np.array(idx_s)
        outcomes = array[idx_s]
        idx_s = idx_s.reshape(target.shape)
        outcomes = outcomes.reshape(target.shape)
        return [outcomes, idx_s]