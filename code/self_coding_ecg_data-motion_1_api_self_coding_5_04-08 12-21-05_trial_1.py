### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    if not output_data.size:  # Check if output_data is empty
        return False
    if np.isnan(output_data).any():  # Check if there are any NaN values
        return False
    # Assuming ECG magnitude ranges are relatively small
    if not (-1.5 <= output_data).all() and (output_data <= 1.5).all(): 
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import welch

    # Calculate Welch power spectral density estimate for input data
    f_input, Pxx_input = welch(input_data, fs=sampling_rate)
    # Calculate Welch power spectral density estimate for output data
    f_output, Pxx_output = welch(output_data, fs=sampling_rate)

    # Determine the dominant low-frequency components in the input data
    dominant_low_freqs_input = f_input[np.argsort(Pxx_input)[:3]]

    # Determine the dominant low-frequency components in the output data
    dominant_low_freqs_output = f_output[np.argsort(Pxx_output)[:3]]

    # Check if the dominant low-frequency components are attenuated in the output
    low_freq_attenuation_check = all(freq_in > freq_out for freq_in, freq_out in zip(dominant_low_freqs_input, dominant_low_freqs_output))

    # Check if the main ECG features (e.g., QRS complexes) are preserved
    # Sum power spectral density in the QRS band (5-15 Hz) for both input and output
    qrs_band_input = np.sum(Pxx_input[(f_input >= 5) & (f_input <= 15)])
    qrs_band_output = np.sum(Pxx_output[(f_output >= 5) & (f_output <= 15)])

    # Check substantial retention of QRS complex
    qrs_preservation_check = qrs_band_output > 0.7 * qrs_band_input

    # Return True if both checks pass
    return low_freq_attenuation_check and qrs_preservation_check

### Index 2 ###
