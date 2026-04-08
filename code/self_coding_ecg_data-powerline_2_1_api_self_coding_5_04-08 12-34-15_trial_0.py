### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    import numpy as np
    
    # Check if the output_data has valid range, is empty, or contains missing values. 
    if output_data is None or len(output_data) == 0:
        return False
    if np.isnan(output_data).any():
        return False

    # Additional check could include verifying the amplitude range
    # Assuming normal ECG amplitude is between -5mV to 5mV.
    amplitude_range_valid = np.all((output_data <= 5) & (output_data >= -5))
    
    if not amplitude_range_valid:
        return False
    
    return True

# Assuming input_data and sampling_rate are provided from the question's context
print(inspection(input_data, output_data, sampling_rate=500))

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=500):
    import numpy as np
    from scipy.signal import periodogram

    # Calculate the power spectral density of the input and output signals
    freqs_input, power_spectrum_input = periodogram(input_data, sampling_rate)
    freqs_output, power_spectrum_output = periodogram(output_data, sampling_rate)

    # Define the powerline noise frequencies
    noise_frequencies = [50, 60]

    # Check if noise frequencies are attenuated in the output
    for noise_freq in noise_frequencies:
        # Find the index of the frequency closest to the noise frequency
        idx_input = np.argmin(np.abs(freqs_input - noise_freq))
        idx_output = np.argmin(np.abs(freqs_output - noise_freq))

        # Compare the power at this frequency in input vs output
        power_input = power_spectrum_input[idx_input]
        power_output = power_spectrum_output[idx_output]

        # Check if the output power is significantly lower than the input power
        if power_output >= 0.5 * power_input:  # Arbitrary threshold, often 0.1*input is significant reduction
            return False

    return True

### Index 2 ###
