### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False. 
    # 1) Check if the output_data has the valid range, is empty, or contains missing values.
    # Args:
    #   input_data: The data type is numpy.ndarray. This is the data provided by the user to perform DSP. 
    #   output_data: The data type is numpy.ndarray. The variable is provided through the function interface for you. This is the data processed by the other AI agent. 
    #   sampling_rate: The sampling rate of the data.
    # Output: boolean variable - True or False. If the result does not pass your test, output False. Else, output True.
    
    import numpy as np
    
    # Check if output_data is empty or contains missing values
    if output_data.size == 0 or np.any(np.isnan(output_data)):
        return False
    
    # Check if output_data has exactly one element since it's supposed to be a single scalar in np.ndarray
    if output_data.shape != (1,):
        return False
    
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=300):
    # HERE is where you put your sanity check code.
    # Args:
    #   input_data: The data type is numpy.ndarray. The variable is provided through the function interface for you. This is the data provided by the user to perform DSP.
    #   output_data: The data type is numpy.ndarray. The variable is provided through the function interface for you. This is the data processed by the other AI agent. 
    #   sampling_rate: The sampling rate of the data.
    # Return: boolean variable - True or False. If your the result does not pass your test, output False. Else, output True.
    
    import numpy as np
    from scipy.signal import welch
    
    # Calculate power spectral density to find dominant frequencies
    freqs, psd = welch(input_data, fs=sampling_rate)
    dominant_freq_indices = np.argsort(psd)[-3:]  # Get top 3 frequency indices
    dominant_freqs = freqs[dominant_freq_indices]
    
    # Convert dominant frequencies to periods
    dominant_periods = 1 / dominant_freqs
    
    # Check if the calculated average period matches one of the dominant periods within a reasonable range
    estimated_period = output_data[0]
    tolerance = 0.05  # Allow small tolerance for variability
    period_match = any(np.isclose(dominant_period, estimated_period, atol=tolerance) for dominant_period in dominant_periods)
    
    return period_match

### Index 2 ###
