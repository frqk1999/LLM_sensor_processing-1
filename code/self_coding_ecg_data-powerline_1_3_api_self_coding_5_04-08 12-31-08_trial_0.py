### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if output_data has valid range, is not empty, and has no NaN values.
    if output_data is None or len(output_data) == 0:
        return False
    if np.any(np.isnan(output_data)):
        return False
    return True

# Assume input_data and output_data provided during function call execution.

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=500):
    import numpy as np
    from scipy.signal import periodogram
    
    # Compute periodogram of the input and output signals
    freqs_input, power_input = periodogram(input_data, fs=sampling_rate)
    freqs_output, power_output = periodogram(output_data, fs=sampling_rate)
    
    # Find frequency components close to 50 Hz in both input and output
    is_50hz_present_input = np.isclose(freqs_input, 50, atol=1).any()
    is_50hz_present_output = np.isclose(freqs_output, 50, atol=1).any()

    # Check for power reduction at 50 Hz
    power_50hz_input = power_input[np.isclose(freqs_input, 50, atol=1)]
    power_50hz_output = power_output[np.isclose(freqs_output, 50, atol=1)]

    # Assure that 50 Hz component is significantly reduced
    if is_50hz_present_input and is_50hz_present_output:
        if power_50hz_output < 0.1 * power_50hz_input:
            return True
        else:
            return False
    return False

### Index 2 ###
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
        if np.all(power_50hz_output < 0.1 * power_50hz_input):
            return True
        else:
            return False
    return False

### Index 3 ###
