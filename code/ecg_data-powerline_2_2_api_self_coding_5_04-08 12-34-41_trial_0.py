### Index 0 ###
import numpy as np
import scipy.signal as signal

def inspection(input_data, sampling_rate=500):
    # 1) Check if the signal is periodic and find the dominant frequency components
    f, Pxx = signal.welch(input_data, fs=sampling_rate)
    peak_indices = np.argsort(Pxx)[-5:]  # Find dominant components
    dominant_frequencies = f[peak_indices]
    
    print("Dominant frequencies in the signal:", dominant_frequencies)
    
    # 2) Check the trend of the signals
    trend = np.mean(input_data)
    print("Mean value of the signal (indicating trend):", trend)
    
    # 3) Check for corruption (unwanted frequency): Focus on powerline noise
    powerline_freq = 50 if sum(dominant_frequencies == 50) > sum(dominant_frequencies == 60) else 60
    if powerline_freq in dominant_frequencies:
        print(f"Powerline noise detected at {powerline_freq} Hz")
    else:
        print("No prominent powerline noise detected")
    
    # 4) Check any missing values
    missing_values = np.isnan(input_data).sum()
    if missing_values > 0:
        print(f"There are {missing_values} missing values in the signal")
    else:
        print("No missing values detected in the signal")

### Index 1 ###
def solver(input_data, sampling_rate=500):
    # Design a notch filter to remove the 60 Hz component
    f0 = 60.0  # Frequency to be removed from signal (in Hz)
    Q = 30.0   # Quality factor
    # Design the notch filter
    b, a = signal.iirnotch(f0, Q, sampling_rate)
    
    # Apply the notch filter to the data
    cleaned_data = signal.filtfilt(b, a, input_data)
    
    return cleaned_data

### Index 2 ###
### Index 3 ###
