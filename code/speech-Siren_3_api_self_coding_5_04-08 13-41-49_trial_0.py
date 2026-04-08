### Index 0 ###
def inspection(input_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import find_peaks, periodogram
    
    # 1) Check if the signal is periodic or non-periodic.
    # Use periodogram to find dominant frequency components.
    f, Pxx = periodogram(input_data, fs=sampling_rate)
    
    # Identify significant peaks, which can indicate dominant frequencies.
    peaks, _ = find_peaks(Pxx, height=np.max(Pxx)/5, distance=5)
    
    print("Frequency components detected:")
    for peak in peaks:
        print(f"Frequency: {f[peak]:.2f} Hz, Power: {Pxx[peak]:.4f}")
    
    # 2) Check the trend of the signal.
    trend = np.polyfit(range(len(input_data)), input_data, 1)
    print(f"Signal trend: Slope = {trend[0]:.5f}, Intercept = {trend[1]:.5f}")
    
    # 3) Check for unwanted frequencies indicating corruption.
    if len(peaks) > 0:
        dominant_frequencies = f[peaks]
        print("Potential noise frequencies:", dominant_frequencies)
    
    # 4) Check any missing values.
    if np.any(np.isnan(input_data)):
        print("Missing values detected in the input data.")
    else:
        print("No missing values in the input data.")

### Index 1 ###
def solver(input_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import iirnotch, lfilter
    
    # Frequencies identified as siren noise components
    noise_frequencies = [158.40, 320.61, 729.01, 753.82, 767.18, 782.44, 803.44, 816.79, 832.06, 856.87, 877.86]

    # Create band-stop filters for each identified frequency
    filtered_signal = input_data
    for freq in noise_frequencies:
        # Quality factor: determines the width of the notch
        q_factor = 30.0  # Adjust as needed
        b, a = iirnotch(w0=freq / (sampling_rate / 2), Q=q_factor)
        filtered_signal = lfilter(b, a, filtered_signal)
    
    # Return the filtered signal
    return filtered_signal

### Index 2 ###
### Index 3 ###
