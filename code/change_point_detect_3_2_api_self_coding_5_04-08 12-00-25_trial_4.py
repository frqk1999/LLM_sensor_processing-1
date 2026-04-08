### Index 0 ###
import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis
from ruptures import detect_cusum

def inspection(input_data, sampling_rate=None):
    # Inspection step is not necessary for this task as we directly process the data.
    pass

def solver(input_data, sampling_rate=None):
    # Calculate basic statistics to establish dynamic thresholds
    mean = np.mean(input_data)
    std_dev = np.std(input_data)
    
    # Dynamic threshold based on overall variance and skewness
    skewness_threshold = std_dev * skew(input_data) / mean
    kurtosis_threshold = std_dev * kurtosis(input_data) / mean
    
    # Placeholder for detected change points
    change_points = []

    # CUSUM detection: identify small shifts effectively
    # Use detect_cusum utility from ruptures
    # We need to tune the parameters 'threshold' based on the data
    change_points = detect_cusum(input_data, threshold=0.01, drift=0.01)

    # Return only the change point positions
    return np.array(change_points)

### Index 1 ###
import numpy as np
from scipy.stats import skew, kurtosis

def inspection(input_data, sampling_rate=None):
    # Inspection step is not necessary for this task as we directly process the data.
    pass

def solver(input_data, sampling_rate=None):
    # Calculate basic statistics to establish dynamic thresholds
    mean = np.mean(input_data)
    std_dev = np.std(input_data)
    
    # Dynamic thresholds based on overall variance and skewness
    skewness_threshold = std_dev * abs(skew(input_data)) / mean
    kurtosis_threshold = std_dev * abs(kurtosis(input_data)) / mean

    # Initialize change points list
    change_points = []

    # Parameters for CUSUM
    mean_estimated = np.mean(input_data)
    cusum_pos = 0
    cusum_neg = 0
    threshold = std_dev * 0.5  # Threshold for detecting changes
    
    # Loop through the data to find change points using simple CUSUM algorithm
    for index in range(1, len(input_data)):
        deviation = input_data[index] - mean_estimated
        cusum_pos += deviation
        cusum_neg -= deviation
        
        if cusum_pos > threshold or cusum_neg > threshold:
            change_points.append(index)
            cusum_pos = 0
            cusum_neg = 0

    return np.array(change_points)

### Index 2 ###
### Index 3 ###
