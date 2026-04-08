### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data is not empty
    if output_data.size == 0:
        return False
    
    # Check if the output_data contains any NaN or infinity values
    if np.isnan(output_data).any() or np.isinf(output_data).any():
        return False
    
    # Check if the output_data is within a reasonable range
    # Note: Since it's audio data, it's unnecessary to define an arbitrary range without context
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
    if np.any(Pxx_output[speech_freqs] > Pxx_input[speech_freqs]):
        # Verify if there are unexpected reductions in the speech frequency range
        return False  # Indicates possible distortion or loss in the speech frequency components

    return noise_reduced

### Index 2 ###
