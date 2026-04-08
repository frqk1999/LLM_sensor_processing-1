### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    if output_data.size == 0 or np.isnan(output_data).any() or not (np.all(np.isfinite(output_data))):
        return False
    # Assuming valid range is based on the context of ECG signals which typically range from -1mV to 1mV
    # This assumes that the digital values are scaled to actual voltage levels.
    if np.min(output_data) < -10.0 or np.max(output_data) > 10.0:
        return False
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
    
    # Calculate the power ratio
    power_ratio_input = np.sum(power_spec_input[np.argsort(power_spec_input)[-3:]]) / np.sum(power_spec_input)
    power_ratio_output = np.sum(power_spec_output[np.argsort(power_spec_output)[-3:]]) / np.sum(power_spec_output)

    # Validate if dominant frequencies are preserved and noise is reduced.
    # Dominant frequencies should be similar or the same, and output should have a higher power ratio, indicating noise reduction
    if np.allclose(dominant_freqs_input, dominant_freqs_output, atol=0.5) and power_ratio_output > power_ratio_input * 1.5:
        return True
    return False

### Index 2 ###
