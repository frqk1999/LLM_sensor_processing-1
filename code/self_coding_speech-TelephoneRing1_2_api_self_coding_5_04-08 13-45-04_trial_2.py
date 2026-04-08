### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the audio output_data has valid ranges, is empty, or contains missing values.
    if len(output_data) == 0:
        return False
    if np.isnan(output_data).any():
        return False
    if np.min(output_data) == 0 and np.max(output_data) == 0:
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    # Analyze the power spectral density of both input and output data.
    from scipy.signal import welch
    import numpy as np
    
    # Compute the power spectral density for both input and output
    freqs_in, Pxx_in = welch(input_data, fs=sampling_rate, nperseg=1024)
    freqs_out, Pxx_out = welch(output_data, fs=sampling_rate, nperseg=1024)
    
    # Target frequencies to remove based on the inspection
    target_freqs = [375, 2000]
    
    # Attenuation threshold: how many dB reduction should be expected at those frequencies?
    attenuation_threshold = 20  # Example threshold of 20dB attenuation
    
    # Check if the filter reduced the amplitude at the target frequencies significantly
    for target_freq in target_freqs:
        # Find the index nearest to the target frequency in the PSD
        idx_in = np.argmin(np.abs(freqs_in - target_freq))
        idx_out = np.argmin(np.abs(freqs_out - target_freq))
        
        # Calculate the attenuation in dB
        attenuation = 10 * np.log10(Pxx_in[idx_in] / Pxx_out[idx_out])
        
        # If the attenuation is less than the threshold, the filtering might not be effective
        if attenuation < attenuation_threshold:
            return False
    
    return True

### Index 2 ###
