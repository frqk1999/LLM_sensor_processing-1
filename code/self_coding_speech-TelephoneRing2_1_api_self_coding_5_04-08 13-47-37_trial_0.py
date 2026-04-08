### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data array is empty or contains NaN values
    if output_data.size == 0:
        return False
    if np.isnan(output_data).any():
        return False
    # Assuming the output_data should range similarly like input_data
    if np.min(output_data) < -32768 or np.max(output_data) > 32767:
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import periodogram

    # Analyze the power spectral density of both input and output signals
    freqs_input, power_input = periodogram(input_data, fs=sampling_rate)
    freqs_output, power_output = periodogram(output_data, fs=sampling_rate)

    # Find the power of the signal at the 216 Hz frequency
    mask_216Hz_input = np.isclose(freqs_input, 216, atol=1)
    mask_216Hz_output = np.isclose(freqs_output, 216, atol=1)

    # Calculate power for 216 Hz frequency
    power_at_216Hz_input = power_input[mask_216Hz_input]
    power_at_216Hz_output = power_output[mask_216Hz_output]

    # Check if the power at the frequency is substantially reduced
    if len(power_at_216Hz_output) > 0 and len(power_at_216Hz_input) > 0:
        if power_at_216Hz_output[0] < power_at_216Hz_input[0] * 0.1:  # Checking for 90% reduction
            return True
    return False

### Index 2 ###
