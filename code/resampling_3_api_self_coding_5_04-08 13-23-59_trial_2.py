### Index 0 ###
import numpy as np
from scipy.signal import firwin, lfilter, welch

def inspection(input_data, sampling_rate=None):
    # Preliminary check for high-frequency components
    nyquist_rate = sampling_rate / 2
    cutoff = 25
    filter_order = 100
    
    # Filter the signal to ensure attenuation of frequencies above the cutoff
    fir_coeff = firwin(filter_order, cutoff / nyquist_rate)
    filtered_data = lfilter(fir_coeff, 1.0, input_data)
    
    # Compute the PSD using Welch\'s method
    freq_original, psd_original = welch(input_data, fs=sampling_rate, nperseg=256)
    freq_filtered, psd_filtered = welch(filtered_data, fs=sampling_rate, nperseg=256)
    
    # Inspect how these components are affected by filtering
    original_lf_power = np.sum(psd_original[freq_original <= cutoff])
    filtered_lf_power = np.sum(psd_filtered[freq_filtered <= cutoff])
    
    attenuation_ratio = original_lf_power / filtered_lf_power
    
    # Print stats about the power in respective bands
    print(f"Low-frequency power (Original): {original_lf_power:.4f}")
    print(f"Low-frequency power (Filtered): {filtered_lf_power:.4f}")
    print(f"Attenuation Ratio for Low Frequency: {attenuation_ratio:.4f}")
    print("Ready to perform downsampling...")

def solver(input_data, sampling_rate=None):
    nyquist_rate = sampling_rate / 2
    cutoff = 25
    filter_order = 100
    
    # Filter data
    fir_coeff = firwin(filter_order, cutoff / nyquist_rate)
    filtered_data = lfilter(fir_coeff, 1.0, input_data)
    
    # Downsample
    downsample_factor = 2
    downsampled_data = filtered_data[::downsample_factor]
    
    return downsampled_data

### Index 1 ###
### Index 2 ###
