### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False. 
    # 1) Check if the output_data has the valid range, is empty, or contains missing values. 
    # Args:
    #   input_data: The data type is numpy.ndarray. This is the data provided by the user to perform DSP. 
    #   output_data: The data type is numpy.ndarray. The variable is provided through the function interface for you. This is the data processed by the other AI agent. 
    #   sampling_rate: The sampling rate of the data. sampling_rate is mandatory for speech, ecg, ppg, and gait data. It could be optional for others.
    # Output: boolean variable - True or False. If the result does not pass your test, output False. Else, output True.
    
    # Check if output_data is empty
    if output_data.size == 0:
        return False

    # Check for NaN values
    if np.any(np.isnan(output_data)):
        return False
    
    # Check for valid range
    # In audio processing maxint might be the range based on a type of PCM data used. Here we assume typical 16-bit data range:
    if not np.all((output_data >= -32768) & (output_data <= 32767)):
        return False

    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    from scipy.signal import periodogram
    
    # Calculate the power spectral density of the input and output signals
    freqs_input, psd_input = periodogram(input_data, fs=sampling_rate)
    freqs_output, psd_output = periodogram(output_data, fs=sampling_rate)

    # Define the bandwidths for speech and high-frequency noise (identified during inspection)
    speech_band = (300, 3400)
    noise_band = (1000, np.max(freqs_input))  # Assume noise affects everything > 1000Hz
    
    # Attenuation should occur primarily > 1000Hz based on inspection and filtering design
    # Summarize power in the noise band to check attenuation
    noise_power_input = psd_input[(freqs_input >= noise_band[0]) & (freqs_input <= noise_band[1])].sum()
    noise_power_output = psd_output[(freqs_output >= noise_band[0]) & (freqs_output <= noise_band[1])].sum()
    
    # Ensure the power in the speech band is not overly reduced
    speech_power_input = psd_input[(freqs_input >= speech_band[0]) & (freqs_input <= speech_band[1])].sum()
    speech_power_output = psd_output[(freqs_output >= speech_band[0]) & (freqs_output <= speech_band[1])].sum()

    # Calculate the noise attenuation ratio
    noise_attenuation_ratio = noise_power_output / noise_power_input if noise_power_input != 0 else float('inf')
    
    # Check if noise is appropriately suppressed
    # We expect a significant reduction in noise band power otherwise suspect inefficiencies or incorrect filtering.
    noise_suppression_check = noise_attenuation_ratio < 0.5  # Arbitrary threshold for significant reduction
    
    # Check if speech band power remains sufficiently intact
    speech_preservation_check = speech_power_output >= 0.7 * speech_power_input  # Retain at least 70% power

    return noise_suppression_check and speech_preservation_check

### Index 2 ###
