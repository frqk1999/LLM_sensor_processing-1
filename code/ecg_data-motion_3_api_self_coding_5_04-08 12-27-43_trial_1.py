### Index 0 ###
import numpy as np
from scipy.signal import find_peaks, welch

def inspection(input_data, sampling_rate):
    # Check for missing values
    if np.isnan(input_data).any():
        print("Signal contains missing values.")
    else:
        print("No missing values found in the signal.")

    # Check periodicity and find dominant frequency components
    f, Pxx = welch(input_data, fs=sampling_rate, nperseg=1024)
    print("Power Spectral Density calculated.")

    # Dominant frequency determination
    dominant_freq = f[np.argmax(Pxx)]
    print(f"Dominant frequency component: {dominant_freq} Hz")

    # Trend check
    peaks, _ = find_peaks(input_data)
    if len(peaks) > len(input_data) / (2 * sampling_rate):
        print("The signal has periodic components.")
    else:
        print("The signal appears to have a non-periodic trend.")

    # Check for low-frequency drift
    lf_power = np.sum(Pxx[f < 0.5])
    print(f"Low-frequency power (below 0.5 Hz): {lf_power}")

### Index 1 ###
from scipy.signal import butter, filtfilt

def solver(input_data, sampling_rate):
    # Define filter parameters
    nyquist = 0.5 * sampling_rate
    cutoff_freq = 0.75  # Adjusted cut-off frequency for baseline drift
    order = 2  # Filter order

    # Design a Butterworth high-pass filter
    b, a = butter(order, cutoff_freq / nyquist, btype='high', analog=False)
    
    # Apply the filter to the input data
    filtered_data = filtfilt(b, a, input_data)
    
    return filtered_data

### Index 2 ###
### Index 3 ###
