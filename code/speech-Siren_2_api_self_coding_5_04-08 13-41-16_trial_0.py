### Index 0 ###
import numpy as np
from scipy.signal import find_peaks, welch

def inspection(input_data, sampling_rate=None):
    # 1) Check if the signal is periodic or non-periodic
    _, power_spectrum = welch(input_data, fs=sampling_rate)
    peaks, _ = find_peaks(power_spectrum)
    
    if len(peaks) > 0:
        print("Signal appears to have periodic components.")
        dominant_freqs = np.argsort(power_spectrum[peaks])[::-1][:2]  # Find two largest peaks
        print("Dominant frequencies:", dominant_freqs)

    # 2) Check the trend of the signals
    trend = np.polyfit(np.arange(len(input_data)), input_data, 1)
    print("Signal trend (approx):", trend)

    # 3) Check if there is any source of corruption like unwanted frequencies
    if len(dominant_freqs) > 1:
        print("Potential unwanted noise detected at frequency:", dominant_freqs[1])

    # 4) Check any missing values
    if np.any(np.isnan(input_data)):
        print("Missing values detected in the input data.")
    else:
        print("No missing values.")

### Index 1 ###
from scipy.signal import iirnotch, filtfilt

def solver(input_data, sampling_rate=None):
    # Assuming the siren noise is at index 6, convert this to actual frequency
    siren_freq_index = 6
    siren_freq = (siren_freq_index / len(input_data)) * (sampling_rate / 2)
    
    # Design a notch filter to remove siren frequency
    Q = 30.0  # Quality factor for the notch filter
    notch_b, notch_a = iirnotch(siren_freq, Q, sampling_rate)
    
    # Apply the notch filter to the input_data
    filtered_signal = filtfilt(notch_b, notch_a, input_data)
    
    print("Filtered siren noise from the signal.")
    
    return filtered_signal

### Index 2 ###
### Index 3 ###
