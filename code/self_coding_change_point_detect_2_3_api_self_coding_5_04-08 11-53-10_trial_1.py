### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False. 
    # Check if the output_data has the valid range, is empty, or contains missing values.
    import numpy as np
    
    # Check if the output_data is not empty and contains no missing values
    if len(output_data) == 0:
        return False
    if np.any(np.isnan(output_data)):
        return False
    
    # Check if all positions in output_data are valid indices in input_data
    if not all(0 <= pos < len(input_data) for pos in output_data):
        return False
    
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.stats import ttest_ind

    # Parameters
    window_size = 20  # As used in the solver to detect change points
    
    # Loop through detected change points to verify the statistical change
    for change_point in output_data:
        if (change_point - window_size < 0) or (change_point + window_size > len(input_data)):
            continue  # Skip if the window around change point is not possible
        
        segment_1 = input_data[change_point - window_size:change_point]
        segment_2 = input_data[change_point:change_point + window_size]
        
        # Perform t-test between the segments around the change point
        _, p_value = ttest_ind(segment_1, segment_2, equal_var=False, nan_policy='omit')
        
        # Check p-value for significance
        if p_value >= 0.05:
            return False  # If any detected change point does not have significant change, return False
    
    return True  # If all detected change points have significant changes, return True

### Index 2 ###
