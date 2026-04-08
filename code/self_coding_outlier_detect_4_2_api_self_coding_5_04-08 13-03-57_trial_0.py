### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if output_data is valid by confirming it has valid index values and is not empty 
    if len(output_data) == 0:
        return False
    if np.isnan(output_data).any():
        return False
    if (output_data < 0).any() or (output_data >= len(input_data)).any():
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.stats import zscore
    
    # Calculate z-scores for the input data
    z_scores = zscore(input_data)
    
    # Assume the same threshold as the solver for detecting outliers
    threshold = 3
    detected_outliers = np.where(np.abs(z_scores) > threshold)[0]
    
    # Compare whether the outliers detected in "output_data" match those identified here
    if list(detected_outliers) == list(output_data):
        return True
    else:
        return False

### Index 2 ###
