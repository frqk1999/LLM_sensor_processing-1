### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False. 
    # Check if the output_data has the valid range, is empty, or contains missing values.
    
    # Check if the output_data is empty
    if output_data.size == 0:
        return False
    
    # Check for missing values in output_data
    if np.any(np.isnan(output_data)):
        return False
    
    # Assuming the signal has a dynamic range typical for audio, check if values exceed expected range
    if np.min(output_data) < -32768 or np.max(output_data) > 32767:
        return False
    
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    from scipy.fft import fft, fftfreq
    
    # Check if sampling rate is given
    if sampling_rate is None:
        return False
    
    # Frequency analysis of the output_data
    N = len(output_data)
    T = 1.0 / sampling_rate
    
    yf_input = fft(input_data)
    yf_output = fft(output_data)
    xf = fftfreq(N, T)[:N//2]
    
    # Define the noise frequency range (700-1400 Hz) to check for attenuation
    phone_ring_freq_range = (700, 1400)
    
    # Check amplitude reduction in the phone ringing frequency range
    noise_freqs = (xf >= phone_ring_freq_range[0]) & (xf <= phone_ring_freq_range[1])
    
    # Calculate mean amplitude in the noise frequency range for both input and output
    input_noise_mean = np.mean(np.abs(yf_input[:N//2][noise_freqs]))
    output_noise_mean = np.mean(np.abs(yf_output[:N//2][noise_freqs]))
    
    # A significant reduction in mean amplitude suggests effective noise attenuation
    # Consider a reduction threshold, e.g., 50% reduction
    if output_noise_mean < 0.5 * input_noise_mean:
        return True
    else:
        return False

### Index 2 ###
