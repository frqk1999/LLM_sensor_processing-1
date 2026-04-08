### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data is empty or contains missing values
    if len(output_data) == 0 or np.isnan(output_data).any():
        return False

    # Check if the values in output_data are within a valid range
    if (output_data < 0).any() or (output_data >= len(input_data)).any():
        return False
    
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    from scipy.stats import skew, kurtosis

    # Define a utility function to calculate significant changes
    def has_significant_change(before, after, threshold=0.5):
        mean_diff = abs(np.mean(after) - np.mean(before))
        var_diff = abs(np.var(after) - np.var(before))
        skew_diff = abs(skew(after) - skew(before))
        kurt_diff = abs(kurtosis(after) - kurtosis(before))

        return (mean_diff > threshold * np.std(input_data) or
                var_diff > threshold * np.var(input_data) or
                skew_diff > 0.5 or
                kurt_diff > 0.5)

    # Iterate over each detected change point
    for change_point in output_data:
        if change_point < 1 or change_point >= len(input_data) - 1:
            return False

        # Define a window size, ensuring it's substantial enough to calculate statistics
        window_size = 10
        if change_point < window_size or change_point + window_size >= len(input_data):
            return False

        # Extract windows before and after the change point
        before_window = input_data[change_point - window_size:change_point]
        after_window = input_data[change_point:change_point + window_size]

        # Check for significant change
        if not has_significant_change(before_window, after_window):
            return False

    # If all change points show significant distributional changes, we return True
    return True

### Index 2 ###
