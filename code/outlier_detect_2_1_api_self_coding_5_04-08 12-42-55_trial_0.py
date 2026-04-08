### Index 0 ###
def inspection(input_data, sampling_rate=None):
    import numpy as np
    import pandas as pd
    from scipy.signal import find_peaks
    import statsmodels.api as sm
    
    # 1. Check for missing values
    missing_values = np.isnan(input_data).sum()
    if missing_values > 0:
        print(f"Missing values found: {missing_values}")
    else:
        print("No missing values found.")
    
    # 2. Check for periodicity and dominant frequencies
    fft_values = np.fft.fft(input_data)
    fft_frequencies = np.fft.fftfreq(len(input_data), d=1/sampling_rate)
    
    # Get positive frequencies
    positive_frequencies = fft_frequencies[np.where(fft_frequencies > 0)]
    positive_fft_values = fft_values[np.where(fft_frequencies > 0)]
    
    # Find the peak frequency
    peak_indices, _ = find_peaks(np.abs(positive_fft_values))
    dominant_frequencies = positive_frequencies[peak_indices]
    print(f"Dominant frequencies: {dominant_frequencies}")
    
    # 3. Check trend
    decomposition = sm.tsa.seasonal_decompose(input_data, model=\'additive\', period=24)
    trend = decomposition.trend
    print(f"Trend detected, showing first 5 trend values: {trend[:5]}")
    
    # 4. Check for noise
    residual = decomposition.resid
    print(f"Residual analysis, showing first 5 residual values: {residual[:5]}")

### Index 1 ###
def inspection(input_data, sampling_rate=1):
    import numpy as np
    import pandas as pd
    from scipy.signal import find_peaks
    import statsmodels.api as sm

    # 1. Check for missing values
    missing_values = np.isnan(input_data).sum()
    if missing_values > 0:
        print(f"Missing values found: {missing_values}")
    else:
        print("No missing values found.")
    
    # 2. Check for periodicity and dominant frequencies
    if sampling_rate is None:
        sampling_rate = 1  # Defaults to 1 if not provided
        
    fft_values = np.fft.fft(input_data)
    fft_frequencies = np.fft.fftfreq(len(input_data), d=1/sampling_rate)
    
    # Get positive frequencies
    positive_frequencies = fft_frequencies[np.where(fft_frequencies > 0)]
    positive_fft_values = fft_values[np.where(fft_frequencies > 0)]
    
    # Find the peak frequency
    peak_indices, _ = find_peaks(np.abs(positive_fft_values))
    dominant_frequencies = positive_frequencies[peak_indices]
    print(f"Dominant frequencies: {dominant_frequencies}")
    
    # 3. Check trend
    decomposition = sm.tsa.seasonal_decompose(input_data, model=\'additive\', period=24)
    trend = decomposition.trend
    print(f"Trend detected, showing first 5 trend values: {trend[:5]}")
    
    # 4. Check for noise
    residual = decomposition.resid
    print(f"Residual analysis, showing first 5 residual values: {residual[:5]}")

### Index 2 ###
def solver(input_data, sampling_rate=1):
    import numpy as np
    import statsmodels.api as sm

    # 1. Decompose the time series to extract residuals
    decomposition = sm.tsa.seasonal_decompose(input_data, model=\'additive\', period=24)
    residual = decomposition.resid

    # 2. Calculate the standard deviation of the residuals
    residual_clean = residual[~np.isnan(residual)]  # Remove NaN values
    std_residual = np.std(residual_clean)

    # 3. Identify indices where residuals exceed threshold (e.g., 2 standard deviations)
    anomaly_indices = np.where(np.abs(residual_clean) > 2 * std_residual)[0]

    # Adjust indices to match original data (considering NaN removal)
    all_indices = np.arange(len(residual))
    effective_indices = all_indices[~np.isnan(residual)]
    anomaly_positions = effective_indices[anomaly_indices]

    print(f"Anomaly positions: {anomaly_positions}")
    return anomaly_positions

### Index 3 ###
### Index 4 ###
