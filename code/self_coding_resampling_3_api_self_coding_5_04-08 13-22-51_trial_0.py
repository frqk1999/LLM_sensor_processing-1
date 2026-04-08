### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # 1) Check if the output_data is within a reasonable range, not empty, and contains finite values.
    if not output_data.size or not np.all(np.isfinite(output_data)):
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    # Compute the Fourier transform of both input and downsampled signals
    from scipy.signal import welch
    
    # Original sampling rate
    original_freqs, original_psd = welch(input_data, fs=sampling_rate)
    
    # New sampling rate after downsampling
    new_sampling_rate = sampling_rate / 2
    downsampled_freqs, downsampled_psd = welch(output_data, fs=new_sampling_rate)
    
    # Check if the main frequencies (low frequencies, below 25 Hz) are preserved
    original_main_freqs = original_freqs[original_freqs <= 25]
    original_main_psd = original_psd[original_freqs <= 25]
    
    downsampled_main_freqs = downsampled_freqs[downsampled_freqs <= 25]
    downsampled_main_psd = downsampled_psd[downsampled_freqs <= 25]
    
    # Confirm that main frequencies are present in both
    if not np.allclose(original_main_psd, downsampled_main_psd, atol=1e-1):
        return False
    
    # Verify if high-frequency components are attenuated in the downsampled signal
    high_freq_psd = downsampled_psd[downsampled_freqs > 25]
    if np.any(high_freq_psd > 1e-2): # Arbitrary threshold
        return False
    
    return True

### Index 2 ###
