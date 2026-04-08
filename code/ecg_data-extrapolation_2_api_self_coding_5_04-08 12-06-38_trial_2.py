### Index 0 ###
def inspection(input_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import find_peaks, welch
    import pandas as pd

    def check_periodicity(data, sampling_rate):
        # Find the power spectral density to check dominant frequencies
        freqs, psd = welch(data, fs=sampling_rate)
        # Identify peaks within the PSD to find dominant frequencies
        peak_indices, _ = find_peaks(psd)
        dominant_freqs = freqs[peak_indices]
        peak_powers = psd[peak_indices]

        if len(peak_indices) > 0:
            is_periodic = True
            dominant_freq = freqs[np.argmax(psd)]
        else:
            is_periodic = False
            dominant_freq = None

        return is_periodic, dominant_freq, dominant_freqs, peak_powers

    def check_trend(data):
        # Using rolling mean to observe trends
        df = pd.Series(data)
        rolling_mean = df.rolling(window=50).mean()
        return rolling_mean

    def check_missing_values(data):
        return np.isnan(data).any()

    # Reset print statement for an organized output
    print("\
ECG Signal Inspection Results:")
    
    # Periodicity Check
    is_periodic, dominant_freq, dominant_freqs, peak_powers = check_periodicity(input_data, sampling_rate)
    
    if is_periodic:
        print(f"Signal is periodic with dominant frequency: {dominant_freq} Hz")
        print(f"Other identified frequency components: {dominant_freqs} with powers: {peak_powers}")
    else:
        print("Signal is non-periodic.")

    # Trend Check
    rolling_mean = check_trend(input_data)
    print("Rolling mean calculated for trend analysis.")

    # Corruption Check (e.g., unwanted frequencies)
    if dominant_freq:
        print("Dominant frequency identified likely represents physiological cycles.")
    
    # Missing Values Check
    has_missing = check_missing_values(input_data)
    if has_missing:
        print("Signal has missing values.")
    else:
        print("No missing values detected in the signal.")

### Index 1 ###
def solver(input_data, sampling_rate=None):
    import numpy as np
    from statsmodels.tsa.holtwinters import ExponentialSmoothing
    
    # Convert to timeseries format
    data = np.asarray(input_data)

    # Define the seasonal period based on dominant frequency
    seasonal_periods = int(sampling_rate / 4.1)

    # Attempt to use Holt-Winters' Exponential Smoothing to capture trend and seasonality
    model = ExponentialSmoothing(
        data,
        seasonal_periods=seasonal_periods,
        trend='add',
        seasonal='add',
        damped_trend=True
    )

    # Fit the model
    model_fit = model.fit()

    # Forecasting the next 50 samples
    forecast = model_fit.forecast(steps=50)
    
    # Return forecasted values
    return forecast

### Index 2 ###
### Index 3 ###
