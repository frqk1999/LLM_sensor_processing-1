### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if output_data is empty or contains missing values
    if output_data.size == 0 or np.any(np.isnan(output_data)):
        return False
    
    # Further checks for valid range can be based on specifics such as ECG signal characteristics
    # For ECG signals, overshoots or extremely large deviations could be unrealistic
    if np.min(output_data) < -5 or np.max(output_data) > 5:  # Arbitrary chosen ECG voltage range
        return False
    
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    from scipy.signal import welch
    
    # Input dominant low-frequency detection
    f_input, Pxx_input = welch(input_data, fs=sampling_rate)
    dominant_freqs_input = f_input[np.argsort(Pxx_input)[:3]]  # Low-frequency focus
    
    # Output dominant low-frequency detection
    f_output, Pxx_output = welch(output_data, fs=sampling_rate)
    dominant_freqs_output = f_output[np.argsort(Pxx_output)[:3]]  # Low-frequency focus
    
    # Check if low frequencies are attenuated
    attenuation_check = all(freq_in > freq_out for freq_in, freq_out in zip(dominant_freqs_input, dominant_freqs_output))
    
    # Check if main ECG features (QRS complex) exist after filtering
    # For simplicity, assume that the main ECG component, e.g., QRS, is in a specific frequency range (e.g., 5-15 Hz)
    qrs_band_in = np.sum(Pxx_input[(f_input >= 5) & (f_input <= 15)])
    qrs_band_out = np.sum(Pxx_output[(f_output >= 5) & (f_output <= 15)])
    
    feature_preservation_check = qrs_band_out > 0.7 * qrs_band_in  # Ensuring substantial retention
    
    return attenuation_check and feature_preservation_check

### Index 2 ###
