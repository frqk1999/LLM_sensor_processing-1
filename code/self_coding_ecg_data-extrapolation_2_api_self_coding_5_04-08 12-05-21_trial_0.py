### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data is valid and has no anomalies
    # 1) Check if the output_data is within valid range, not empty, and does not contain missing values.
    if output_data.size == 0 or np.any(np.isnan(output_data)) or np.any(np.isinf(output_data)):
        return False
    
    # Since it's ECG (Microvolts), check if values are reasonable for such a signal
    if np.min(output_data) < -2000 or np.max(output_data) > 2000:
        return False
    
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    # Check for preservation of periodicity
    fft_values_input = np.fft.fft(input_data)
    frequencies_input = np.fft.fftfreq(len(input_data), d=1.0/sampling_rate)
    magnitude_input = np.abs(fft_values_input)

    fft_values_output = np.fft.fft(output_data)
    frequencies_output = np.fft.fftfreq(len(output_data), d=1.0/sampling_rate)
    magnitude_output = np.abs(fft_values_output)

    dominant_freqs_input = set(frequencies_input[magnitude_input > np.mean(magnitude_input) + 2*np.std(magnitude_input)])
    dominant_freqs_output = set(frequencies_output[magnitude_output > np.mean(magnitude_output) + 2*np.std(magnitude_output)])

    if not (dominant_freqs_input & dominant_freqs_output):
        return False

    # Check if there is a consistent trend in output_data
    output_series = pd.Series(output_data)
    rolling_mean_output = output_series.rolling(window=5).mean()

    if not np.allclose(output_series, rolling_mean_output, atol=0.5):
        return False

    # Check if the magnitude is reasonable
    mean_input, std_input = np.mean(input_data), np.std(input_data)
    if not (mean_input - 3 * std_input <= np.mean(output_data) <= mean_input + 3 * std_input):
        return False

    return True

### Index 2 ###
