### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False. 
    # 1) Check if the output_data has the valid range, is empty, or contains missing values. 
    # 2) The use of isinstance or np.isscalar function is not reliable.

    import numpy as np

    # Check for empty output
    if output_data.size == 0:
        return False

    # Check for NaN values
    if np.isnan(output_data).any():
        return False

    # Validity of range: Check for any unusually large or small values
    # In the context of ECG signals, we might expect outputs within a reasonable range from input mean
    input_mean = np.mean(input_data)
    input_std = np.std(input_data)

    # Define a range based on the input data
    allowed_range = (input_mean - 5*input_std, input_mean + 5*input_std)

    if not np.all((output_data >= allowed_range[0]) & (output_data <= allowed_range[1])):
        return False

    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    import pandas as pd
    from scipy.signal import find_peaks

    # Check for preservation of periodicity
    # Using autocorrelation to check periodicity consistency
    autocorr_input = np.correlate(input_data - np.mean(input_data), input_data - np.mean(input_data), mode='full')
    autocorr_input = autocorr_input[autocorr_input.size // 2:]
    
    autocorr_output = np.correlate(output_data - np.mean(output_data), output_data - np.mean(output_data), mode='full')
    autocorr_output = autocorr_output[autocorr_output.size // 2:]
    
    input_peaks, _ = find_peaks(autocorr_input, distance=len(input_data)//2, height=0)
    output_peaks, _ = find_peaks(autocorr_output, distance=len(output_data)//2, height=0)

    if len(input_peaks) == 0 or len(output_peaks) == 0:
        return False

    # Compare the dominant period detected
    dominant_period_input = np.diff(input_peaks) / sampling_rate
    dominant_period_output = np.diff(output_peaks) / sampling_rate
    
    if not np.isclose(np.mean(dominant_period_input), np.mean(dominant_period_output), atol=0.1):
        return False

    # Check for trend appropriateness
    output_trend = np.polyfit(np.arange(len(output_data)), output_data, 1)[0]
    input_trend = np.polyfit(np.arange(len(input_data)), input_data, 1)[0]
    
    if not np.isclose(output_trend, input_trend, atol=0.1):
        return False

    # Check for magnitude consistency
    rolling_mean_output = pd.Series(output_data).rolling(window=5).mean()
    mean_input, std_input = np.mean(input_data), np.std(input_data)
    if not (mean_input - 3 * std_input <= np.mean(rolling_mean_output.dropna()) <= mean_input + 3 * std_input):
        return False
    
    return True

### Index 2 ###
