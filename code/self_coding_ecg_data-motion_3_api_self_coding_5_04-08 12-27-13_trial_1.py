### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if output_data is empty or contains NaN
    if output_data.size == 0 or np.isnan(output_data).any():
        return False
    # Check if any value is excessively large, which might point to instability
    if np.max(np.abs(output_data)) > 10**4:
        return False
    return True

# The function checks if the output data is non-empty, does not contain NaN, and has no excessively large values.

### Index 1 ###
from scipy.signal import welch
import numpy as np

def challenger(input_data, output_data, sampling_rate=500):
    # Analyze the power spectral density (PSD) of both input and output data to verify filtering

    # Compute power spectra for input and output signals
    freqs_input, power_input = welch(input_data, fs=sampling_rate)
    freqs_output, power_output = welch(output_data, fs=sampling_rate)

    # Compare power in low frequency bands (< 0.5 Hz) before and after filtering
    low_freq_power_input = np.sum(power_input[freqs_input < 0.5])
    low_freq_power_output = np.sum(power_output[freqs_output < 0.5])

    # Determine the effectiveness of the high-pass filter
    # Good filtering should significantly reduce low-frequency power
    low_freq_reduced = low_freq_power_output < 0.5 * low_freq_power_input

    # Check if there is significant energy retention in the important frequency band (e.g., 0.5-40 Hz for ECG)
    high_freq_power_preserved = np.sum(power_output[(freqs_output >= 0.5) & (freqs_output <= 40)]) > 0.5 * np.sum(power_input[(freqs_input >= 0.5) & (freqs_input <= 40)])

    # Return true if low-frequency artifacts are reduced and important ECG components are preserved
    return low_freq_reduced and high_freq_power_preserved

### Index 2 ###
