### Index 0 ###
import numpy as np
import scipy.signal as signal

def inspection(input_data, sampling_rate=500):
    # Check if there are any missing values
    if np.any(np.isnan(input_data)):
        print("The signal contains missing values.")
    else:
        print("No missing values detected in the signal.")
    
    # Check signal periodicity and dominant frequencies
    freqs, psd = signal.welch(input_data, fs=sampling_rate)
    
    # Find dominant frequency components
    dominant_freqs = freqs[np.argsort(psd)[-5:]]  # top 5 frequencies
    print(f"Dominant frequencies in the signal: {dominant_freqs}")
    
    # Check for powerline noise at 50/60 Hz
    powerline_freq = 50 if np.any(np.isclose(dominant_freqs, 50, atol=1.5)) else 60
    if np.any(np.isclose(dominant_freqs, powerline_freq, atol=1.5)):
        print(f"Powerline interference detected at {powerline_freq} Hz.")
    else:
        print("No significant powerline interference detected.")

    # Check trend using a simple mean value
    mean_value = np.mean(input_data)
    print(f"Mean value of the signal: {mean_value}")

    # No output other than the prints in the above checks

# Note: Call this function with the ECG data as input_data and sampling_rate=500.

### Index 1 ###
import numpy as np
import scipy.signal as signal

def solver(input_data, sampling_rate=500):
    # Design a notch filter to remove the 50 Hz powerline noise
    notch_freq = 50  # Frequency to be removed from signal (Hz)
    quality_factor = 30  # Quality factor (higher means sharper notch)
    
    # Design the notch filter
    b, a = signal.iirnotch(notch_freq, quality_factor, sampling_rate)
    
    # Apply the notch filter to the data
    filtered_data = signal.filtfilt(b, a, input_data)
    
    return filtered_data

# Note: Call this function with the ECG data as input_data and sampling_rate=500 to perform the filtering.

### Index 2 ###
### Index 3 ###
