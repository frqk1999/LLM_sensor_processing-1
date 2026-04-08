### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if output_data is empty or contains missing values
    if output_data.size == 0 or np.isnan(output_data).any():
        return False

    # Check if any data point in the output_data is non-finite
    if not np.all(np.isfinite(output_data)):
        return False

    return True

# Given that output_data is: 
# [ 0.00000000e+00, 1.49577953e-01, 6.28749695e-01, ... , -2.61602919e-01]

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import welch
    
    # Compute power spectral density of input and output signals
    freqs_input, psd_input = welch(input_data, fs=sampling_rate)
    freqs_output, psd_output = welch(output_data, fs=50)  # The output is downsampled to 50Hz

    # Define a frequency range for low-frequency components
    low_frequency_range = (0, 10)

    # Calculate the sum of the power spectral density in the low-frequency range
    low_freq_power_input = np.sum(psd_input[(freqs_input >= low_frequency_range[0]) & (freqs_input <= low_frequency_range[1])])
    low_freq_power_output = np.sum(psd_output[(freqs_output >= low_frequency_range[0]) & (freqs_output <= low_frequency_range[1])])
    
    # Calculate the total power of input and output signals
    total_power_input = np.sum(psd_input)
    total_power_output = np.sum(psd_output)

    # Calculate the ratio of low-frequency power to total power
    ratio_input = low_freq_power_input / total_power_input
    ratio_output = low_freq_power_output / total_power_output

    # Allow some tolerance in the ratio differences due to filtering effects
    tolerance = 0.1
    # Verify if the low-frequency component is preserved
    if abs(ratio_input - ratio_output) > tolerance:
        return False

    return True

### Index 2 ###
