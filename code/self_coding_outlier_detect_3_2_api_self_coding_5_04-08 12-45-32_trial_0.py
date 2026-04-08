### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Ensure output_data is not empty
    if len(output_data) == 0:
        return False
    # Ensure there are no missing values in output_data
    if np.any(np.isnan(output_data)):
        return False
    # Check if values in output_data are valid indices for input_data
    if np.any(output_data < 0) or np.any(output_data >= len(input_data)):
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    # Calculate mean and standard deviation of input data
    mean = np.mean(input_data)
    std_dev = np.std(input_data)
    
    # Calculate Z-scores
    z_scores = (input_data - mean) / std_dev
    
    # Anomaly threshold
    threshold = 3
    
    # Verify output_data indices correspond to anomalies
    for idx in output_data:
        if abs(z_scores[idx]) <= threshold:
            return False
    
    return True

### Index 2 ###
