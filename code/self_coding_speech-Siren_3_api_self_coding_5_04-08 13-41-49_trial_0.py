### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data has the valid range, is empty, or contains missing values. 
    if output_data.size == 0:  # Check if output_data is empty
        return False
    if np.any(np.isnan(output_data)):  # Check for missing values in output_data
        return False
    if np.max(output_data) > 32767 or np.min(output_data) < -32768:  # Check if output_data is within valid range for audio sample
        return False
    return True

# Assuming input_data is available from context, checking with given output_data.
inspection_result = inspection(input_data, output_data)

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    from scipy.signal import periodogram

    # Compute the periodogram of the input and output signals
    f_input, Pxx_input = periodogram(input_data, fs=sampling_rate)
    f_output, Pxx_output = periodogram(output_data, fs=sampling_rate)

    # Frequencies identified as siren noise components 
    noise_frequencies = [158.40, 320.61, 729.01, 753.82, 767.18, 
                         782.44, 803.44, 816.79, 832.06, 856.87, 877.86]

    # Check if the power at the noise frequencies has considerably decreased
    for noise_freq in noise_frequencies:
        # Find index of closest frequency in the periodogram
        idx_input = (np.abs(f_input - noise_freq)).argmin()
        idx_output = (np.abs(f_output - noise_freq)).argmin()

        # Compare power levels at this frequency
        if Pxx_output[idx_output] >= 0.5 * Pxx_input[idx_input]:
            return False

    return True

# Run the challenger check with given input_data, output_data, and sampling_rate.
challenge_result = challenger(input_data, output_data, sampling_rate)

### Index 2 ###
