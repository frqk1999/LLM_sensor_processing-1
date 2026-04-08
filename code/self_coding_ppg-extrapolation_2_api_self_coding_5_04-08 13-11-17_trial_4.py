### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if output_data is within a valid range and that it is not empty or contains missing values
    if (output_data.size == 0) or np.isnan(output_data).any() or np.isinf(output_data).any():
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import periodogram

    # Calculate the periodogram for the input data
    f_input, Pxx_input = periodogram(input_data, sampling_rate)
    
    # Determine the dominant frequencies of input_data
    dominant_freq_input = f_input[np.argsort(Pxx_input)[-3:]]

    # Calculate the periodogram for the output data
    f_output, Pxx_output = periodogram(output_data, sampling_rate)
    
    # Determine the dominant frequencies of the output data
    dominant_freq_output = f_output[np.argsort(Pxx_output)[-3:]]

    # Check the dominant frequencies from the predictions to those of the input
    freq_diff = np.abs(dominant_freq_input - dominant_freq_output)
    if np.mean(freq_diff) > 0.2:  # Allowable frequency difference threshold
        return False

    # Check the trend consistency between input and output data
    input_trend = np.polyfit(np.arange(len(input_data)), input_data, 1)
    output_trend = np.polyfit(np.arange(len(output_data)), output_data, 1)
    
    # If trend deviation is significantly high, it is concerning (e.g., 20% deviation)
    if (np.abs(output_trend[0] - input_trend[0]) / np.abs(input_trend[0]) > 0.2):
        return False
    
    return True

### Index 2 ###
