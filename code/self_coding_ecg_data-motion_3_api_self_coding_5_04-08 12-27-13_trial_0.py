### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Step 1: Check if output_data has the valid range
    # In general, ECG signals should not have extreme values (e.g., beyond -5 to 5 mV)

    # Check if the output_data is empty
    if output_data.size == 0:
        return False
    
    # Check for NaN or Inf values
    if np.any(np.isnan(output_data)) or np.any(np.isinf(output_data)):
        return False
    
    # Check for unrealistic ECG range
    if np.min(output_data) < -2.0 or np.max(output_data) > 2.0:
        return False
    
    return True

### Index 1 ###
from scipy.signal import welch

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
    if low_freq_power_output < 0.5 * low_freq_power_input:
        low_freq_reduced = True
    else:
        low_freq_reduced = False

    # Check if there is significant energy retention in the important frequency band (e.g., 0.5-40 Hz for ECG)
    high_freq_power_preserved = np.sum(power_output[(freqs_output >= 0.5) & (freqs_output <= 40)]) > 0.5 * np.sum(power_input[(freqs_input >= 0.5) & (freqs_input <= 40)])

    # Return true if low-frequency artifacts are reduced and important ECG components are preserved
    return low_freq_reduced and high_freq_power_preserved

### Index 2 ###
