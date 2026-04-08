### Index 0 ###
def inspection(input_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import find_peaks
    from scipy.fft import fft
    
    # Check if the signal has missing values
    if np.any(np.isnan(input_data)):
        print("The signal contains missing values.")
    else:
        print("No missing values detected in the signal.")
    
    # Calculate the Fourier Transform to examine frequency components
    frequency_data = fft(input_data)
    magnitude = np.abs(frequency_data)
    frequencies = np.fft.fftfreq(len(magnitude), 1/sampling_rate)
    
    # Identify peaks in the FFT spectrum
    peaks, properties = find_peaks(magnitude, height=0.1*np.max(magnitude))
    dominant_frequencies = frequencies[peaks]
    
    # Find if any dominant frequency is present around 216 Hz (common phone ringing frequency)
    ringing_frequency = 216  # Approximate the ringing frequency
    margin = 5  # Hz margin around the ringing frequency
    
    # Check if the 216 Hz or nearby is a significant component
    unwanted_frequencies = dominant_frequencies[(dominant_frequencies >= ringing_frequency - margin) & 
                                                (dominant_frequencies <= ringing_frequency + margin)]
    
    if unwanted_frequencies.size > 0:
        print(f"Unwanted frequencies detected around {ringing_frequency} Hz: {unwanted_frequencies}")
    else:
        print(f"No significant unwanted frequency component detected around {ringing_frequency} Hz.")
    
    # Identify the trend
    if np.all(input_data == input_data.mean()):
        print("The signal has no trend.")
    else:
        print("The signal has a trend.")
    
    # Analyze periodicity
    if any(dominant_frequencies):  # If there are any dominant frequencies
        # Determine if periodic
        print("The signal contains periodic components.")
        print(f"Dominant frequency components (Hz): {dominant_frequencies}")
    else:
        print("The signal is non-periodic.")

# Note: The Fourier transform output must be limited to non-negative frequencies.

### Index 1 ###
def solver(input_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import iirnotch, lfilter, freqz
    import matplotlib.pyplot as plt
    
    # Target frequency to filter out
    f0 = 216.63  # identified unwanted frequency (phone ringing)
    
    # Quality factor and bandwidth
    Q = 30.0  # Initial Q factor
    
    # Higher Q means narrower bandwidth
    # Design notch filter
    b, a = iirnotch(f0, Q, sampling_rate)
    
    # Apply notch filter
    filtered_signal = lfilter(b, a, input_data)

    # Optional: Check frequency response
    # freq, h = freqz(b, a, fs=sampling_rate)
    # plt.plot(freq, 20 * np.log10(abs(h)))
    # plt.title(\'Notch Filter Frequency Response\')
    # plt.xlabel(\'Frequency (Hz)\')
    # plt.ylabel(\'Amplitude (dB)\')
    # plt.show()
    
    # Verify that 216 Hz component is removed
    freq_data_filtered = np.abs(np.fft.fft(filtered_signal))
    freqs = np.fft.fftfreq(len(freq_data_filtered), d=1/sampling_rate)
    
    unwanted_freq_present = np.any(
        (freqs >= f0 - 1) & (freqs <= f0 + 1) & (freq_data_filtered > 0.1 * np.max(freq_data_filtered))
    )
    
    if not unwanted_freq_present:
        print("Successfully reduced the unwanted frequency component.")
    else:
        print("Unwanted frequency still present. Consider tuning Q factor for more specific attenuation.")
    
    return filtered_signal

### Index 2 ###
### Index 3 ###
