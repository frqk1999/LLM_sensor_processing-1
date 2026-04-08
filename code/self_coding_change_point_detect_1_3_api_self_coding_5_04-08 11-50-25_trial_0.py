### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data has the valid range, is empty, or contains missing values.
    if output_data is None or len(output_data) == 0:
        return False  # Check for empty output
    
    if np.isnan(output_data).any() or np.isinf(output_data).any():
        return False  # Check for NaN or infinite values in the output
    
    if not (0 <= output_data).all() or not (output_data <= len(input_data)).all():
        return False  # Ensure all change points are within the bounds of input_data

    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.stats import ttest_ind

    # Function to check for significant mean differences at change points
    def check_statistical_change(data, change_points):
        window_size = 50  # Assuming a window size similar to what's used in the solver
        for idx in change_points:
            # Ensure index is valid for window slicing
            if idx - window_size < 0 or idx >= len(data):
                continue
            # Create windows around the change point
            window_before = data[max(0, idx - window_size):idx]
            window_after = data[idx:min(len(data), idx + window_size)]
            # Perform a t-test to determine if there's a statistically significant difference
            stat, p_value = ttest_ind(window_before, window_after)
            if p_value >= 0.05:
                return False  # No significant change detected
        return True
    
    # Perform the statistical check at detected points
    return check_statistical_change(input_data, output_data)

### Index 2 ###
