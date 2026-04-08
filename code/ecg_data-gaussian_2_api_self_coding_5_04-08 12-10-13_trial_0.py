### Index 0 ###
import numpy as np
import scipy.signal as signal

def inspection(input_data, sampling_rate=None):
    # Check if the signal is periodic and find dominant frequencies
    freqs, power_spec = signal.welch(input_data, fs=sampling_rate)
    dominant_frequencies = freqs[np.argsort(power_spec)[-3:]]  # Top 3 dominant frequencies
    is_periodic = len(dominant_frequencies) > 0 and np.max(power_spec) > 0.1 * np.sum(power_spec)
    
    # Check the trend of the signal
    trend = np.mean(np.diff(input_data))  # Calculate mean of differences, simple trend detection
    
    # Detect unwanted frequencies (Gaussian noise not detectable directly here but should have high randomness)
    # Check any missing values
    missing_values = np.isnan(input_data).sum()
    
    print("Inspection Results:")
    print(f"Is the signal periodic?: {\'Yes\' if is_periodic else \'No\'}")
    print(f"Dominant Frequencies: {dominant_frequencies} Hz")
    print(f"Trend in the signal: {\'None\' if np.abs(trend) < 1e-3 else trend}")
    print(f"Presence of missing values: {\'Yes\' if missing_values > 0 else \'No\'}")

# Waiting for input on whether the properties of the signal need further exploration.

### Index 1 ###
def solver(input_data, sampling_rate=None):
    # Design a bandpass filter to retain the dominant frequencies while reducing noise
    nyquist = 0.5 * sampling_rate
    low_cut = 0.5 / nyquist  # Low cut-off frequency in Nyquist units, typically ECG starts from 0.5 Hz
    high_cut = 45 / nyquist  # High cut-off frequency in Nyquist units, usually using up to 45 Hz for ECG
    
    # Design Butterworth filter
    b, a = signal.butter(4, [low_cut, high_cut], btype='band')
    
    # Apply the filter to the input_data
    filtered_data = signal.filtfilt(b, a, input_data)
    
    return filtered_data

[SUCCESS]

### Index 2 ###
def solver(input_data, sampling_rate=None):
    # Design a bandpass filter to retain the dominant frequencies while reducing noise
    nyquist = 0.5 * sampling_rate
    low_cut = 0.5 / nyquist  # Low cut-off frequency in Nyquist units, typically ECG starts from 0.5 Hz
    high_cut = 45 / nyquist  # High cut-off frequency in Nyquist units, usually using up to 45 Hz for ECG
    
    # Design Butterworth filter
    b, a = signal.butter(4, [low_cut, high_cut], btype='band')
    
    # Apply the filter to the input_data
    filtered_data = signal.filtfilt(b, a, input_data)
    
    return filtered_data

[SUCCESS]

### Index 3 ###
def solver(input_data, sampling_rate=None):
    # Design a bandpass filter to retain the dominant frequencies while reducing noise
    nyquist = 0.5 * sampling_rate
    low_cut = 0.5 / nyquist  # Low cut-off frequency in Nyquist units, typically ECG starts from 0.5 Hz
    high_cut = 45 / nyquist  # High cut-off frequency in Nyquist units, usually using up to 45 Hz for ECG
    
    # Design Butterworth filter
    b, a = signal.butter(4, [low_cut, high_cut], btype=\'band\')
    
    # Apply the filter to the input_data
    filtered_data = signal.filtfilt(b, a, input_data)
    
    return filtered_data

# After processing, indicate success of the operation
print("SUCCESS")

### Index 4 ###
