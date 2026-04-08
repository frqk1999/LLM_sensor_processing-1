### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data has the valid range, is empty, or contains missing values. 
    # Args:
    #   input_data: numpy.ndarray
    #   output_data: numpy.ndarray
    #   sampling_rate: int (optional)
    # Output: boolean

    # Ensure the output is not empty
    if output_data.size == 0:
        return False
    
    # Ensure there are no missing or NaN values in the output
    if np.isnan(output_data).any():
        return False

    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import periodogram
    
    # Frequency range calculation for input and output signals
    input_freq, input_Pxx = periodogram(input_data, sampling_rate)
    output_freq, output_Pxx = periodogram(output_data, sampling_rate / 2)
    
    # Main frequency components in input data should be low frequencies (e.g., < 25 Hz)
    main_input_freq_indices = np.where(input_Pxx > np.max(input_Pxx) * 0.2)[0]
    main_input_freqs = input_freq[main_input_freq_indices]
    
    # Main frequency components in output data should match those in the input data
    main_output_freq_indices = np.where(output_Pxx > np.max(output_Pxx) * 0.2)[0]
    main_output_freqs = output_freq[main_output_freq_indices]
    
    # Check if the main frequencies are preserved in the downsampled data
    for freq in main_input_freqs:
        # Allow some tolerance due to resolution limits and processing
        if not np.any((main_output_freqs >= freq - 0.5) & (main_output_freqs <= freq + 0.5)):
            return False

    # Check if the higher frequency components above 25 Hz are attenuated after downsampling
    high_freq_indices = np.where(output_freq > 25)[0]
    if np.any(output_Pxx[high_freq_indices] > np.max(input_Pxx) * 0.2):
        return False

    return True

### Index 2 ###
