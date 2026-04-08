### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check the validity of the output_data
    if output_data is None or len(output_data) == 0 or np.any(np.isnan(output_data)):
        return False
    
    # Ensure the output contains a positive period
    if output_data[0] <= 0:
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
    
    # Convert dominant frequencies to periods in frames
    dominant_periods_in_frames = sampling_rate / dominant_freqs
    
    # Check if the calculated average period matches one of the dominant periods in frames within a reasonable range
    estimated_period = output_data[0]
    tolerance = 5  # Allow small tolerance for variability in frames
    period_match = any(np.isclose(dominant_period, estimated_period, atol=tolerance) for dominant_period in dominant_periods_in_frames)
    
    return period_match

### Index 2 ###
