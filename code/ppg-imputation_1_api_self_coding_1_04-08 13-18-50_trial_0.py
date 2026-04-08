### Index 0 ###
import numpy as np
import scipy.signal as signal

def inspection(input_data, sampling_rate=None):
    # Check if there are any missing values
    missing_values = np.isnan(input_data)
    num_missing_values = np.sum(missing_values)
    
    print(f"Number of missing values: {num_missing_values}")
    
    # If there are missing values, print their indices
    if num_missing_values > 0:
        missing_indices = np.where(missing_values)[0]
        print(f"Indices of missing values: {missing_indices}")
    
    # Check for periodicity by finding dominant frequency components
    if sampling_rate is not None:
        freqs, power = signal.periodogram(input_data[~missing_values], fs=sampling_rate)
        peak_freq = freqs[np.argmax(power)]
        print(f"Dominant frequency component: {peak_freq} Hz")
    
    # Check the trend of non-missing signal parts by evaluating moving averages
    non_missing_data = input_data[~missing_values]
    rolling_mean = pd.Series(non_missing_data).rolling(window=10, min_periods=1).mean()
    print(f"Trend estimate (first 5 values): {rolling_mean.head().values}")
    
    # Check for unwanted frequency components, focusing here on checking if 50 Hz powerline interference is present
    if sampling_rate is not None:
        if 48 <= peak_freq <= 52:
            print("Detected potential powerline interference near 50 Hz.")
        else:
            print("No significant powerline interference detected.")

# Assuming input_data and sampling_rate are provided
# inspection(input_data, sampling_rate=50)

### Index 1 ###
import numpy as np
import scipy.signal as signal
import pandas as pd  # Importing pandas for rolling mean calculation

def inspection(input_data, sampling_rate=None):
    # Check if there are any missing values
    missing_values = np.isnan(input_data)
    num_missing_values = np.sum(missing_values)
    
    print(f"Number of missing values: {num_missing_values}")
    
    # If there are missing values, print their indices
    if num_missing_values > 0:
        missing_indices = np.where(missing_values)[0]
        print(f"Indices of missing values: {missing_indices}")
    
    # Check for periodicity by finding dominant frequency components
    if sampling_rate is not None:
        freqs, power = signal.periodogram(input_data[~missing_values], fs=sampling_rate)
        peak_freq = freqs[np.argmax(power)]
        print(f"Dominant frequency component: {peak_freq} Hz")

    # Check the trend of non-missing signal parts by evaluating moving averages
    non_missing_data = input_data[~missing_values]
    rolling_mean = pd.Series(non_missing_data).rolling(window=10, min_periods=1).mean()
    print(f"Trend estimate (first 5 values): {rolling_mean.head().values}")
    
    # Check for unwanted frequency components, focusing here on checking if 50 Hz powerline interference is present
    if sampling_rate is not None:
        if 48 <= peak_freq <= 52:
            print("Detected potential powerline interference near 50 Hz.")
        else:
            print("No significant powerline interference detected.")

# Assuming input_data and sampling_rate are provided
# inspection(input_data, sampling_rate=50)

### Index 2 ###
import numpy as np
import pandas as pd

def solver(input_data, sampling_rate=None):
    # Convert input data into a pandas Series for convenience
    data_series = pd.Series(input_data)
    
    # Use linear interpolation to fill missing values
    imputed_data = data_series.interpolate(method='linear')
    
    # Extract only the imputed values that were originally missing
    missing_indices = np.where(np.isnan(input_data))[0]
    imputed_values = imputed_data.iloc[missing_indices].values
    
    # Return only the imputed missing values
    return imputed_values

# Assuming input_data and sampling_rate are provided
# imputed_values = solver(input_data, sampling_rate=50)
# print(imputed_values)

### Index 3 ###
### Index 4 ###
