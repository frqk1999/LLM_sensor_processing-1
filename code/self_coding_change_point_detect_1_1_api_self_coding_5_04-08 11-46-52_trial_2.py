### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data meets the criteria:
    # 1) It should not be empty.
    # 2) It should not contain NaN values.
    # These criteria ensure that the output_data is operationally valid.
    if len(output_data) == 0:
        return False
    if np.any(np.isnan(output_data)):
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    # Define window size for evaluation
    window_size = 50
    
    # Ensure that the output_data (change points) are sorted
    change_points = np.sort(output_data)  
    
    # Check for significant changes in the means around each detected change point
    for i in change_points:
        if i < window_size or i + window_size > len(input_data):
            continue
        
        # Compute the mean of segments before and after the change point
        before_mean = np.mean(input_data[i - window_size:i])
        after_mean = np.mean(input_data[i:i + window_size])
        
        # Check if the difference in means is significant
        if np.abs(after_mean - before_mean) < np.std(input_data) * 0.5:
            return False
    
    # If all detected change points passed the significance test
    return True

### Index 2 ###
