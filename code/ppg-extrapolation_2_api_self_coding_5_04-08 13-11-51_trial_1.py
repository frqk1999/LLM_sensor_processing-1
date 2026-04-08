### Index 0 ###
def inspection(input_data, sampling_rate=50):
    import numpy as np
    from scipy.signal import find_peaks
    import statsmodels.api as sm
    
    # 1) Check if the signal is periodic or non-periodic
    n = len(input_data)
    freqs, power_spectrum = np.fft.rfftfreq(n, 1/sampling_rate), np.abs(np.fft.rfft(input_data))**2
    dominant_freqs = freqs[np.argsort(power_spectrum)[-3:]]  # Top 3 dominant frequencies
    print(f"Dominant Frequencies: {dominant_freqs} Hz")
        
    # 2) Check the trend of the signals
    decomposition = sm.tsa.seasonal_decompose(input_data, period=int(sampling_rate), model=\'additive\')
    print("Trend component first few values:", decomposition.trend[:5])
    
    # 3) Check if there is any source of corruption in the signal, such as unwanted frequency
    unwanted_freq_threshold = 0.1  # Arbitrary threshold to identify unwanted noise
    significant_freqs = freqs[power_spectrum > unwanted_freq_threshold]
    print(f"Significant Frequencies: {significant_freqs}")
    
    # 4) Check any missing values
    missing_values = np.isnan(input_data).sum()
    print(f"Number of missing values: {missing_values}")

### Index 1 ###
def solver(input_data, sampling_rate=50):
    import numpy as np
    import pmdarima as pm
    
    # Fit a seasonal ARIMA model
    # Considering seasonal order focusing on the discovered periodic components (1.4 Hz as a base cycle)
    model = pm.auto_arima(input_data, seasonal=True, m=int(sampling_rate/1.4),    # Here periodicity m derived from the dominant frequency
                          stepwise=True, suppress_warnings=True, error_action="ignore")
    
    # Predict the next 50 values
    forecast = model.predict(n_periods=50)
    
    return forecast

### Index 2 ###
### Index 3 ###
