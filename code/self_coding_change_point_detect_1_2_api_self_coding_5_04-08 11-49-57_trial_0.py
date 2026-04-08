### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Checking if output_data has valid values, is non-empty, and contains no missing values.
    if output_data is None or len(output_data) == 0:
        return False
    if any(output_data < 0) or any(output_data > len(input_data)):
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.stats import kstest

    # Normalize the data for consistency
    normalized_data = (input_data - np.mean(input_data)) / np.std(input_data)
    
    # Window size based on detected change positions
    window_size = 30
    num_checks = len(output_data)
    
    # Verify the change points
    for change_point in output_data:
        if change_point < window_size:
            continue
            
        pre_change_segment = normalized_data[change_point-window_size:change_point]
        post_change_segment = normalized_data[change_point:change_point+window_size]
        
        if len(pre_change_segment) < window_size or len(post_change_segment) < window_size:
            return False
        
        # Compare distribution before and after the change point
        _, p_value = kstest(pre_change_segment, post_change_segment)
        
        if p_value > 0.05:
            return False
    
    return True

### Index 2 ###
