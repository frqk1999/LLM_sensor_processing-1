### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data is empty or contains missing values.
    if output_data is None or len(output_data) == 0:
        return False
    if np.any(np.isnan(output_data)) or np.any(np.isinf(output_data)):
        return False
    
    # Check if the output_data is within reasonable numerical range by inspecting its min and max values.
    if np.min(output_data) < -1e6 or np.max(output_data) > 1e6:
        return False
    
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    # Import necessary library
    from scipy.signal import welch

    # Calculate the PSD to understand frequency distribution of the input and output signals
    # For the original signal
    original_freqs, original_psd = welch(input_data, fs=sampling_rate)
    # For the downsampled signal
    new_sampling_rate = sampling_rate / 2
    downsampled_freqs, downsampled_psd = welch(output_data, fs=new_sampling_rate)
    
    # Compute total power for frequencies below 25 Hz in both signals
    original_power_low_freq = np.sum(original_psd[original_freqs <= 25])
    downsampled_power_low_freq = np.sum(downsampled_psd[downsampled_freqs <= 25])

    # Check if low-frequency power is preserved
    if not np.isclose(original_power_low_freq, downsampled_power_low_freq, atol=1e-1 * original_power_low_freq):
        return False
    
    # Check that high-frequency components are dampened in the downsampled signal
    high_freq_power = np.sum(downsampled_psd[downsampled_freqs > 25])
    if high_freq_power > 1e-2 * downsampled_power_low_freq:  # Arbitrary threshold based on low-frequency power
        return False

    return True

### Index 2 ###
