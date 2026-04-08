### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data has the valid range, is empty, or contains missing values.
    import numpy as np

    # Check if the output_data is empty
    if len(output_data) == 0:
        return False

    # Check if there are NaNs or missing values
    if np.any(np.isnan(output_data)):
        return False

    # Check for any extreme values that may indicate an issue
    if np.max(output_data) > 32767 or np.min(output_data) < -32768:
        return False

    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import welch

    # Calculate the power spectral density (PSD) of both input and output signals
    f_input, Pxx_input = welch(input_data, fs=sampling_rate, nperseg=1024)
    f_output, Pxx_output = welch(output_data, fs=sampling_rate, nperseg=1024)
    
    # Frequency identified as phone ringing noise
    target_noise_freq = 555  # Can be adjusted based on inspection results
    
    # Define acceptable reduction ratio for noise frequency
    acceptable_noise_reduction_ratio = 0.1  # Expect significant reduction in noise power

    # Check if the noise frequency power is reduced adequately
    idx_input = np.argmin(np.abs(f_input - target_noise_freq))
    idx_output = np.argmin(np.abs(f_output - target_noise_freq))
    
    # Calculate the power reduction ratio at the target noise frequency
    if Pxx_output[idx_output] > acceptable_noise_reduction_ratio * Pxx_input[idx_input]:
        return False

    # Ensure speech frequencies are retained within the range of 300 to 3400 Hz
    speech_freqs = (f_input >= 300) & (f_input <= 3400)
    if np.any(Pxx_output[speech_freqs] < 0.5 * Pxx_input[speech_freqs]):
        # If significant reduction is observed in speech frequencies, indicate distortion
        return False

    return True

### Index 2 ###
