### Index 0 ###
import numpy as np
from scipy.signal import periodogram, iirnotch

def inspection(input_data, sampling_rate):
    # Check if the signal is periodic and inspect the dominant frequency components
    frequencies, power_spectrum = periodogram(input_data, sampling_rate)

    # Check for the presence of 50 Hz powerline noise
    if 50 in frequencies:
        index_50hz = list(frequencies).index(50)
        power_50hz = power_spectrum[index_50hz]

        # Output evaluation
        print(f"The signal contains a 50 Hz component with power: {power_50hz:.2f}")

    # Check for any trends and missing values
    missing_values = np.isnan(input_data).sum()
    if missing_values > 0:
        print(f"There are {missing_values} missing values in the signal.")
    else:
        print("No missing values detected in the signal.")

    trend = np.polyfit(np.arange(len(input_data)), input_data, 1)
    print(f"The estimated trend of the signal is: slope {trend[0]:.4f}, intercept {trend[1]:.4f}")

    # Check if there is any source of corruption other than the powerline noise
    if np.any(input_data > 1e3) or np.any(input_data < -1e3):
        print("Possible DC offset or other forms of distortion detected.")

inspection(input_data, sampling_rate=500)

### Index 1 ###
from scipy.signal import filtfilt

def solver(input_data, sampling_rate):
    # Design a notch filter to remove 50 Hz noise
    notch_freq = 50  # Frequency to be removed from the signal (Hz)
    quality_factor = 30  # Quality factor of the notch filter
    b, a = iirnotch(notch_freq, quality_factor, sampling_rate)
    
    # Apply the notch filter to the input data
    filtered_data = filtfilt(b, a, input_data)

    # Verification of the filtering by comparing periodograms
    frequencies, power_original = periodogram(input_data, sampling_rate)
    frequencies, power_filtered = periodogram(filtered_data, sampling_rate)

    # Check power reduction at 50 Hz
    if 50 in frequencies:
        index_50hz = list(frequencies).index(50)
        power_50hz_input = power_original[index_50hz]
        power_50hz_output = power_filtered[index_50hz]

        # Ensure reduction in noise power
        if power_50hz_output < 0.1 * power_50hz_input:
            print(f"Successful reduction of 50 Hz noise: input power = {power_50hz_input:.4f}, output power = {power_50hz_output:.4f}")
        else:
            print("Filtering may not have been successful. Noise power at 50 Hz has not reduced adequately.")
    else:
        print("50 Hz frequency component not found in the output, indicating successful removal.")
    
    return filtered_data

# Assuming that the input_data is provided in context with sampling_rate=500 Hz.
filtered_ecg = solver(input_data, sampling_rate=500)

### Index 2 ###
### Index 3 ###
