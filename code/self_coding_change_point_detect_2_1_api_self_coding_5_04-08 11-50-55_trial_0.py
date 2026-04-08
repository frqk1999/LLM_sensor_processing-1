### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Verify the validity of the output_data. 
    # 1) Check if the output_data is empty, invalid.
    
    if output_data.size == 0:
        return False
    
    if np.any(np.isnan(output_data)):
        return False

    # Check if the output_data values are within a possible range based on input data length.
    if np.any((output_data < 0) | (output_data >= input_data.size)):
        return False

    # If all checks are passed
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.stats import ks_2samp
    
    segment_length = 50
    change_positions = output_data

    # Verify the statistical differences around detected change points
    for change_pos in change_positions:
        if change_pos - segment_length < 0 or change_pos + segment_length > len(input_data):
            # Skip invalid segments
            continue
        
        segment1 = input_data[change_pos - segment_length:change_pos]
        segment2 = input_data[change_pos:change_pos + segment_length]
        
        # Perform a statistical test to validate the change
        statistic, p_value = ks_2samp(segment1, segment2)
        
        # Threshold for significance
        if p_value >= 0.05:  # No significant change found
            return False
        
    return True

### Index 2 ###
