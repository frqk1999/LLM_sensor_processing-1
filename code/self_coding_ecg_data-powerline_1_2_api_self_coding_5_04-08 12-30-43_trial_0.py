### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    if output_data is None or len(output_data) == 0:
        return False
    if np.isnan(output_data).any():
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=500):
    import numpy as np
    from scipy.fft import fft, fftfreq
    
    # Perform Fourier transform to find frequency components in the output data
    n = len(output_data)
    T = 1.0 / sampling_rate
    yf = fft(output_data)
    xf = fftfreq(n, T)[:n//2]
    
    # Identify frequency components in the output data
    filtered_freqs = np.abs(yf[:n//2])
    max_freq_amp_output = np.max(filtered_freqs)
    threshold_output = 0.1 * max_freq_amp_output
    
    # Check for the presence of 50 Hz in the significant frequencies
    significant_freqs_output = xf[filtered_freqs > threshold_output]
    
    # Check if 50 Hz component was significantly reduced or not present in the output signal
    if 50 in significant_freqs_output:
        return False
    return True

### Index 2 ###
