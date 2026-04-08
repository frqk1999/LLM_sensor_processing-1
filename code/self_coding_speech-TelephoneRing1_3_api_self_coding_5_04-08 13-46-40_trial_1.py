### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False.
    # 1) Check if the output_data has the valid range, is empty, or contains missing values.
    if output_data.size == 0 or np.isnan(output_data).any() or not np.isfinite(output_data).all():
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import periodogram
    
    # Calculate power spectral density (PSD) of the input and output signals
    freqs_input, power_input = periodogram(input_data, fs=sampling_rate)
    freqs_output, power_output = periodogram(output_data, fs=sampling_rate)
    
    # Unwanted frequencies identified from initial inspection that need attenuation
    ringing_frequencies = [
        308.62, 310.62, 312.63, 314.63, 316.63,
        320.64, 322.65, 326.65, 328.66, 330.66,
        450.90, 452.91, 462.93, 1963.93, 2042.08
    ]
    
    # Check if the ringing noise frequencies have been attenuated
    for freq in ringing_frequencies:
        idx_input = (np.abs(freqs_input - freq)).argmin()
        idx_output = (np.abs(freqs_output - freq)).argmin()
        
        # More aggressive attenuation target: ensure significant reduction
        if power_output[idx_output] > power_input[idx_input] * 0.05:
            return False

    # Check maintained integrity of typical speech frequency range
    speech_freq_lower, speech_freq_upper = 85, 255
    speech_power_input = np.sum(power_input[(freqs_input >= speech_freq_lower) & (freqs_input <= speech_freq_upper)])
    speech_power_output = np.sum(power_output[(freqs_output >= speech_freq_lower) & (freqs_output <= speech_freq_upper)])
    
    # Ensure speech frequencies are intact by checking output power is at least a fraction of input power
    if speech_power_output < 0.6 * speech_power_input:
        return False

    return True

### Index 2 ###
