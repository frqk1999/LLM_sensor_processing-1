### Index 0 ###
import numpy as np
from scipy.signal import find_peaks, welch

def inspection(input_data, sampling_rate=None):
    # Check for missing values
    if np.isnan(input_data).any():
        print("Warning: The signal contains missing values.")

    # Compute the Power Spectral Density (PSD)
    freqs, psd = welch(input_data, fs=sampling_rate, nperseg=2048)
    
    # Identify peaks in the frequency spectrum to find dominant frequencies
    peaks, properties = find_peaks(psd, height=np.mean(psd) + 2 * np.std(psd))
    dominant_freqs = freqs[peaks]
    
    print("Dominant Frequency Components Identified in the Signal:", dominant_freqs)
    
    # Check if the signal contains the noise frequencies
    noise_frequencies = [375, 2000]
    
    for nf in noise_frequencies:
        if any(np.isclose(dominant_freqs, nf, atol=5)):
            print(f"Detected noise at approximately {nf} Hz")
        else:
            print(f"No significant noise detected at {nf} Hz")
    
    # Determine if the signal is periodic by checking for major peaks indicative of a fundamental frequency
    if len(dominant_freqs) > 0:
        print("The signal is periodic with key frequency components.")
    else:
        print("The signal is non-periodic.")

    # Detect and inspect the trend: Not typically applicable for audio, trends are for time series like ECG.
    print("Trend analysis not applicable for audio signals.")

### Index 1 ###
from scipy.signal import butter, sosfilt, sosfreqz

def solver(input_data, sampling_rate=None):
    # Design bandstop filters for the identified frequencies
    def bandstop_filter(lowcut, highcut, fs, order=4):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        sos = butter(order, [low, high], btype=\'bandstop\', output=\'sos\')
        return sos

    # Increase bandwidth a little bit for better noise capture
    band_375_hz = bandstop_filter(370, 380, sampling_rate, order=6)
    band_2000_hz = bandstop_filter(1990, 2010, sampling_rate, order=6)

    # Apply filters to the input_data
    filtered_signal = sosfilt(band_375_hz, input_data)
    filtered_signal = sosfilt(band_2000_hz, filtered_signal)

    # Validate effectiveness using Power Spectral Density
    freqs, psd = welch(filtered_signal, fs=sampling_rate, nperseg=2048)
    print("Post-Filtering PSD Analysis: Frequencies with reduced power:", freqs[np.where(psd < np.mean(psd))])

    return filtered_signal

### Index 2 ###
### Index 3 ###
