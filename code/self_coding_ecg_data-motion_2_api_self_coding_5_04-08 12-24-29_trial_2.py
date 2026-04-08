### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data
    # Check if the output_data contains NaN or infinite values
    if np.isnan(output_data).any() or np.isinf(output_data).any():
        return False
    # Check if the data is within a valid range, considering ECG values typically shouldn't be extremely large.
    if np.min(output_data) < -1e9 or np.max(output_data) > 1e9:
        return False
    return True

### Index 1 ###
from scipy.signal import welch

def challenger(input_data, output_data, sampling_rate=None):
    # Perform spectral analysis to determine power distribution over frequencies
    f_input, Pxx_input = welch(input_data, fs=sampling_rate)
    f_output, Pxx_output = welch(output_data, fs=sampling_rate)    
   
    # Calculate power in low-frequency range (below 0.5 Hz) for both input and output
    low_freq_threshold = 0.5
    input_low_freq_power = Pxx_input[f_input < low_freq_threshold].sum()
    output_low_freq_power = Pxx_output[f_output < low_freq_threshold].sum()

    # Confirm significant reduction (e.g., at least 90%) in low-frequency power from input to output
    if output_low_freq_power < 0.1 * input_low_freq_power:
        return True
    
    return False

### Index 2 ###
