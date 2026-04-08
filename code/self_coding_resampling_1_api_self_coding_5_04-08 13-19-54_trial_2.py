### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data has valid range, is empty, or contains missing values.
    if output_data.size == 0:
        return False
    if np.isnan(output_data).any():
        return False
    # Assuming a reasonable range for processed signals: let's say values should not exceed +/- 10 in standard cases.
    if (output_data < -10).any() or (output_data > 10).any():
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
