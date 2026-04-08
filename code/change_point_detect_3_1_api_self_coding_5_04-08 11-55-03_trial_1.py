### Index 0 ###
import numpy as np
import scipy.signal as signal
import ruptures as rpt

def inspection(input_data, sampling_rate=None):
    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("There are missing values in the input data.")
    else:
        print("No missing values found.")
        
    # Check for noise and apply Gaussian smoothing for preprocessing
    smoothed_data = signal.gaussian_filter1d(input_data, sigma=1)
    
    # Detect initial change points using various methods
    model = "l1"  # L1 norm is suitable for changes in mean
    algo = rpt.Pelt(model=model).fit(smoothed_data)
    change_points = algo.predict(pen=10)  # Initial penalty = 10, needs tuning
    
    print("Initial change points detected (may include false positives):", change_points)
    
    # TODO: Implement further validation with statistical tests (not executed here as per protocol)

### Index 1 ###
import numpy as np
import scipy.signal as signal
from scipy.stats import ttest_ind, levene

def inspection(input_data, sampling_rate=None):
    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("There are missing values in the input data.")
    else:
        print("No missing values found.")
    
    # Apply Gaussian smoothing for preprocessing
    smoothed_data = signal.gaussian_filter1d(input_data, sigma=1)
    print("Applied Gaussian smoothing to the input data.")

    # Manual change point detection method (e.g., evaluating rolling window statistics)
    window_size = 50  # Example window size
    threshold_mean = 1.0  # Example threshold for mean change
    threshold_var = 1.0  # Example threshold for variance change
    change_positions = []

    for i in range(window_size, len(smoothed_data) - window_size):
        left_segment = smoothed_data[i-window_size:i]
        right_segment = smoothed_data[i:i+window_size]

        # Check for change in mean
        t_stat, p_value_mean = ttest_ind(left_segment, right_segment)
        # Check for change in variance
        _, p_value_var = levene(left_segment, right_segment)

        # Detecting significant change in statistics (both mean and variance)
        if (p_value_mean < threshold_mean) or (p_value_var < threshold_var):
            change_positions.append(i)

    print("Detected potential change positions:", change_positions)

### Index 2 ###
import numpy as np
from scipy.ndimage import gaussian_filter1d
from scipy.stats import ttest_ind, levene

def inspection(input_data, sampling_rate=None):
    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("There are missing values in the input data.")
    else:
        print("No missing values found.")
    
    # Apply Gaussian smoothing for preprocessing using the correct module
    smoothed_data = gaussian_filter1d(input_data, sigma=1)
    print("Applied Gaussian smoothing to the input data.")

    # Manual change point detection method (e.g., evaluating rolling window statistics)
    window_size = 50  # Example window size
    threshold_mean = 0.05  # Example threshold for p-value of mean change
    threshold_var = 0.05  # Example threshold for p-value of variance change
    change_positions = []

    for i in range(window_size, len(smoothed_data) - window_size):
        left_segment = smoothed_data[i-window_size:i]
        right_segment = smoothed_data[i:i+window_size]

        # Check for change in mean
        t_stat, p_value_mean = ttest_ind(left_segment, right_segment)
        # Check for change in variance
        _, p_value_var = levene(left_segment, right_segment)

        # Detecting significant change in statistics (both mean and variance)
        if (p_value_mean < threshold_mean) or (p_value_var < threshold_var):
            change_positions.append(i)

    print("Detected potential change positions:", change_positions)

### Index 3 ###
import numpy as np
from scipy.ndimage import gaussian_filter1d
from scipy.stats import ttest_ind, levene

def inspection(input_data, sampling_rate=None):
    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("There are missing values in the input data.")
    else:
        print("No missing values found.")
    
    # Apply Gaussian smoothing for preprocessing using the correct module
    smoothed_data = gaussian_filter1d(input_data, sigma=1)
    print("Applied Gaussian smoothing to the input data.")

    # Manual change point detection method (e.g., evaluating rolling window statistics)
    window_size = 100  # Increased window size for more reliable segments
    threshold_mean = 0.01  # More stringent p-value threshold for mean change
    threshold_var = 0.01  # More stringent p-value threshold for variance change
    change_positions = []

    for i in range(window_size, len(smoothed_data) - window_size):
        left_segment = smoothed_data[i-window_size:i]
        right_segment = smoothed_data[i:i+window_size]

        # Check for change in mean
        t_stat, p_value_mean = ttest_ind(left_segment, right_segment)
        # Check for change in variance
        _, p_value_var = levene(left_segment, right_segment)

        # More stringent criteria for significant change in statistics
        if (p_value_mean < threshold_mean) and (p_value_var < threshold_var):
            change_positions.append(i)

    print("Detected potential change positions:", change_positions)

### Index 4 ###
import numpy as np
from scipy.ndimage import gaussian_filter1d
from scipy.stats import ttest_ind, levene

def solver(input_data, sampling_rate=None):
    # Apply Gaussian smoothing for preprocessing
    smoothed_data = gaussian_filter1d(input_data, sigma=1)
    
    window_size = 100  
    threshold_mean = 0.01  
    threshold_var = 0.01  
    change_positions = []

    for i in range(window_size, len(smoothed_data) - window_size):
        left_segment = smoothed_data[i-window_size:i]
        right_segment = smoothed_data[i:i+window_size]

        # Check for change in mean
        t_stat, p_value_mean = ttest_ind(left_segment, right_segment)
        # Check for change in variance
        _, p_value_var = levene(left_segment, right_segment)

        if (p_value_mean < threshold_mean) and (p_value_var < threshold_var):
            change_positions.append(i)
    
    # Return refined change positions if necessary 
    return np.array(change_positions)

### Index 5 ###
### Index 6 ###
