### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False. 
    # 1) Check if the output_data has the valid range, is empty, or contains missing values. 
    # 2) Do NOT check the data type - using the isinstance or np.isscalar function is not reliable.
    # Args:
    #   input_data: The data type is numpy.ndarray. This is the data provided by the user to perform DSP. 
    #   output_data: The data type is numpy.ndarray. The variable is provided through the function interface for you. This is the data processed by the other AI agent. 
    #   sampling_rate: The sampling rate of the data. sampling_rate is mandatory for speech, ecg, ppg, and gait data. It could be optional for others.
    # Output: boolean variable - True or False. If the result does not pass your test, output False. Else, output True.

    import numpy as np

    # Check if the output is empty
    if output_data.size == 0:
        return False
    
    # Check for missing values
    if np.any(np.isnan(output_data)):
        return False

    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    # Check if the detected change points correspond to significant changes in the data.
    import numpy as np

    change_indices = output_data
    num_change_points = len(change_indices)

    # Set threshold for what constitutes a 'significant' change
    mean_change_threshold = np.std(input_data) * 0.5 # Example threshold
    variance_change_threshold = np.var(input_data) * 0.5 # Example threshold
    
    # Iterate over detected change points and analyze changes around those points
    for index in change_indices:
        if index <= 0 or index >= len(input_data) - 1:
            # Skip invalid indices
            continue
        
        # Calculate mean and variance before and after the change point
        window_size = 5
        prev_window = input_data[max(0, index - window_size):index]
        post_window = input_data[index:index + window_size]
        
        if len(prev_window) == 0 or len(post_window) == 0:
            # Skip if there are not enough data points for analysis
            continue
        
        mean_change = np.abs(np.mean(post_window) - np.mean(prev_window))
        variance_change = np.abs(np.var(post_window) - np.var(prev_window))

        # Check if changes in mean or variance around the change point are significant
        if mean_change < mean_change_threshold and variance_change < variance_change_threshold:
            return False

    # If all change points checked meet criteria, return True
    return True

### Index 2 ###
