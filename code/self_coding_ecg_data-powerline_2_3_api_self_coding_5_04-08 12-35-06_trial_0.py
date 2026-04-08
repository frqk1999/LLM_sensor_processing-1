### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # 1) Check if the output_data has the valid range, is empty, or contains missing values.
    if output_data is None or len(output_data) == 0:
        return False
    if np.isnan(output_data).any():
        return False
    # Additional check to ensure range of values is realistically bounded for ECG signals
    if np.min(output_data) < -5 or np.max(output_data) > 5:
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    # Compare the frequency spectrum of input and output to verify that the 60 Hz component is attenuated
    from scipy.signal import periodogram

    # Calculate power spectral densities
    freqs_in, power_in = periodogram(input_data, fs=sampling_rate)
    freqs_out, power_out = periodogram(output_data, fs=sampling_rate)

    # Find the power of the 60 Hz component in input and output
    idx_in = np.where((freqs_in >= 59) & (freqs_in <= 61))
    idx_out = np.where((freqs_out >= 59) & (freqs_out <= 61))

    power_60hz_in = np.sum(power_in[idx_in])
    power_60hz_out = np.sum(power_out[idx_out])

    # Verify if 60 Hz component is attenuated in the output
    # and overall power level is not drastically reduced
    if power_60hz_out < power_60hz_in * 0.1 and np.sum(power_out) > np.sum(power_in) * 0.5:
        return True
    else:
        return False

### Index 2 ###
