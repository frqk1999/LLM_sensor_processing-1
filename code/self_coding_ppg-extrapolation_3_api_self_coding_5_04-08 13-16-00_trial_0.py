### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False. 
    # 1) Check if the output_data has the valid range, is empty, or contains missing values. 
    import numpy as np

    # Check for empty array
    if output_data.size == 0:
        return False

    # Check for missing or NaN values
    if np.isnan(output_data).any():
        return False

    # Check for unreasonable values (optional, assuming PPG values won't be extreme)
    if (np.min(output_data) < -1000) or (np.max(output_data) > 5000):  # Assuming typical PPG value range
        return False
        
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    
    # Calculate dominant frequency of input data
    from scipy.signal import periodogram
    input_freq, input_power = periodogram(input_data, fs=sampling_rate)
    dominant_input_freq = input_freq[np.argmax(input_power)]
    
    # Calculate dominant frequency of output data
    output_freq, output_power = periodogram(output_data, fs=sampling_rate)
    dominant_output_freq = output_freq[np.argmax(output_power)]
    
    # Check if the dominant frequency of output is similar to input
    freq_threshold = 0.1  # Acceptable deviation in Hz
    if abs(dominant_input_freq - dominant_output_freq) > freq_threshold:
        return False
    
    # Check if the mean and variance of prediction is within a reasonable range of input
    mean_threshold = 0.5  # Acceptable mean deviation
    variance_threshold = 0.5  # Acceptable variance deviation
    if abs(np.mean(output_data) - np.mean(input_data)) > mean_threshold:
        return False
    if abs(np.var(output_data) - np.var(input_data)) > variance_threshold:
        return False
    
    return True

### Index 2 ###
