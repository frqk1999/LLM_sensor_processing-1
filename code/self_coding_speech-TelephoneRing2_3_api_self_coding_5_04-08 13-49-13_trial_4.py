### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    if output_data is None or len(output_data) == 0:
        return False
    # Check if output_data contains any NaN values
    if np.any(np.isnan(output_data)):
        return False
    # Check if the data falls within a reasonable range, assuming audio signals
    if np.min(output_data) < -32768 or np.max(output_data) > 32767:
        return False
    # If all checks pass
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
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
