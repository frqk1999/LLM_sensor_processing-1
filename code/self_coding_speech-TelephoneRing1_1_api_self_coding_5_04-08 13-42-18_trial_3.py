### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data has the valid range, is empty, or contains missing values.
    import numpy as np
    
    # Output data should not be empty
    if output_data.size == 0:
        return False
    
    # Check if there are any NaN values in the output data
    if np.any(np.isnan(output_data)):
        return False
    
    # Check if the values fall within a reasonable range (e.g., typical PCM audio range for speech)
    if np.max(output_data) > 32767 or np.min(output_data) < -32768:  # Assuming 16-bit PCM
        return False
    
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    from scipy.signal import periodogram
    
    # Calculate the power spectral density of the input and output signals
    freqs_input, psd_input = periodogram(input_data, fs=sampling_rate)
    freqs_output, psd_output = periodogram(output_data, fs=sampling_rate)

    # Define the bandwidths for speech and identified high-frequency ringing noise
    speech_band = (300, 3400)
    ringing_noise_band = (1900, 2100)  # Bandwidth centered around 2000 Hz for ringing noise
    
    # Calculate power in the ringing noise band to check attenuation
    ringing_noise_power_input = psd_input[(freqs_input >= ringing_noise_band[0]) & (freqs_input <= ringing_noise_band[1])].sum()
    ringing_noise_power_output = psd_output[(freqs_output >= ringing_noise_band[0]) & (freqs_output <= ringing_noise_band[1])].sum()
    
    # Calculate power in the speech band to ensure it's not overly reduced
    speech_power_input = psd_input[(freqs_input >= speech_band[0]) & (freqs_input <= speech_band[1])].sum()
    speech_power_output = psd_output[(freqs_output >= speech_band[0]) & (freqs_output <= speech_band[1])].sum()

    # Calculate the attenuation ratio in the ringing noise band
    ringing_noise_attenuation_ratio = ringing_noise_power_output / ringing_noise_power_input if ringing_noise_power_input != 0 else float('inf')
    
    # Check if ringing noise is appropriately suppressed
    # We expect a significant reduction in ringing noise power otherwise suspect inefficiencies in filtering.
    ringing_noise_suppression_check = ringing_noise_attenuation_ratio < 0.5  # Arbitrary threshold for significant reduction
    
    # Check if the speech band power remains sufficiently intact
    speech_preservation_check = speech_power_output >= 0.7 * speech_power_input  # Retain at least 70% of original speech band power

    return ringing_noise_suppression_check and speech_preservation_check

### Index 2 ###
