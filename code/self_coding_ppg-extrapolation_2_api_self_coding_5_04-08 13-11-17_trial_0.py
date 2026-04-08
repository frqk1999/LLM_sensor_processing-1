### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # 1. Check for validity
    # 1) Check if the output_data is not empty
    if len(output_data) == 0:
        return False
    
    # 2. Check if the output_data has the valid range (e.g., PPG data is typically within a certain range)
    if np.any(np.isnan(output_data)) or np.any(np.isinf(output_data)):
        return False

    # 3. Check for general statistical properties to ensure the data nature is not drastically different.
    # Typical PPG values within physiological range (assuming normalized or standard range).
    if np.min(output_data) < -2 or np.max(output_data) > 2:
        return False

    return True

# The function prototype employs variables passed through the interface (input_data, output_data, sampling_rate).
# In case of output_data being empty, having NaN or Inf values, or being out of physiological range, the data is deemed invalid.

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import periodogram

    # Calculate the periodogram for the input data
    f_input, Pxx_input = periodogram(input_data, sampling_rate)
    
    # Determine the dominant frequencies of input_data
    dominant_freq_input = f_input[np.argsort(Pxx_input)[-3:]]
    
    # Calculate the periodogram for the output data to check prediction
    f_output, Pxx_output = periodogram(output_data, sampling_rate)
    
    # Determine the dominant frequencies of output_data
    dominant_freq_output = f_output[np.argsort(Pxx_output)[-3:]]

    # Check that the dominant frequencies of the prediction match those of the input
    # Here we can allow a small variance due to prediction nature
    freq_diff = np.abs(dominant_freq_input - dominant_freq_output)
    if np.mean(freq_diff) > 0.2:  # Threshold for acceptable frequency difference
        return False

    # Check the trend consistency between input and output
    input_trend = np.polyfit(np.arange(len(input_data)), input_data, 1)
    output_trend = np.polyfit(np.arange(len(output_data)), output_data, 1)
    
    # If trend deviation is significantly high, let's clarify it (e.g. 20%)
    if (np.abs(output_trend[0] - input_trend[0]) / np.abs(input_trend[0]) > 0.2):
        return False
    
    return True

### Index 2 ###
