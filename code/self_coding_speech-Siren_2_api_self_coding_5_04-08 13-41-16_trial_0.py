### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False.
    # 1) Check if the output_data has the valid range, is empty, or contains missing values.
    # 2) Do NOT check the data type - using the isinstance or np.isscalar function is not reliable.
    
    # Check if output_data is empty
    if output_data.size == 0:
        return False
        
    # Check if there are any missing (NaN) values in output_data
    if np.any(np.isnan(output_data)):
        return False

    return True

### Index 1 ###
from scipy.signal import welch

def challenger(input_data, output_data, sampling_rate=None):
    # Compute the power spectral density of both input and output data
    _, power_spectrum_input = welch(input_data, fs=sampling_rate)
    _, power_spectrum_output = welch(output_data, fs=sampling_rate)
    
    # Identify the dominant frequencies in both input and output data
    dominant_freqs_input = np.argsort(power_spectrum_input)[::-1][:2]
    dominant_freqs_output = np.argsort(power_spectrum_output)[::-1][:2]
    
    # Assess if the siren noise frequency is attenuated in the output data
    # Assuming the siren was the second most significant component in input
    siren_index_in_input = dominant_freqs_input[1]
    siren_power_in_output = power_spectrum_output[siren_index_in_input]
    siren_power_in_input = power_spectrum_input[siren_index_in_input]
    
    # Check conditions for successful noise attenuation
    # Siren frequency should have reduced power in the output compared to input
    if siren_power_in_output < siren_power_in_input:
        return True
    else:
        return False

### Index 2 ###
