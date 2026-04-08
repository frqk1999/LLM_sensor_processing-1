### Index 0 ###
import numpy as np
from scipy.signal import welch, find_peaks

def inspection(input_data, sampling_rate=None):
    """
    Inspects properties of the pressure sensor signal for a foot while walking.

    Args:
        input_data (np.ndarray): The signal data.
        sampling_rate (float): The sampling rate of the signal in Hz.
    """
    # Check if signal is periodic
    if len(input_data) == 0:
        print("No data provided.")
        return
    
    # Welch\'s method to identify frequency components
    freqs, psd = welch(input_data, fs=sampling_rate)
    
    # Identify dominant frequency component peaks
    peaks, _ = find_peaks(psd)
    dominant_freqs = freqs[peaks]
    
    # Inspect the main frequency (physiological walking range typically 1-2 Hz)
    human_step_lower, human_step_upper = 1, 2
    valid_step_freqs = dominant_freqs[(dominant_freqs >= human_step_lower) & (dominant_freqs <= human_step_upper)]
    
    # Check for missing values
    missing_values = np.isnan(input_data).sum()

    # Print analysis
    print(f"Sampling rate: {sampling_rate} Hz")
    print(f"Estimated dominant frequencies: {dominant_freqs}")
    print(f"Valid step frequencies (1-2 Hz): {valid_step_freqs}")
    print(f"Number of missing values: {missing_values}")

def solver(input_data, sampling_rate=None):
    """
    Solves for the average step period in the provided pressure sensor data.

    Args:
        input_data (np.ndarray): The sensor data.
        sampling_rate (float): The sampling rate of the sensor data.
        
    Returns:
        np.ndarray: Average period of a step.
    """
    if len(input_data) == 0:
        raise ValueError("No data provided.")
    
    # Welch\'s method to identify frequency components
    freqs, psd = welch(input_data, fs=sampling_rate)
    
    # Identify dominant frequency peaks
    peaks, _ = find_peaks(psd)
    dominant_freqs = freqs[peaks]
    
    # Filter for frequencies within physiologically reasonable range for walking (1-2 Hz)
    human_step_lower, human_step_upper = 1, 2
    valid_step_freqs = dominant_freqs[(dominant_freqs >= human_step_lower) & (dominant_freqs <= human_step_upper)]
    
    if len(valid_step_freqs) == 0:
        raise ValueError("No valid walking frequencies found in the signal.")
    
    # Estimate the average step frequency
    average_step_freq = np.mean(valid_step_freqs)
    
    # Calculate the period
    average_step_period = 1 / average_step_freq
    
    return np.array([average_step_period])

### Index 1 ###
### Index 2 ###
