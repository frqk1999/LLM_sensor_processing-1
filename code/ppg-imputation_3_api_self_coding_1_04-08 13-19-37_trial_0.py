### Index 0 ###
import numpy as np
import pandas as pd

def inspection(input_data, sampling_rate=None):
    # 1) Check for periodicity
    is_periodic = np.allclose(input_data[:len(input_data)//2], input_data[len(input_data)//2:], atol=1e-2)
    print("Signal periodicity:", "Periodic" if is_periodic else "Non-periodic")
    
    # Since sampling rate is provided for PPG, consider analyzing the frequency if needed
    if sampling_rate:
        # Calculate the Fast Fourier Transform (FFT) to find dominant frequencies
        fft_result = np.fft.fft(input_data)
        fft_freq = np.fft.fftfreq(len(input_data), 1/sampling_rate)
        
        # Only take positive frequencies
        positive_freqs = fft_freq[:len(fft_freq)//2]
        positive_fft = np.abs(fft_result[:len(fft_result)//2])
        dominant_freq_index = np.argmax(positive_fft)
        print("Dominant frequency components frequency:", positive_freqs[dominant_freq_index])

    # 2) Check the trend of the signals
    trend = np.polyfit(np.arange(len(input_data)), input_data, 1)
    print("Signal trend: Slope =", trend[0], "; Intercept =", trend[1])

    # 3) Check for unwanted frequencies (such as powerline noise)
    unwanted_freq = 50  # Powerline noise is typically 50Hz or 60Hz
    if any(positive_freqs[dominant_freq_index] == unwanted_freq for index, freq in enumerate(positive_freqs)):
        print("Potential powerline noise detected at 50Hz")

    # 4) Check for missing values
    missing_values = np.isnan(input_data).sum()
    print("Number of missing values:", missing_values)

### Index 1 ###
import numpy as np
import pandas as pd

def solver(input_data, sampling_rate=None):
    # Use pandas to interpolate missing values
    series_data = pd.Series(input_data)
    
    # Filling the missing values using linear interpolation
    filled_data = series_data.interpolate(method='linear', limit_direction='forward')
    
    # Identify and extract the missing values that were filled
    missing_values_only = filled_data[np.isnan(input_data)]
    
    # Return the missing values only
    return missing_values_only.values

### Index 2 ###
### Index 3 ###
