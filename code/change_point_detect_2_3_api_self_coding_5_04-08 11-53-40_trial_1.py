### Index 0 ###
def inspection(input_data, sampling_rate=None):
    import numpy as np
    import pandas as pd
    
    # Step 1: Check for missing values
    if np.any(pd.isnull(input_data)):
        print("There are missing values in the input data.")
    else:
        print("No missing values found.")
    
    # Step 2: Determine if the signal is periodic (not focus here since we are detecting change points)
    # Step 3: Check trends and unexpected artifacts
    # We can use moving average or plotting, but since visualization is not possible let\'s use basic descriptive stats.
    mean = np.mean(input_data)
    std = np.std(input_data)
    print(f"Signal Mean: {mean}, Signal Standard Deviation: {std}")
    
    # Step 4: Basic Stationarity Check - using Rolling Mean/Variance
    rolling_mean = pd.Series(input_data).rolling(window=10).mean()
    if np.any(np.diff(rolling_mean)):
        print("Signal likely has changing mean.")
    
    # Step 5: Detecting change points is part of solver, so keeping inspection basic.
    print("Inspection completed. Proceeding to detect change points.")

### Index 1 ###
def solver(input_data, sampling_rate=None):
    import ruptures as rpt
    
    # Use the PELT method from the ruptures library for change point detection
    algo = rpt.Pelt(model="rbf").fit(input_data)
    # Apply Binary Segmentation to find change points based on specified penalty; adjust as necessary
    change_points = algo.predict(pen=10)  # The penalty value may need adjustment based on data
    
    print(f"Detected change points at positions: {change_points[:-1]} (before last point in series)")
    return change_points[:-1]  # Return positions without the last point (end of data)

### Index 2 ###
def solver(input_data, sampling_rate=None):
    import numpy as np
    from scipy.stats import ttest_ind
    
    # Parameters
    window_size = 20  # This determines the size of the segments to compare; adjust as needed
    change_points = []
    
    # Loop through the data to compute t-test on windowed segments
    for i in range(0, len(input_data) - 2 * window_size, window_size):
        segment_1 = input_data[i:i + window_size]
        segment_2 = input_data[i + window_size:i + 2 * window_size]
        
        # Perform t-test between the segments
        _, p_value = ttest_ind(segment_1, segment_2, equal_var=False, nan_policy=\'omit\')
        
        # Consider a change point if p-value is significant (common threshold is 0.05)
        if p_value < 0.05:
            change_points.append(i + window_size)
    
    # Print detected change points
    print(f"Detected change points at positions: {change_points}")
    return np.array(change_points)

### Index 3 ###
### Index 4 ###
