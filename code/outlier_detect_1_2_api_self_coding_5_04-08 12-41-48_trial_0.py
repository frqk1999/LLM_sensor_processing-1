### Index 0 ###
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from statsmodels.tsa.seasonal import seasonal_decompose

def inspection(input_data, sampling_rate=None):
    # 1) Check if the signal is periodic by performing a seasonal decomposition.
    try:
        decomposed = seasonal_decompose(input_data, period=24)  # Assuming daily periodicity
        
        print("Seasonal Decomposition:")
        print("Trend Component: ", decomposed.trend)
        print("Seasonal Component: ", decomposed.seasonal)
        print("Residual Component: ", decomposed.resid)
    except Exception as e:
        print("Decomposition Error:", e)
    
    # 2) Check the trend of the signal
    trend = pd.Series(input_data).rolling(window=24, center=True).mean()
    print("Rolling Trend (24-hour window):", trend)
    
    # 3) Check for any unexpected peaks as a proxy for unwanted corruption
    peaks, _ = find_peaks(input_data)
    print(f"Detected Peaks at: {peaks}")
    
    # 4) Check for missing values
    if np.isnan(input_data).any():
        print("Missing Values Detected")
    else:
        print("No Missing Values")

### Index 1 ###
from scipy.stats import zscore

def solver(input_data, sampling_rate=None):
    # Use Z-score method for anomaly detection
    data_zscore = zscore(input_data)
    
    # Define a threshold for anomaly detection
    threshold = 3  # Typically, 2.5 to 3 sigma
    
    # Get positions with absolute z-score higher than the threshold
    anomaly_positions = np.where(np.abs(data_zscore) > threshold)[0]

    return anomaly_positions

### Index 2 ###
### Index 3 ###
