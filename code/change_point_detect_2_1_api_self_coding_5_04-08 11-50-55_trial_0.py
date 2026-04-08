### Index 0 ###
def inspection(input_data, sampling_rate=None):
    import numpy as np
    import ruptures as rpt
    
    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("There are missing values in the input data.")

    # Using ruptures library to visually check for change points
    # We assume that the signal is likely stationary between change points
    model = "l2"  # Use a model appropriate for detecting changes in the mean
    algo = rpt.KernelCPD(kernel= "linear").fit(input_data)
    result = algo.predict(n_bkps=10)
    
    print(f"Detected potential change points at positions: {result}")

    # Check the mean or variance between change points for confirmation
    for i in range(len(result) - 1):
        start, end = result[i], result[i+1]
        segment_mean = np.mean(input_data[start:end])
        segment_var = np.var(input_data[start:end])
        print(f"Segment {i}: Mean = {segment_mean}, Variance = {segment_var}")

### Index 1 ###
def inspection(input_data, sampling_rate=None):
    import numpy as np
    import pandas as pd
    from scipy.stats import zscore

    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("There are missing values in the input data.")
    
    # Calculate z-scores to detect outliers which could indicate change points
    z_scores = zscore(input_data)
    threshold = 3  # A typical threshold for considering something as an outlier
    potential_changes = np.where(np.abs(z_scores) > threshold)[0]
    
    print(f"Potential change points based on z-scores at positions: {potential_changes}")

    # Analyzing rolling mean and variance to see the trend changes
    rolling_window = 10
    rolling_mean = pd.Series(input_data).rolling(window=rolling_window).mean()
    rolling_var = pd.Series(input_data).rolling(window=rolling_window).var()

    # Print some statistics to aid interpretation
    print(f"Mean of rolling mean values: {np.nanmean(rolling_mean)}")
    print(f"Mean of rolling variance values: {np.nanmean(rolling_var)}")

    # Detect abrupt changes in rolling statistics as potential change points
    change_positions_mean = np.where(np.abs(np.diff(rolling_mean)) > np.std(rolling_mean))[0]
    change_positions_var = np.where(np.abs(np.diff(rolling_var)) > np.std(rolling_var))[0]

    print(f"Detected change points based on rolling mean at positions: {change_positions_mean}")
    print(f"Detected change points based on rolling variance at positions: {change_positions_var}")

### Index 2 ###
def solver(input_data, sampling_rate=None):
    import numpy as np
    from scipy.stats import ks_2samp
    
    segment_length = 50  # Define the length of the segments to compare
    change_positions = []

    # Iterate through the data and compare adjacent segments
    for i in range(segment_length, len(input_data) - segment_length, segment_length):
        segment1 = input_data[i - segment_length:i]
        segment2 = input_data[i:i + segment_length]
        
        # Perform a statistical test to check if the two segments are from different distributions
        statistic, p_value = ks_2samp(segment1, segment2)
        
        # Use threshold to determine a significant change
        if p_value < 0.05:  # standard significance level
            change_positions.append(i)
    
    print(f"Detected change points at positions: {change_positions}")
    return np.array(change_positions)

### Index 3 ###
### Index 4 ###
