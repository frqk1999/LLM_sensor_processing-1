### Index 0 ###
import numpy as np
from scipy.signal import find_peaks

def inspection(input_data, sampling_rate=None):
    # Step 1: Check for missing values
    n_missing = np.isnan(input_data).sum()
    
    # Step 2: Detect dominant frequency components if periodic (using FFT)
    if sampling_rate is not None:
        freqs = np.fft.fftfreq(len(input_data), d=1/sampling_rate)
        fft_values = np.fft.fft(input_data)
        dominant_freq_index = np.argmax(np.abs(fft_values))
        dominant_frequency = abs(freqs[dominant_freq_index])
    else:
        dominant_frequency = None
      
    # Step 3: Detect potential periodic patterns using autocorrelation
    periodic = np.correlate(input_data, input_data, mode=\'full\')
    
    # Step 4: Check the trend using linear regression (over a simple model here)
    x = np.arange(len(input_data))
    trend = np.polyfit(x, input_data, 1)
    
    summary = {
        "Missing Values": n_missing,
        "Dominant Frequency": dominant_frequency,
        "Periodicity Estimation": periodic,
        "Trend": trend
    }
    
    print("Inspection Result:")
    for key, value in summary.items():
        print(f"{key}: {value}")

### Index 1 ###
from scipy.stats import median_absolute_deviation

def solver(input_data, sampling_rate=None):
    # Step 1: Handle missing values
    # Replace missing (NaN) values with the median of the signal
    median_val = np.nanmedian(input_data)
    data_filled = np.where(np.isnan(input_data), median_val, input_data)
    
    # Step 2: Detect outliers using a robust method (e.g. MAD)
    mad_val = median_absolute_deviation(data_filled)
    threshold = 3 * mad_val  # Typically, 3 times the MAD
    median_of_data = np.median(data_filled)
    
    # Identify where the outliers are
    abs_diff = np.abs(data_filled - median_of_data)
    outliers_positions = np.where(abs_diff > threshold)[0]
    
    return outliers_positions

### Index 2 ###
import numpy as np

def solver(input_data, sampling_rate=None):
    # Step 1: Handle missing values
    # Replace missing (NaN) values with the median of the signal
    median_val = np.nanmedian(input_data)
    data_filled = np.where(np.isnan(input_data), median_val, input_data)
    
    # Step 2: Detect outliers using a robust method (e.g., MAD)
    def median_absolute_deviation(data):
        """Calculate median absolute deviation (MAD)"""
        median = np.median(data)
        deviation = np.abs(data - median)
        mad = np.median(deviation)
        return mad
    
    mad_val = median_absolute_deviation(data_filled)
    threshold = 3 * mad_val  # Typically, 3 times the MAD
    median_of_data = np.median(data_filled)
    
    # Identify where the outliers are
    abs_diff = np.abs(data_filled - median_of_data)
    outliers_positions = np.where(abs_diff > threshold)[0]
    
    return outliers_positions

### Index 3 ###
### Index 4 ###
