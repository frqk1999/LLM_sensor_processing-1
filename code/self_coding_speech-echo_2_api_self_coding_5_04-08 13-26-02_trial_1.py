### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if output_data contains NaN or invalid values
    if np.isnan(output_data).any():
        return False
    # Check if output_data is empty
    if output_data.size == 0:
        return False
    # Check the value range for int16 audio data
    if np.min(output_data) < -32768 or np.max(output_data) > 32767:
        return False
    return True

### Index 1 ###
import numpy as np
from scipy.signal import correlate

def challenger(input_data, output_data, sampling_rate=None):
    # Autocorrelation of input_data and output_data
    autocorr_input = correlate(input_data, input_data, mode='full')
    autocorr_output = correlate(output_data, output_data, mode='full')
    
    # Lag where autocorrelation is maximum for both input and output
    lag_input = np.argmax(autocorr_input) - (len(input_data) - 1)
    lag_output = np.argmax(autocorr_output) - (len(output_data) - 1)
    
    # Maximum value of autocorrelation for both
    max_autocorr_input = np.max(autocorr_input)
    max_autocorr_output = np.max(autocorr_output)
    
    # Ratio of max autocorrelation of output to input
    reduction_factor = max_autocorr_output / max_autocorr_input if max_autocorr_input != 0 else 0
    
    # Echo considered sufficiently removed if reduction factor is below a threshold, e.g., <0.5
    return reduction_factor < 0.5

### Index 2 ###
