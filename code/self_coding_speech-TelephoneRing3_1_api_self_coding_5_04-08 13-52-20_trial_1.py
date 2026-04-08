### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False. 
    # 1) Check if the output_data has the valid range, is empty, or contains missing values. 
    # 2) Do NOT check the data type - using the isinstance or np.isscalar function is not reliable.
    # Args:
    #   input_data: The data type is numpy.ndarray. This is the data provided by the user to perform DSP. 
    #   output_data: The data type is numpy.ndarray. The variable is provided through the function interface for you. This is the data processed by the other AI agent. 
    #   sampling_rate: The sampling rate of the data. sampling_rate is mandatory for speech, ecg, ppg, and gait data. It could be optional for others.
    # Output: boolean variable - True or False. If the result does not pass your test, output False. Else, output True.

    # Check for empty output_data
    if output_data.size == 0:
        return False
    
    # Check for missing or NaN values in output_data
    if np.any(np.isnan(output_data)):
        return False

    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import welch

    # Calculate power spectral density (PSD) of both input and output signals
    f_input, Pxx_input = welch(input_data, fs=sampling_rate, nperseg=1024)
    f_output, Pxx_output = welch(output_data, fs=sampling_rate, nperseg=1024)

    # Define the threshold for acceptable noise frequency reduction
    threshold_reduction_ratio = 0.1  # Target frequency's power should be reduced significantly

    # Check if the target frequency's power is reduced adequately
    target_freq = 218.44
    idx_input = np.argmin(np.abs(f_input - target_freq))
    idx_output = np.argmin(np.abs(f_output - target_freq))
    
    # Calculate the power reduction at the target frequency
    if Pxx_output[idx_output] > threshold_reduction_ratio * Pxx_input[idx_input]:
        return False

    # Check that the speech frequency components are retained
    speech_freqs = (f_input >= 300) & (f_input <= 3400)
    if not np.all(Pxx_output[speech_freqs] <= Pxx_input[speech_freqs]):
        return False  # Indicates possible distortion in the speech component frequency

    return True

### Index 2 ###
