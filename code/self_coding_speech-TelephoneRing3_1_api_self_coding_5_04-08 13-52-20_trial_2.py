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
    if output_data is None or len(output_data) == 0:
        return False
    if np.any(np.isnan(output_data)):
        return False
    if not np.all((output_data >= -32768) & (output_data <= 32767)):
        # Assuming 16-bit PCM audio valid range
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
    target_noise_freqs = [218.75, 406.25, 679.69]  # Frequencies identified as noise
    acceptable_noise_reduction_ratio = 0.1  # Significantly reduced power

    # Check for reduction in power at noise frequencies
    noise_reduced = True
    for freq in target_noise_freqs:
        idx_input = np.argmin(np.abs(f_input - freq))
        idx_output = np.argmin(np.abs(f_output - freq))
        if Pxx_output[idx_output] >= acceptable_noise_reduction_ratio * Pxx_input[idx_input]:
            noise_reduced = False
            break

    # Check that the speech frequency components are retained within 300 to 3400 Hz
    speech_freqs = (f_input >= 300) & (f_input <= 3400)
    if not np.all(Pxx_output[speech_freqs] <= Pxx_input[speech_freqs]):
        # Verify if there are unexpected reductions in the speech frequency range
        return False  # Indicates possible distortion or loss in the speech frequency components

    return noise_reduced

### Index 2 ###
