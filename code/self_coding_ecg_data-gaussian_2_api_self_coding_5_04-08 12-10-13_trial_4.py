### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False.
    # Check if the output_data has the valid range, is empty, or contains missing values.
    
    # Check if output_data is empty
    if len(output_data) == 0:
        return False
    
    # Check for missing values in output_data
    if np.any(np.isnan(output_data)):
        return False
    
    # Check if the output_data has valid range (Consider typical ECG values range)
    if np.min(output_data) < -5 or np.max(output_data) > 5:  # ECG values outside this range may indicate error
        return False
    
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate):
    import numpy as np
    from scipy.signal import welch, find_peaks
    
    # Frequency-domain analysis
    freqs_input, power_spec_input = welch(input_data, fs=sampling_rate, nperseg=1024)
    freqs_output, power_spec_output = welch(output_data, fs=sampling_rate, nperseg=1024)
    
    # Find dominant frequency components
    dominant_freqs_input = freqs_input[np.argsort(power_spec_input)[-3:]]
    dominant_freqs_output = freqs_output[np.argsort(power_spec_output)[-3:]]
    
    # Calculate power ratio
    power_ratio_input = np.sum(power_spec_input[np.argsort(power_spec_input)[-3:]]) / np.sum(power_spec_input)
    power_ratio_output = np.sum(power_spec_output[np.argsort(power_spec_output)[-3:]]) / np.sum(power_spec_output)
    
    # Time-domain analysis: Check for PQRST preservation through peak detection
    peaks_input, _ = find_peaks(input_data, distance=sampling_rate//2)  # Assume at least 1s between heartbeats
    peaks_output, _ = find_peaks(output_data, distance=sampling_rate//2)
    
    # Validate if dominant frequencies are preserved, noise is reduced, and peaks are consistent
    if (np.allclose(dominant_freqs_input, dominant_freqs_output, atol=0.5) and
        power_ratio_output > power_ratio_input * 1.2 and  # Check for at least 20% improvement in power ratio
        len(peaks_input) == len(peaks_output)):  # Check consistency in detected peaks
        return True
    return False

### Index 2 ###
