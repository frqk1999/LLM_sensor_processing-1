### Index 0 ###
import numpy as np
from scipy.signal import welch

def inspection(input_data, sampling_rate=None):
    if sampling_rate is None:
        raise ValueError("Sampling rate must be provided for ECG data.")

    print("Starting ECG signal inspection...")
    
    # Check for periodicity and dominant frequencies
    freqs, psd = welch(input_data, fs=sampling_rate, nperseg=2048)  # Use Welch\'s method for PSD
    # Dominant frequency related to baseline drift detection
    dominant_freq_index = np.argmax(psd[:int(1.5/sampling_rate*len(freqs))])  # Looking up to 1.5Hz
    dominant_freq = freqs[dominant_freq_index]

    print(f"Dominant frequency detected up to 1.5 Hz: {dominant_freq:.2f} Hz")
    
    # Check trend (e.g., using np.diff or rolling average if in pandas)
    trend_direction = np.mean(np.gradient(input_data))
    if trend_direction > 0:
        print("Signal has upward trend.")
    elif trend_direction < 0:
        print("Signal has downward trend.")
    else:
        print("Signal has no trend.")
    
    # Check for noise/corruption in specific bands
    unwanted_freq_band = (50, 60)  # Example: Powerline noise
    powerline_noise = np.any((freqs >= unwanted_freq_band[0]) & (freqs <= unwanted_freq_band[1]) & (psd > np.mean(psd)/5))
    if powerline_noise:
        print(f"Potential unwanted noise detected in the frequency range {unwanted_freq_band[0]}-{unwanted_freq_band[1]} Hz.")
    
    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("Missing values detected in the input data.")
    else:
        print("No missing values found in the input data.")
    
    print("Inspection completed.")

### Index 1 ###
from scipy.signal import butter, filtfilt

def solver(input_data, sampling_rate=None):
    if sampling_rate is None:
        raise ValueError("Sampling rate must be provided for ECG data.")

    # High-pass filter design parameters
    cutoff_freq = 0.3  # Cutoff frequency slightly above the detected dominant frequency
    filter_order = 5  # Relatively high order to improve filtering

    # Design the Butterworth high-pass filter
    b, a = butter(N=filter_order, Wn=cutoff_freq/(0.5*sampling_rate), btype=\'highpass\')

    # Apply the filter to the ECG signal
    filtered_signal = filtfilt(b, a, input_data)

    return filtered_signal

### Index 2 ###
### Index 3 ###
