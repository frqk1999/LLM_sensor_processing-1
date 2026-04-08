### Index 0 ###
def inspection(input_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import find_peaks, periodogram
    
    # Check for missing values
    if np.any(np.isnan(input_data)):
        print("Missing values detected in input data.")
    
    # Check basic statistics
    print(f"Mean of the signal: {np.mean(input_data)}")
    print(f"Standard deviation of the signal: {np.std(input_data)}")

    # Periodicity Check using FFT
    frequencies, power_spectrum = periodogram(input_data, sampling_rate)
    dominant_frequency = frequencies[np.argmax(power_spectrum)]
    print(f"Dominant frequency: {dominant_frequency:.2f} Hz")
    
    # Peak detection to investigate periodic components
    peak_indices, _ = find_peaks(input_data, height=np.mean(input_data), distance=sampling_rate/2)
    if len(peak_indices) > 1:
        peak_intervals = np.diff(peak_indices) / sampling_rate
        average_interval = np.mean(peak_intervals)
        print(f"Average interval between peaks: {average_interval:.2f} seconds")

    # Trend Analysis
    trend = np.polyfit(np.arange(len(input_data)), input_data, 1)
    print(f"Trend: slope = {trend[0]}, intercept = {trend[1]}")

    # Noise Detection: Check for unexpected high frequency noise
    noise_level_threshold = np.mean(power_spectrum) + 2*np.std(power_spectrum)
    high_freq_noise = frequencies[power_spectrum > noise_level_threshold]
    
    if len(high_freq_noise) > 0:
        print("Detected potential high frequency noise at frequencies: ", high_freq_noise)
    else:
        print("No significant high frequency noise detected.")

### Index 1 ###
def solver(input_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import savgol_filter
    from statsmodels.tsa.ar_model import AutoReg
    
    # Step 1: Denoise the signal slightly without affecting the physiological information
    denoised_signal = savgol_filter(input_data, window_length=11, polyorder=2)

    # Step 2: Fit an autoregressive model
    model = AutoReg(denoised_signal, lags=20)
    model_fit = model.fit()

    # Step 3: Predict the next 50 values
    predicted_values = model_fit.predict(start=len(input_data), end=len(input_data) + 49, dynamic=False)

    return predicted_values

### Index 2 ###
### Index 3 ###
