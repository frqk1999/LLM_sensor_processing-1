### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False. 
    # Check if the output_data has the valid range, is empty, or contains missing values. 
    if output_data is None or len(output_data) == 0:  # Check if output_data is empty
        return False
    if np.isnan(output_data).any():  # Check for missing values
        return False
    return True  # If all checks are passed, output True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=500):
    import numpy as np
    import scipy.signal as signal

    # Compute power spectral density of both input and output_data
    f_in, Pxx_in = signal.welch(input_data, fs=sampling_rate)
    f_out, Pxx_out = signal.welch(output_data, fs=sampling_rate)

    # Identify frequencies around 60 Hz in both input and output
    noise_freq = 60
    freq_tol = 1.5  # +/- frequency tolerance for detection
    
    # Determine power of the frequency range of interest in input and output
    def frequency_power(frequencies, powers, target_freq, tol):
        mask = (frequencies >= target_freq - tol) & (frequencies <= target_freq + tol)
        return np.sum(powers[mask])
    
    power_in_60Hz = frequency_power(f_in, Pxx_in, noise_freq, freq_tol)
    power_out_60Hz = frequency_power(f_out, Pxx_out, noise_freq, freq_tol)

    # Check if power at 60 Hz is significantly decreased in output
    noise_reduction_ratio = power_out_60Hz / power_in_60Hz if power_in_60Hz != 0 else 0
    significant_noise_reduction = noise_reduction_ratio < 0.1  # Less than 10% remaining

    return significant_noise_reduction

### Index 2 ###
