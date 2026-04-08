### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False.

    # Check if the output_data is not empty and does not contain NaN or infinite values
    if output_data.size == 0 or np.any(np.isnan(output_data)) or np.any(np.isinf(output_data)):
        return False
    
    # Check if the output_data range is reasonable (not extreme values)
    if np.max(output_data) > 10**3 or np.min(output_data) < -10**3:  # Example range check
        return False

    return True

# Assume the inspection function returns True, as output_data values seem reasonable.

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=500):
    import numpy as np
    from scipy.signal import periodogram
    
    # Compute periodogram of the input and output signals
    freqs_input, power_input = periodogram(input_data, fs=sampling_rate)
    freqs_output, power_output = periodogram(output_data, fs=sampling_rate)
    
    # Find frequency components close to 50 Hz in both input and output
    mask_50hz_input = np.isclose(freqs_input, 50, atol=1)
    mask_50hz_output = np.isclose(freqs_output, 50, atol=1)

    # Retrieve power values at 50 Hz
    power_50hz_input = power_input[mask_50hz_input]
    power_50hz_output = power_output[mask_50hz_output]

    # Assure that 50 Hz component is significantly reduced
    if power_50hz_input.size > 0 and power_50hz_output.size > 0:
        # Check if the power of the 50 Hz component in the output is less than 10% of the input's
        if np.all(power_50hz_output < 0.1 * power_50hz_input):
            return True
        else:
            return False

    return False

### Index 2 ###
