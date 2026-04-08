### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data for any issues such as invalid range, emptiness or missing values.
    
    # Check if the output_data is empty
    if not output_data.size:
        return False
    
    # Check for any NaN values in the output_data
    if np.isnan(output_data).any():
        return False
    
    # Check if the output_data is within a reasonable range
    # ECG signal values typically range between -2mV to 2mV. We need to make sure all values are within this range.
    if not (-2.0 <= output_data).all() or not (output_data <= 2.0).all():
        return False
    
    return True

### Index 1 ###
from scipy.signal import welch

def challenger(input_data, output_data, sampling_rate=None):
    # 1. Compute the power spectral density (PSD) of both input and output data using Welch's method.
    f_input, Pxx_input = welch(input_data, fs=sampling_rate)
    f_output, Pxx_output = welch(output_data, fs=sampling_rate)

    # 2. Check the power in the low-frequency range (below 0.5 Hz) for both input and output.
    low_freq_threshold = 0.5
    input_low_freq_power = Pxx_input[f_input < low_freq_threshold].sum()
    output_low_freq_power = Pxx_output[f_output < low_freq_threshold].sum()

    # 3. Ensure that the power in the low-frequency range is significantly reduced in the output.
    if output_low_freq_power < 0.1 * input_low_freq_power:  # Expecting at least 90% reduction
        return True
    
    return False

### Index 2 ###
