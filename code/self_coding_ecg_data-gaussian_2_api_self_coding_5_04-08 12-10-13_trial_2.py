### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False.
    # Check if the output_data has the valid range, is empty, or contains missing values.
    
    # Check if output_data is empty or contains NaN values
    if len(output_data) == 0 or np.isnan(output_data).any():
        return False
    
    # Optional: Validate the range of output_data for ECG signals, which are typically within a few millivolts.
    # As we are focusing on the absence of NaNs and data length currently, this check is commented out.
    # if not (np.min(output_data) >= -5 and np.max(output_data) <= 5):
    #     return False

    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate):
    import numpy as np
    from scipy.signal import welch

    # Calculate the power spectral density of input and output data
    freqs_input, power_spec_input = welch(input_data, fs=sampling_rate, nperseg=1024)
    freqs_output, power_spec_output = welch(output_data, fs=sampling_rate, nperseg=1024)
    
    # Find dominant frequency components
    dominant_freqs_input = freqs_input[np.argsort(power_spec_input)[-3:]]
    dominant_freqs_output = freqs_output[np.argsort(power_spec_output)[-3:]]
    
    # Calculate power ratio
    power_ratio_input = np.sum(power_spec_input[np.argsort(power_spec_input)[-3:]]) / np.sum(power_spec_input)
    power_ratio_output = np.sum(power_spec_output[np.argsort(power_spec_output)[-3:]]) / np.sum(power_spec_output)

    # Validate if dominant frequencies are preserved and noise is reduced.
    # Dominant frequencies should be similar or the same and output should have higher power ratio, indicating noise reduction
    if np.allclose(dominant_freqs_input, dominant_freqs_output, rtol=0.1) and power_ratio_output > power_ratio_input * 1.5:
        return True
    return False

### Index 2 ###
