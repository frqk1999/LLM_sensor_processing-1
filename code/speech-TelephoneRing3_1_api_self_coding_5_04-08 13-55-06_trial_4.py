### Index 0 ###
def inspection(input_data, sampling_rate):
    import numpy as np
    from scipy.signal import find_peaks
    from scipy.fft import fft, fftfreq

    # Calculate the Fast Fourier Transform (FFT) to get the frequency domain representation
    yf = fft(input_data)
    xf = fftfreq(len(input_data), 1 / sampling_rate)

    # Use power spectral density to find dominant frequencies
    power_spectral_density = np.abs(yf)**2

    # Find peaks in the power spectral density to identify dominant frequencies
    peaks, _ = find_peaks(power_spectral_density, height=0)

    # Sort peaks by prominence (height)
    sorted_indices = np.argsort(-power_spectral_density[peaks])
    dominant_freqs = xf[peaks][sorted_indices][:5]  # Top 5 dominant frequencies

    print("Dominant Frequencies (Hz):", dominant_freqs)

    # Check periodicity (if only a few distinct frequencies are found, it\'s periodic)
    if len(dominant_freqs) <= 3:
        print("The signal is periodic.")
    else:
        print("The signal is mostly non-periodic, indicating presence of multiple sources.")

    # Identify any unusual frequency spikes that could indicate phone ringing
    # Phone ring frequencies are typically in the range of 400Hz - 4kHz
    unusual_freqs = [f for f in dominant_freqs if 400 < abs(f) < 4000]
    print("Potential Noise Frequencies (Hz):", unusual_freqs)

    # Check if there are NaNs or missing values
    if np.any(np.isnan(input_data)):
        print("There are missing values in the signal.")
    else:
        print("No missing values in the signal.")

    # Check trend of the signal: Mean value inspection
    trend = np.mean(input_data)
    print("Signal trend (mean):", trend)

### Index 1 ###
def solver(input_data, sampling_rate):
    import numpy as np
    from scipy.signal import butter, lfilter, wiener

    # Butterworth Bandstop filter design to remove phone ringing noise
    def butter_bandstop(lowcut, highcut, fs, order=4):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='bandstop')
        return b, a

    def bandstop_filter(data, lowcut, highcut, fs, order=4):
        b, a = butter_bandstop(lowcut, highcut, fs, order=order)
        y = lfilter(b, a, data)
        return y

    # Define parameters based on identified noise frequencies
    lowcut1 = 545  # Just below the noise frequency
    highcut1 = 575 # Just above the noise frequency

    # Apply bandstop filter to remove the identified noise frequencies
    filtered_data_1 = bandstop_filter(input_data, lowcut1, highcut1, sampling_rate)

    # Apply Wiener filter for additional smoothing and noise reduction
    processed_data = wiener(filtered_data_1)

    return processed_data

### Index 2 ###
### Index 3 ###
