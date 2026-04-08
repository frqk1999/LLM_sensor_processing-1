### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data is empty or contains missing values
    if len(output_data) == 0 or np.isnan(output_data).any():
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    # Loop over each detected change point
    for change_point in output_data:
        if change_point < 1 or change_point >= len(input_data) - 1:
            return False

        # Define a small window before and after each change point
        window_size = 5
        if change_point < window_size or change_point + window_size >= len(input_data):
            return False

        # Calculate mean values before and after the change point
        mean_before = np.mean(input_data[change_point - window_size:change_point])
        mean_after = np.mean(input_data[change_point:change_point + window_size])

        # Check if the means before and after the change point differ significantly
        if abs(mean_after - mean_before) <= 2 * np.std(input_data):
            return False

    # If all change points show significant mean changes, we return True
    return True

### Index 2 ###
