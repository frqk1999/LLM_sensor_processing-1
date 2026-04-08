### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data has the valid range, is empty, or contains missing values.
    if output_data is None or len(output_data) == 0:
        return False
    if np.isnan(output_data).any() or np.isinf(output_data).any():
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    # Calculate the power spectral density of the input and output data
    freqs_input, power_spec_input = signal.welch(input_data, fs=sampling_rate)
    freqs_output, power_spec_output = signal.welch(output_data, fs=sampling_rate)
    
    # Identify the dominant frequency components in both input and output
    dominant_freqs_input = freqs_input[np.argsort(power_spec_input)[-3:]]
    dominant_freqs_output = freqs_output[np.argsort(power_spec_output)[-3:]]

    # Ratio of power in dominant frequencies
    power_ratio_input = np.sum(power_spec_input[np.argsort(power_spec_input)[-3:]]) / np.sum(power_spec_input)
    power_ratio_output = np.sum(power_spec_output[np.argsort(power_spec_output)[-3:]]) / np.sum(power_spec_output)
    
    # Check if the output preserves the dominant components and reduces noise
    if (set(dominant_freqs_input) == set(dominant_freqs_output) and
        power_ratio_output > power_ratio_input * 1.5):  # Ensure at least 50% improvement in power ratio
        return True
    return False

### Index 2 ###
