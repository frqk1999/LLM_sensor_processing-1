### Index 0 ###
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks

def inspection(input_data, sampling_rate=None):
    if input_data is None or sampling_rate is None:
        print("Input data or sampling rate not provided.")
        return

    # Length of the signal
    n = len(input_data)

    # Calculate Fourier Transform
    yf = fft(input_data)
    xf = fftfreq(n, 1 / sampling_rate)

    # Get amplitude spectrum
    amplitude_spectrum = np.abs(yf)

    # Find dominant frequencies using peak finding
    prominence = 0.1 * np.max(amplitude_spectrum)  # define prominence
    peaks, _ = find_peaks(amplitude_spectrum, prominence=prominence)
    dominant_freqs = xf[peaks]

    # Check periodicity
    is_periodic = len(dominant_freqs) > 0

    # Check for any missing values
    missing_values = np.isnan(input_data).any()

    # Print Inspection results
    print("Signal Analysis:")
    print(f"Signal Length: {n} samples")
    print(f"Found dominant frequencies: {dominant_freqs}")
    print(f"Is the signal periodic? {\'Yes\' if is_periodic else \'No\'}")
    print(f"Missing values: {missing_values}")

    # Check trends by analyzing the first few dominant frequencies
    if is_periodic:
        print("Potential siren frequency components are at:")
        for freq in dominant_freqs:
            print(f"{freq} Hz")

    print("Inspection completed.")

### Index 1 ###
import numpy as np
from scipy.signal import iirnotch, filtfilt

def solver(input_data, sampling_rate=None):
    # Design notch filters for siren frequencies observed in the inspection
    def apply_notch_filter(data, fs):
        # Frequencies to target based on inspection results
        siren_frequencies = [110, 118, 206, 217, 223, 228, 234]
        filtered_data = data.copy()
        
        for freq in siren_frequencies:
            notch_freq = freq / (fs / 2)  # Normalizing the frequency
            b, a = iirnotch(notch_freq, Q=30)  # Design notch filter
            filtered_data = filtfilt(b, a, filtered_data)  # Apply filter to data
            
        return filtered_data

    if input_data is None or sampling_rate is None:
        raise ValueError("Input data or sampling rate not provided.")

    # Perform filtering
    filtered_audio = apply_notch_filter(input_data, sampling_rate)

    # Return the filtered audio data
    return filtered_audio

### Index 2 ###
### Index 3 ###
