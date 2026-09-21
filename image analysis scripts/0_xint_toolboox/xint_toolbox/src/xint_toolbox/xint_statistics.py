import numpy as np
import scipy

def confidence_interval(data, confidence=0.95):
    """
    Calculate the confidence interval for the mean of a NumPy array.

    Parameters:
        data (array-like): Input data (1D NumPy array or list).
        confidence (float): Confidence level (e.g., 0.95 for 95%).

    Returns:
        (float, float): Lower and upper bounds of the confidence interval.
    """
    data = np.array(data).flatten()
    n = len(data)
    if n < 2:
        raise ValueError("At least two data points are required")
    mean = np.mean(data)
    sem = scipy.stats.sem(data)  # standard error of the mean
    margin = sem * scipy.stats.t.ppf((1 + confidence) / 2.0, n - 1)
    return margin