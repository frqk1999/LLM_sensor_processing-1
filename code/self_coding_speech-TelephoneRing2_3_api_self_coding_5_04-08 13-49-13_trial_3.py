### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False.
    # 1) Check if the output_data has the valid range, is empty, or contains missing values.
    # Args:
    #   input_data: The data type is numpy.ndarray. This is the data provided by the user to perform DSP. 
    #   output_data: The data type is numpy.ndarray. The variable is provided through the function interface for you. This is the data processed by the other AI agent. 
    #   sampling_rate: The sampling rate of the data. sampling_rate is mandatory for speech, ecg, ppg, and gait data. It could be optional for others.
    # Output: boolean variable - True or False. If the result does not pass your test, output False. Else, output True.
    import numpy as np

    # Check if output_data is empty
    if len(output_data) == 0:
        return False
    
    # Check for NaN values
    if np.any(np.isnan(output_data)):
        return False

    # Check for values out of typical audio range (e.g., excessive amplitude suggesting overflow)
    if np.max(output_data) > 32767 or np.min(output_data) < -32768:
        return False
    
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    # Perform FFT analysis on the input and output data to find frequency components
    input_fft = np.abs(np.fft.fft(input_data))
    output_fft = np.abs(np.fft.fft(output_data))
    
    freqs = np.fft.fftfreq(len(input_data), 1/sampling_rate)
    
    # Define the target range for the phone ringing noise (for analysis purposes)
    ringing_freq_range = (100, 400)  # Updated based on notch freq in solution
    speech_freq_range = (250, 3000)
    
    # Check attenuation in ringing frequency range
    ringing_indices = np.where((freqs >= ringing_freq_range[0]) & (freqs <= ringing_freq_range[1]))
    ring_input_power = np.sum(input_fft[ringing_indices] ** 2)
    ring_output_power = np.sum(output_fft[ringing_indices] ** 2)
    ringing_attenuated = ring_output_power < ring_input_power * 0.1  # Expect significant attenuation
    
    # Check preservation/enhancement in speech frequency range
    speech_indices = np.where((freqs >= speech_freq_range[0]) & (freqs <= speech_freq_range[1]))
    speech_input_power = np.sum(input_fft[speech_indices] ** 2)
    speech_output_power = np.sum(output_fft[speech_indices] ** 2)
    speech_preserved = speech_output_power >= speech_input_power * 0.9  # Expect preservation or slight enhancement
    
    return ringing_attenuated and speech_preserved

### Index 2 ###
