### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data has the valid range, is empty, or contains missing values.
    if output_data is None or len(output_data) == 0:
        return False
    if np.isnan(output_data).any():
        return False
    if np.max(output_data) > 1.0 or np.min(output_data) < -1.0:  # assuming normalized ECG data
        return False
    return True

### Index 1 ###
