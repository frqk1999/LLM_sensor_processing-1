### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data is empty, contains NaN, or has an unrealistic range.
    # Check for NaNs or infinite values
    if np.isnan(output_data).any() or np.isinf(output_data).any():
        return False
    # Check if the data is in a valid range, assuming ECG values shouldn't be extremely large or small.
    if np.min(output_data) < -1e9 or np.max(output_data) > 1e9:
        return False
    return True

### Index 1 ###
