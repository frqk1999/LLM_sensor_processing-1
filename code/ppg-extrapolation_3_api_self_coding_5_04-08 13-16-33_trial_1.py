### Index 0 ###
def inspection(input_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import find_peaks
    from scipy.fft import rfft, rfftfreq

    # Check missing values
    if np.any(np.isnan(input_data)):
        print("The signal contains missing values.")
    else:
        print("No missing values found in the signal.")
    
    # Detrend the data
    detrended_data = input_data - np.mean(input_data)
    
    # Compute FFT to find dominant frequencies
    N = len(input_data)
    yf = rfft(detrended_data)
    xf = rfftfreq(N, 1/sampling_rate)
    
    # Taking magnitude of FFT
    magnitude_spectrum = np.abs(yf)
    dominant_frequencies = xf[np.argsort(magnitude_spectrum)[-5:][::-1]]
    
    # Check periodicity
    if np.max(magnitude_spectrum) > np.mean(magnitude_spectrum) * 1.5:
        print(f"The signal appears to be periodic with dominant frequencies at: {dominant_frequencies} Hz")
    else:
        print("The signal does not show strong periodicity.")
    
    # Check for noise or unwanted frequencies
    peaks, _ = find_peaks(magnitude_spectrum, height=np.mean(magnitude_spectrum) + np.std(magnitude_spectrum))
    if len(peaks) > 1:
        print("The signal might contain noise or unwanted frequency components.")
    else:
        print("No significant noise detected.")
    
    # Check for trends
    if np.abs(np.mean(input_data) - np.median(input_data)) > np.std(input_data) * 0.1:
        print("A significant trend is detected in the signal.")
    else:
        print("No significant trend detected in the signal.")

### Index 1 ###
def solver(input_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import detrend
    from statsmodels.tsa.holtwinters import ExponentialSmoothing

    # Detrend the signal
    detrended_data = detrend(input_data)

    # Apply a Fourier Transform to model periodicity
    N = len(detrended_data)
    yf = np.fft.rfft(detrended_data)
    xf = np.fft.rfftfreq(N, 1/sampling_rate)

    # Zero out the frequencies that are outside the dominant range (e.g., above 5 Hz)
    # This assumes that the dominant frequencies are less than 5 Hz, based on inspection
    yf[(xf > 5)] = 0

    # Inverse Fourier Transform to reconstruct signal with only dominant frequencies
    filtered_signal = np.fft.irfft(yf, n=N)

    # Use Exponential Smoothing (or similar time series models) to capture remaining trends and predict
    model = ExponentialSmoothing(filtered_signal, seasonal='add', seasonal_periods=sampling_rate)
    model_fit = model.fit()

    # Forecast the next 50 values
    forecasted_values = model_fit.forecast(steps=50)
    
    return forecasted_values

### Index 2 ###
### Index 3 ###
