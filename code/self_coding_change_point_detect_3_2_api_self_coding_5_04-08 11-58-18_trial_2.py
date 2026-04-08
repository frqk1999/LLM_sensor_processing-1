### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data has the valid range, is empty, or contains missing values. 
    if len(output_data) == 0 or np.isnan(output_data).any():
        return False
    if np.any(output_data < 0) or np.any(output_data >= len(input_data)):
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    # Loop over each detected change point
    for change_point in output_data:
        if change_point < 1 or change_point >= len(input_data) - 1:
            return False

        # Define a window before and after each change point
        window_size = 10
        if change_point < window_size or change_point + window_size >= len(input_data):
            return False

        # Calculate statistical properties before and after the change point
        mean_before = np.mean(input_data[change_point - window_size:change_point])
        mean_after = np.mean(input_data[change_point:change_point + window_size])
        
        var_before = np.var(input_data[change_point - window_size:change_point])
        var_after = np.var(input_data[change_point:change_point + window_size])

        # Check if the means and variances before and after the change point differ significantly
        if not (abs(mean_after - mean_before) > 2 * np.std(input_data) or abs(var_after - var_before) > 2 * np.var(input_data)):
            return False

    # If all change points show significant changes, we return True
    return True

### Index 2 ###
