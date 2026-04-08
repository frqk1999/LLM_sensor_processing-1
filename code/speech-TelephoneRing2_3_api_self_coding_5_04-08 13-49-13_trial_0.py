### Index 0 ###
import numpy as np
from scipy.signal import find_peaks
from scipy.fft import fft, fftfreq

def inspection(input_data, sampling_rate=None):
    # Check if the signal length is appropriate
    if input_data is None or len(input_data) == 0:
        print("Input data is empty or None.")
        return
    
    # Check if there are any missing values
    if np.isnan(input_data).any():
        print("Signal contains missing values.")
    else:
        print("No missing values detected in the signal.")
    
    # FFT analysis to find dominant frequencies
    N = len(input_data)
    yf = fft(input_data)
    xf = fftfreq(N, 1 / sampling_rate)[:N // 2]
    
    # Find peaks to identify dominant frequencies
    peaks, _ = find_peaks(np.abs(yf[:N // 2]), height=0)
    dominant_freqs = xf[peaks]
    
    print("Dominant frequency components found at:", dominant_freqs)
    
    # Check periodicity by looking at dominant frequency components
    if len(dominant_freqs) > 0:
        print("The signal is periodic with dominant frequencies.")
    else:
        print("The signal does not appear to have strong periodic components.")
    
    # Detect any potential noise sources (e.g., phone ringing frequency approx 2 kHz)
    ringing_noise_freqs = [freq for freq in dominant_freqs if 1500 <= freq <= 2500]
    
    if ringing_noise_freqs:
        print(f"Potential phone ringing noise detected at frequencies: {ringing_noise_freqs}")
    else:
        print("No potential phone ringing noise detected.")
    
    # Checking trend (Visual inspection would normally be used here)
    trend = np.mean(input_data)
    print(f"Signal trend (mean value): {trend}")

### Index 1 ###
from scipy.signal import iirnotch, lfilter, butter

def solver(input_data, sampling_rate=None):
    # Define the target range for the phone ringing noise
    ringing_freq = 2000  # Example assumption for ringtone frequency
    quality_factor = 30  # Quality factor for the notch filter

    # Design the notch filter
    b_notch, a_notch = iirnotch(ringing_freq, quality_factor, sampling_rate)

    # Apply the notch filter to remove the noise
    filtered_signal = lfilter(b_notch, a_notch, input_data)

    # Design a band-pass filter for speech (accepts human speech ranges)
    lowcut = 85  # Lower cut-off frequency for male voice
    highcut = 3000  # Conservatively allow for high harmonics 
    order = 6  # Filter order

    # Create butterworth band-pass filter
    b_band, a_band = butter(order, [lowcut, highcut], fs=sampling_rate, btype='band')

    # Apply the speech band-pass filter
    speech_enhanced_signal = lfilter(b_band, a_band, filtered_signal)

    return speech_enhanced_signal

### Index 2 ###
### Index 3 ###
