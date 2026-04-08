### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # 1) Check if the output_data has the valid range, is empty, or contains missing values.
    if np.any(np.isnan(output_data)) or len(output_data) == 0:
        return False
    # Assuming speech signal ranges, typically normalized [-1, 1] or as full-scale audio integer types.
    if np.min(output_data) < -32768 or np.max(output_data) > 32767:  # For int16 audio format.
        return False

    # Otherwise, return True as it's within a valid range.
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    from scipy.signal import periodogram
    import numpy as np

    # Compute the power spectrum of the input and output signals
    freqs_input, power_spectrum_input = periodogram(input_data, fs=sampling_rate)
    freqs_output, power_spectrum_output = periodogram(output_data, fs=sampling_rate)

    # Focusing on the known noise frequencies
    noise_frequencies = np.array([141.84, 158.39, 319.15, 330.97, 401.89, 
                                  416.08, 444.44, 449.17, 458.63, 482.27, 
                                  496.45, 517.73, 529.55, 541.37, 557.92, 
                                  576.83, 588.65, 609.93, 624.11, 647.75, 
                                  669.03, 761.23, 895.98, 900.71, 976.36, 1801.42])

    tolerance = 5  # Allowed tolerance in frequency detection

    # Review how well these noise components have been attenuated in the output
    for noise_freq in noise_frequencies:
        # Find nearby frequency index
        indices_input = np.where((freqs_input >= (noise_freq - tolerance)) & 
                                 (freqs_input <= (noise_freq + tolerance)))[0]
        indices_output = np.where((freqs_output >= (noise_freq - tolerance)) & 
                                  (freqs_output <= (noise_freq + tolerance)))[0]

        # If the noise frequencies are reduced, the power spectrum value of output should be significantly less.
        if np.sum(power_spectrum_output[indices_output]) >= np.sum(power_spectrum_input[indices_input]) * 0.5:
            return False

    # If all noise frequencies are sufficiently attenuated, then we're successful.
    return True

### Index 2 ###
