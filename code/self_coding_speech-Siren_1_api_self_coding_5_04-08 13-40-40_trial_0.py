### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if output_data is within a valid range and has no missing values or is empty.
    if output_data is None or len(output_data) == 0:
        return False
    if np.isnan(output_data).any():
        return False
    return True

### Index 1 ###
import numpy as np
from scipy.fft import fft, fftfreq

def challenger(input_data, output_data, sampling_rate=None):
    # Calculate frequency spectrum of both input and output to compare and check if siren frequencies are attenuated.

    # Calculate Fourier Transform of input and output
    n = len(input_data)
    yf_input = fft(input_data)
    yf_output = fft(output_data)
    xf = fftfreq(n, 1 / sampling_rate)

    # Get amplitude spectrum
    amplitude_input = np.abs(yf_input)
    amplitude_output = np.abs(yf_output)

    # Frequencies identified as siren - they should be attenuated
    siren_frequencies = [110, 118, 206, 217, 223, 228, 234]

    # Checking attenuation at siren frequencies
    siren_att_indices = [np.argmin(np.abs(xf - freq)) for freq in siren_frequencies]
    for idx in siren_att_indices:
        # Ensure output frequencies are significantly lower than input at those frequencies
        if amplitude_output[idx] >= 0.5 * amplitude_input[idx]:
            return False

    # Optionally ensure speech-related frequencies, if known, remain unaltered
    # Here, let's assume speech frequencies (in human range 300-3400 Hz) should have minimal attenuation
    speech_freq_range = (300, 3400)
    speech_indices = (xf >= speech_freq_range[0]) & (xf <= speech_freq_range[1])
    if not np.all(amplitude_output[speech_indices] >= 0.8 * amplitude_input[speech_indices]):
        return False

    return True

### Index 2 ###
