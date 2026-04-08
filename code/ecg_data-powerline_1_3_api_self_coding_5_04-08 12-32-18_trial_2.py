### Index 0 ###
import numpy as np
from scipy.signal import periodogram

def inspection(input_data, sampling_rate=None):
    if sampling_rate is None:
        raise ValueError("Sampling rate must be provided for ECG data")
    
    # Check for periodicity and dominant frequency components
    freqs, power = periodogram(input_data, fs=sampling_rate)
    
    # Find the dominant frequency
    dominant_freq = freqs[np.argmax(power)]
    
    print(f"Dominant Frequency: {dominant_freq} Hz")

    # Check for 50 Hz interference
    powerline_index = np.argmin(np.abs(freqs - 50.0))
    powerline_power = power[powerline_index]
    print(f"Power at 50 Hz: {powerline_power:.4f}")

    # Check if there are any missing values
    if np.any(np.isnan(input_data)):
        print("There are missing values in the input data.")
    else:
        print("No missing values found.")
    
    # Simple trend check (using first and last values)
    if input_data[0] != input_data[-1]:
        trend = "upward" if input_data[-1] > input_data[0] else "downward"
        print(f"Signal Trend: {trend}")
    else:
        print("No significant trend detected.")
    
    # Summary
    if powerline_power > np.mean(power):
        print("50 Hz powerline noise detected. Recommend filtering.")
    else:
        print("No significant 50 Hz noise detected.")
    
    # If other sources of corruption are necessary to check, they won\'t be visible from this inspection alone.

### Index 1 ###
from scipy.signal import iirnotch, filtfilt

def solver(input_data, sampling_rate=None):
    if sampling_rate is None:
        raise ValueError("Sampling rate must be provided for ECG data")
    
    # Design Notch Filter
    f0 = 50.0  # Frequency to remove (50Hz powerline noise)
    Q = 30.0   # Quality factor
    b, a = iirnotch(f0, Q, sampling_rate)
    
    # Apply Notch Filter
    filtered_data = filtfilt(b, a, input_data)
    
    # Verify Effectiveness
    freqs, power = periodogram(filtered_data, fs=sampling_rate)
    powerline_index = np.argmin(np.abs(freqs - f0))
    powerline_power_after = power[powerline_index]
    print(f"Post-filtering power at {f0} Hz: {powerline_power_after:.4f}")
    
    # Return filtered signal
    return filtered_data

### Index 2 ###
### Index 3 ###
