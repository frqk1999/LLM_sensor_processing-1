### Index 0 ###
import numpy as np
import scipy.signal as signal

def inspection(input_data, sampling_rate=None):
    # Check if the signal is periodic or non-periodic
    freqs, power_spectrum = signal.periodogram(input_data, fs=sampling_rate)
    
    # Check for dominant frequency components
    dominant_freqs = freqs[np.argsort(power_spectrum)[-3:]]  # Get top 3 dominant frequencies
    print(f"Dominant Frequency Components: {dominant_freqs} Hz")
    
    # Check for unwanted frequencies (like powerline noise around 50 Hz)
    powerline_freqs = freqs[(freqs >= 49) & (freqs <= 51)]
    powerline_power = power_spectrum[(freqs >= 49) & (freqs <= 51)]
    if np.any(powerline_power > np.median(power_spectrum) * 2):  # Arbitrary threshold to detect significant 50Hz noise
        print("Powerline noise detected at 50Hz frequency range")
    
    # Check for trend and non-stationarity
    trend = np.mean(np.gradient(input_data))
    print(f"Signal Trend (mean gradient): {trend}")
    
    # Check for missing values in the signal
    if np.any(np.isnan(input_data)):
        print("Missing values detected in the signal")
    else:
        print("No missing values detected")

# Note: The function does not return any value. It prints the inspection results.

### Index 1 ###
def solver(input_data, sampling_rate=None):
    # Design a notch filter to remove 50 Hz frequency
    notch_freq = 50.0  # Frequency to be removed from signal (Hz)
    quality_factor = 30.0  # Quality factor for the notch filter
    b_notch, a_notch = signal.iirnotch(notch_freq, quality_factor, sampling_rate)
    
    # Apply the notch filter to the input data
    filtered_data = signal.filtfilt(b_notch, a_notch, input_data)
    
    # Verify the effectiveness of the filter
    freqs, power_spectrum_input = signal.periodogram(input_data, fs=sampling_rate)
    _, power_spectrum_output = signal.periodogram(filtered_data, fs=sampling_rate)
    
    # Calculate the power at 50 Hz for input and output
    power_50hz_input = power_spectrum_input[np.argmin(np.abs(freqs - 50))]
    power_50hz_output = power_spectrum_output[np.argmin(np.abs(freqs - 50))]
    
    # Check if the power at 50 Hz is significantly reduced
    power_reduction = (power_50hz_input - power_50hz_output) / (power_50hz_input + 1e-10)  # Avoid division by zero
    
    threshold_reduction = 0.7  # Define a threshold for significant reduction (e.g., 70%)
    if power_reduction > threshold_reduction:
        print("Significant reduction of powerline noise achieved.")
    else:
        print("Failed to significantly reduce powerline noise.")
    
    return filtered_data

### Index 2 ###
### Index 3 ###
