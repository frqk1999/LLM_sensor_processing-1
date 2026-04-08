### Index 0 ###
def inspection(input_data, sampling_rate):
    import numpy as np
    from scipy.signal import find_peaks
    from scipy.fft import fft
    
    # 1) Periodicity and Dominant Frequencies
    n = len(input_data)
    yf = fft(input_data)
    xf = np.fft.fftfreq(n, 1 / sampling_rate)
    indices = np.argsort(np.abs(yf))[-10:]  # Get dominant frequencies
    dominant_freqs = xf[indices]
    print("Dominant Frequencies (Hz):", dominant_freqs)
    
    # Check periodicity via peaks
    peaks, _ = find_peaks(input_data)
    if len(peaks) > 1:
        print("The signal is likely periodic.")
    else:
        print("The signal does not exhibit strong periodicity.")
    
    # 2) Trend Analysis (using simple difference approach)
    trend = np.diff(input_data)
    if np.all(trend > 0):
        print("The signal shows an increasing trend.")
    elif np.all(trend < 0):
        print("The signal shows a decreasing trend.")
    else:
        print("The signal shows no clear trend.")
        
    # 3) Check for possible noise or unwanted frequencies
    powerline_noise_freq = 50  # Hz, commonly see in power lines
    if powerline_noise_freq in dominant_freqs:
        print("Possible powerline noise detected at 50 Hz.")
    
    # 4) Check for missing values
    if np.any(np.isnan(input_data)):
        print("There are missing values in the data.")
    else:
        print("No missing values detected in the data.")

### Index 1 ###
def solver(input_data, sampling_rate):
    import numpy as np
    from statsmodels.tsa.ar_model import AutoReg

    # Fit an autoregressive model to the data
    model = AutoReg(input_data, lags=20, old_names=False)  # 20 lags assuming short-term dependence
    model_fit = model.fit()

    # Predict the next 50 values
    num_points_to_predict = 50
    forecasted_values = model_fit.predict(start=len(input_data), end=len(input_data) + num_points_to_predict - 1)
    
    return forecasted_values

### Index 2 ###
### Index 3 ###
