### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    import numpy as np

    # Check for any anomalies in the output_data
    if output_data is None or len(output_data) == 0:
        return False  # Output data cannot be empty
    if np.any(np.isnan(output_data)):
        return False  # Output data must not have missing values
    if np.max(output_data) > 32767 or np.min(output_data) < -32768:
        return False  # Assuming 16-bit PCM audio; values should be in a valid range

    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import welch

    # Calculate power spectral density (PSD) of input and output to compare
    f_input, Pxx_input = welch(input_data, fs=sampling_rate, nperseg=1024)
    f_output, Pxx_output = welch(output_data, fs=sampling_rate, nperseg=1024)

    # Define threshold for acceptable reduction in power of noise frequencies
    acceptable_noise_reduction = 0.1  # Significantly reduced power

    # Frequency bands to check (example, based on noise detected frequencies)
    noise_freqs = [203.125, 218.75, 312.5, 328.125]

    # Check for reduction in noise power
    noise_reduced = True
    for freq in noise_freqs:
        idx_input = np.argmin(np.abs(f_input - freq))
        idx_output = np.argmin(np.abs(f_output - freq))
        if Pxx_output[idx_output] >= acceptable_noise_reduction * Pxx_input[idx_input]:
            noise_reduced = False
            break

    return noise_reduced

### Index 2 ###
