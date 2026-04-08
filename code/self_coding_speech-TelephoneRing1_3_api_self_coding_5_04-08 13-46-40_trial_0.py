### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if output_data is valid
    if output_data is None or len(output_data) == 0:
        return False
    if np.any(np.isnan(output_data)):
        return False
    # Assuming 16-bit audio with range -32768 to 32767 for validity check
    if np.any(output_data < -32768) or np.any(output_data > 32767):
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    from scipy.signal import periodogram
    
    # Calculate the power spectral density (PSD) of the raw input signal
    freqs_input, power_input = periodogram(input_data, fs=sampling_rate)
    
    # Calculate the power spectral density (PSD) of the output (filtered) signal
    freqs_output, power_output = periodogram(output_data, fs=sampling_rate)
    
    # Specify the unwanted frequencies to check attenuation
    ringing_frequencies = [100.2, 110.22, 120.24, 200.40, 1009.21, 1609.21, 1723.44, 2026.05, 2114.22]
    
    # Check attenuation in output_data for these frequencies
    for freq in ringing_frequencies:
        # Find the index corresponding to the frequency
        idx_input = (np.abs(freqs_input - freq)).argmin()
        idx_output = (np.abs(freqs_output - freq)).argmin()
        
        # Check if the frequency has been attenuated in the output
        if power_output[idx_output] > power_input[idx_input] * 0.1:
            # The noise has not been sufficiently attenuated
            return False
    
    # If all targeted frequencies are sufficiently attenuated, return True
    return True

### Index 2 ###
