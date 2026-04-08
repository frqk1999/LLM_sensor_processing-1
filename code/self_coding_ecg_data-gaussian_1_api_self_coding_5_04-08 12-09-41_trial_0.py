### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False.
    # 1) Check if the output_data has the valid range, is empty, or contains missing values. 
    # 2) Do NOT check the data type - using the isinstance or np.isscalar function is not reliable.
    import numpy as np
    
    # Check if the output_data is empty
    if len(output_data) == 0:
        return False
    
    # Check for missing values
    if np.any(np.isnan(output_data)):
        return False
        
    # Check for infinite values
    if np.any(np.isinf(output_data)):
        return False
    
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.fft import fft, fftfreq
    
    # Convert signals to frequency domain
    n_input = len(input_data)
    n_output = len(output_data)
    
    input_fft = np.abs(fft(input_data))[:n_input // 2]
    output_fft = np.abs(fft(output_data))[:n_output // 2]
    
    freq_input = fftfreq(n_input, 1/sampling_rate)[:n_input // 2]
    freq_output = fftfreq(n_output, 1/sampling_rate)[:n_output // 2]
    
    # Check frequency ranges for input and output
    low_freq_threshold = 0.5
    high_freq_threshold = 150.0
    
    # Compute the power in the low-frequency and high-frequency range
    input_power_low = np.sum(input_fft[(freq_input >= low_freq_threshold) & (freq_input <= high_freq_threshold)])
    input_power_high = np.sum(input_fft[freq_input > high_freq_threshold])
    
    output_power_low = np.sum(output_fft[(freq_output >= low_freq_threshold) & (freq_output <= high_freq_threshold)])
    output_power_high = np.sum(output_fft[freq_output > high_freq_threshold])
    
    # Ensure low frequency is preserved and high-frequency noise is reduced
    if output_power_low >= 0.9 * input_power_low and output_power_high < 0.5 * input_power_high:
        return True  # Noise was filtered correctly
    else:
        return False  # Filtering wasn't effective

### Index 2 ###
