### Index 0 ###
import numpy as np
import scipy.signal as sps

def inspection(input_data, sampling_rate=50):
    # 1. Check if the signal is periodic
    f, Pxx_den = sps.periodogram(input_data, sampling_rate)
    dominant_freqs = f[np.argsort(Pxx_den)[-3:]]  # Top 3 dominant frequencies
    
    # 2. General trend detection
    trend = np.polyfit(np.arange(len(input_data)), input_data, 1)
    
    # 3. Check for unwanted frequency components (like powerline noise)
    undesirable_freq = 50  # Common powerline
    if undesirable_freq in dominant_freqs:
        print("Powerline interference detected at 50Hz.")
    
    # 4. Check for missing values
    if np.any(np.isnan(input_data)):
        print("The signal contains NaN values.")
    else:
        print("No missing values detected in the signal.")
    
    print(f"Dominant frequencies in the signal are: {dominant_freqs}")
    print(f"The linear trend of the signal is: slope={trend[0]}, intercept={trend[1]}.")

# Assuming that input_data and the sampling rate are provided
# inspection(input_data, sampling_rate)

### Index 1 ###
import numpy as np
import pmdarima as pm

def solver(input_data, sampling_rate=50):
    # Fit an ARIMA model
    model = pm.auto_arima(input_data, seasonal=False, trace=False,
                          error_action='ignore', suppress_warnings=True)
    
    # Predict the next 50 data points
    forecast = model.predict(n_periods=50)
    
    return np.array(forecast)

# Assuming that input_data and the sampling rate are provided
# predicted_values = solver(input_data, sampling_rate)
# print(predicted_values)

### Index 2 ###
### Index 3 ###
