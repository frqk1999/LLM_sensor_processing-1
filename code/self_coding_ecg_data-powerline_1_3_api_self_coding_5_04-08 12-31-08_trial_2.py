### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data has the valid range, is empty, or contains missing values.
    if output_data is None or len(output_data) == 0:
        return False

    # Check for missing values
    if np.any(np.isnan(output_data)):
        return False
    
    # Check for infinite values
    if np.any(np.isinf(output_data)):
        return False

    # (Optional) Typically for values in physiological signals, we check if values are within a humanly possible range.
    # However, without knowing the signal amplitude range, we skip amplitude checks.

    return True

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
