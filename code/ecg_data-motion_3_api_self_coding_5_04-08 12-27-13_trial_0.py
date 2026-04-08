### Index 0 ###
import numpy as np
from scipy.signal import find_peaks, welch

def inspection(input_data, sampling_rate=500):
    # Check if there are missing values
    if np.any(np.isnan(input_data)):
        print("The signal contains missing values.")
    else:
        print("No missing values detected in the signal.")

    # Check for periodicity by examining the prominent frequency components
    freqs, power = welch(input_data, fs=sampling_rate)
    dominant_freq_idx = np.argmax(power)
    dominant_frequency = freqs[dominant_freq_idx]
    print(f"Dominant frequency component (peak power): {dominant_frequency} Hz")

    # Check if the signal shows a trend, indicating baseline drift
    trend = np.polyfit(np.arange(len(input_data)), input_data, 1)[0]
    if abs(trend) > 0.01:
        print(f"Trend detected: The signal has a baseline drift with a slope of {trend:.5f}")

    # Check for unwanted low-frequency components that may correspond to motion artifacts
    # Typically, motion artifacts affect the frequency range below 0.5 Hz, which contributes to baseline drift
    low_freq_power = np.sum(power[freqs < 0.5])
    if low_freq_power > np.sum(power)*0.1:
        print("Significant low-frequency power detected, indicating possible motion artifacts.")

# This function will only print the inspection results, no return value is required

### Index 1 ###
from scipy.signal import butter, filtfilt

def solver(input_data, sampling_rate=500):
    # Design a high-pass Butterworth filter to remove the baseline drift
    # We'll choose a cut-off frequency just below the normal ECG signal frequencies (e.g., 0.5 Hz)
    cutoff_frequency = 0.5  # in Hz
    order = 2  # Filter order, can be adjusted if needed
    nyquist = 0.5 * sampling_rate
    normal_cutoff = cutoff_frequency / nyquist
    
    # Create and apply the high-pass Butterworth filter
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    filtered_data = filtfilt(b, a, input_data)
    
    return filtered_data

### Index 2 ###
### Index 3 ###
