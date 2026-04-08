### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False. 
    # 1) Check if the output_data has the valid range, is empty, or contains missing values. 
    # 2) Do NOT check the data type.
    # Args:
    #   input_data: The data type is numpy.ndarray. This is the data provided by the user to perform DSP. 
    #   output_data: The data type is numpy.ndarray. The variable is provided through the function interface for you. This is the data processed by the other AI agent. 
    #   sampling_rate: The sampling rate of the data. Sampling_rate is mandatory for speech, ecg, ppg, and gait data. It could be optional for others.
    # Output: boolean variable - True or False. If the result does not pass your test, output False. Else, output True.
    
    import numpy as np
    
    # Check for missing (NaN) values and empty output
    if not output_data.size or np.isnan(output_data).any():
        return False
    
    # Check for valid range (assume a realistic range for normalized PPG signals)
    if output_data.min() < -5 or output_data.max() > 5:
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
    
    # Calculate the periodogram for the output data to check predictions
    f_output, Pxx_output = periodogram(output_data, sampling_rate)
    
    # Determine the dominant frequencies of output_data
    dominant_freq_output = f_output[np.argsort(Pxx_output)[-3:]]

    # Check that the dominant frequencies of the prediction align with those of the input (a small variance allowed)
    freq_diff = np.abs(dominant_freq_input - dominant_freq_output)
    if np.mean(freq_diff) > 0.2:  # Threshold for acceptable frequency difference
        return False

    # Check the trend consistency between input and output data
    input_trend = np.polyfit(np.arange(len(input_data)), input_data, 1)
    output_trend = np.polyfit(np.arange(len(output_data)), output_data, 1)
    
    # If the trend deviation is significantly high, it's problematic (e.g., 20% deviation)
    if (np.abs(output_trend[0] - input_trend[0]) / np.abs(input_trend[0]) > 0.2):
        return False
    
    return True

### Index 2 ###
