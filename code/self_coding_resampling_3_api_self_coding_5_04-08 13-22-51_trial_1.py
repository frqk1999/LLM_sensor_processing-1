### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check for empty array
    if len(output_data) == 0:
        return False
    
    # Check for NaN or Infinite values
    if np.any(np.isnan(output_data)) or np.any(np.isinf(output_data)):
        return False

    # Check if the output_data is within a reasonable range, assuming it should resemble the input_data's range
    min_input, max_input = np.min(input_data), np.max(input_data)
    min_output, max_output = np.min(output_data), np.max(output_data)

    # Calculate an allowable range (perhaps stretching the input range by 20%)
    allowable_min = min_input - (0.2 * abs(min_input))
    allowable_max = max_input + (0.2 * abs(max_input))

    if min_output < allowable_min or max_output > allowable_max:
        return False

    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    # Import necessary library
    from scipy.signal import welch

    # Original sampling rate computation
    original_freqs, original_psd = welch(input_data, fs=sampling_rate)
    
    # New sampling rate after downsampling
    new_sampling_rate = sampling_rate / 2
    downsampled_freqs, downsampled_psd = welch(output_data, fs=new_sampling_rate)
    
    # Check if the main frequencies (low frequencies, below 25 Hz) are preserved
    original_main_freqs = original_freqs[original_freqs <= 25]
    original_main_psd = original_psd[original_freqs <= 25]
    
    downsampled_main_freqs = downsampled_freqs[downsampled_freqs <= 25]
    downsampled_main_psd = downsampled_psd[downsampled_freqs <= 25]
    
    # Test main frequencies are present in both
    if not np.allclose(original_main_psd, downsampled_main_psd, atol=1e-1): # Allow small tolerance due to filtering
        return False
    
    # Check if high-frequency components are sufficiently attenuated in the downsampled signal
    high_freq_psd = downsampled_psd[downsampled_freqs > 25]
    if np.any(high_freq_psd > 1e-2):  # Arbitrary threshold
        return False
    
    return True

### Index 2 ###
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

### Index 3 ###
