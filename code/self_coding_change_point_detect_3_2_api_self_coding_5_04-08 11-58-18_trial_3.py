### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data is empty or contains missing values
    if len(output_data) == 0 or np.isnan(output_data).any():
        return False
    # Check if the indices are within the range of input_data
    if any(point < 0 or point >= len(input_data) for point in output_data):
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    from scipy.stats import skew, kurtosis
    
    # Iterate over each detected change point
    for change_point in output_data:
        if change_point < 1 or change_point >= len(input_data) - 1:
            return False

        # Define a window before and after each change point
        window_size = 10
        if change_point < window_size or change_point + window_size >= len(input_data):
            return False

        # Calculate statistical properties before and after the change point
        skew_before = skew(input_data[change_point - window_size:change_point])
        skew_after = skew(input_data[change_point:change_point + window_size])
        
        kurt_before = kurtosis(input_data[change_point - window_size:change_point])
        kurt_after = kurtosis(input_data[change_point:change_point + window_size])

        # Check if the skewness and kurtosis before and after the change point differ significantly
        if not (abs(skew_after - skew_before) > 0.5 or abs(kurt_after - kurt_before) > 0.5):
            return False

    # If all change points show significant distributional changes, we return True
    return True

### Index 2 ###
