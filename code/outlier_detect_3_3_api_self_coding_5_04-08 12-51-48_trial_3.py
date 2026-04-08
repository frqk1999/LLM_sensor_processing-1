### Index 0 ###
import numpy as np
import pandas as pd
from scipy.signal import find_peaks

def inspection(input_data, sampling_rate=None):
    # Ensure input_data is a valid NumPy array
    if not isinstance(input_data, np.ndarray):
        print("Error: Input data is not a numpy array.")
        return
    
    # Check for missing or NaN values
    if np.any(np.isnan(input_data)):
        print("Missing values detected.")
    else:
        print("No missing values.")

    # Check for trends and variability using rolling statistics
    input_series = pd.Series(input_data)
    rolling_mean = input_series.rolling(window=24).mean()
    rolling_std = input_series.rolling(window=24).std()
    
    # Maintain series of differences to understand changes
    differences = input_series.diff().dropna()
    rolling_diff_mean = differences.rolling(window=24).mean()
    rolling_diff_std = differences.rolling(window=24).std()

    # Detect peaks and anomalous trends in differences
    thresholds = rolling_diff_mean + 3 * rolling_diff_std
    anomalies = differences > thresholds
    anomaly_indices = np.where(anomalies)[0]

    print(f"Anomalous positions detected at indices: {anomaly_indices}")

    # Plot results if needed (commented out since visualization is not allowed)
    # import matplotlib.pyplot as plt
    # plt.plot(input_data, label=\'Data\')
    # plt.scatter(anomaly_indices, input_data[anomaly_indices], color=\'red\', label=\'Anomalies\')
    # plt.legend()
    # plt.show()

    return anomaly_indices

### Index 1 ###
import numpy as np
import pandas as pd

def solver(input_data, sampling_rate=None):
    # Ensure input_data is a valid NumPy array
    if not isinstance(input_data, np.ndarray):
        raise ValueError("Input data is not a numpy array.")
    
    # Convert input data to a pandas series
    input_series = pd.Series(input_data)
    
    # Use a more refined rolling means and deviation method
    rolling_mean = input_series.rolling(window=24).mean().shift(1)
    rolling_std = input_series.rolling(window=24).std().shift(1)
    
    # Calculate differences and identify anomalies
    diff = (input_series - rolling_mean) / rolling_std
    anomaly_threshold = 3  # Typical threshold for Z-score anomaly detection

    # Identify anomalies based on cumulative deviation passing threshold
    anomaly_indices = diff[diff.abs() > anomaly_threshold].index.values
    
    # Return the detected anomaly indices
    return anomaly_indices

### Index 2 ###
### Index 3 ###
