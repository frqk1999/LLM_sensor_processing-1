### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False.
    # 1) Check if the output_data has a valid range, is empty, or contains missing values. 
    # 2) Do NOT check the data type - using the isinstance or np.isscalar function is not reliable.
    # Args:
    #   input_data: The data type is numpy.ndarray. This is the data provided by the user to perform DSP. 
    #   output_data: The data type is numpy.ndarray. The variable is provided through the function interface for you. This is the data processed by the other AI agent. 
    #   sampling_rate: The sampling rate of the data. Sampling_rate is mandatory for speech, ECG, PPG, and gait data. It could be optional for others.
    # Output: boolean variable - True or False. If the result does not pass your test, output False. Else, output True.
    if output_data is None or len(output_data) == 0:
        return False
    
    if np.isnan(output_data).sum() > 0:
        return False
    
    if np.all((output_data >= 0) & (output_data < len(input_data))):
        return True 
    else:
        return False

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.stats import ttest_ind, levene

    change_points = output_data
    epsilon = 5  # Number of points around the change point to consider for comparison

    # Check if any true change in mean or variance around detected change points
    for cp in change_points:
        if cp - epsilon < 0 or cp + epsilon >= len(input_data):
            continue  # Skipping edge cases where comparison is not possible
        
        before_segment = input_data[max(0, cp - 2*epsilon):cp - epsilon]
        after_segment = input_data[cp + epsilon : min(len(input_data), cp + 2*epsilon)]

        # Check for a change in mean using t-test
        t_stat, p_value_mean = ttest_ind(before_segment, after_segment, equal_var=False)
        if p_value_mean >= 0.05:
            return False  # No significant change in mean detected

        # Check for a change in variance using Levene's test
        l_stat, p_value_variance = levene(before_segment, after_segment)
        if p_value_variance >= 0.05:
            return False  # No significant change in variance detected

    return True

### Index 2 ###
