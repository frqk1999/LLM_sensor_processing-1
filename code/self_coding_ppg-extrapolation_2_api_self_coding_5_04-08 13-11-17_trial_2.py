### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Ensure output_data is not out of valid range, empty, nor contains missing values.
    if output_data is None or len(output_data) == 0:
        return False
    if np.any(np.isnan(output_data)):
        return False
    # Assuming valid range for PPG data as typical -1 to 1 for normalized signals
    if np.any(output_data > 1) or np.any(output_data < -1):
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

    # Check dominant frequencies of the prediction and alignment with input (allow small variance)
    freq_diff = np.abs(dominant_freq_input - dominant_freq_output)
    if np.mean(freq_diff) > 0.2:  # Threshold for acceptable frequency difference
        return False

    # Check the trend consistency between input and output data
    input_trend = np.polyfit(np.arange(len(input_data)), input_data, 1)
    output_trend = np.polyfit(np.arange(len(output_data)), output_data, 1)
    
    # If trend deviation is significantly high, it's problematic (e.g., 20% deviation)
    if (np.abs(output_trend[0] - input_trend[0]) / np.abs(input_trend[0]) > 0.2):
        return False
    
    return True

### Index 2 ###
