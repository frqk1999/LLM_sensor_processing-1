### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False.
    # Check if the output_data has the valid range, is empty, or contains missing values.
    
    # Check if output_data is not empty
    if output_data.size == 0:
        return False
    
    # Check for missing values (NaNs) in the output_data
    if np.any(np.isnan(output_data)):
        return False

    # Check for reasonable numeric range, which should be similar to input_data's range
    if np.min(output_data) < np.min(input_data) or np.max(output_data) > np.max(input_data):
        return False

    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    from scipy.signal import welch
    
    # Compute power spectral density of input and output signals
    freqs_input, psd_input = welch(input_data, fs=sampling_rate)
    freqs_output, psd_output = welch(output_data, fs=50)  # Output is downsampled to 50Hz

    # Focus on low-frequency components, e.g., 0-10Hz
    low_freq_components_input = np.sum(psd_input[(freqs_input >= 0) & (freqs_input <= 10)])
    low_freq_components_output = np.sum(psd_output[(freqs_output >= 0) & (freqs_output <= 10)])
    
    # Check if the proportion of low to total power is similar or preserved
    total_power_input = np.sum(psd_input)
    total_power_output = np.sum(psd_output)
    
    ratio_input = low_freq_components_input / total_power_input
    ratio_output = low_freq_components_output / total_power_output
    
    # Allow some tolerance in the ratio difference due to filter effects
    tolerance = 0.1
    if abs(ratio_input - ratio_output) > tolerance:
        return False
    
    return True

### Index 2 ###
