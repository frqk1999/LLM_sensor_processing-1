### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False. 
    # 1) Check if the output_data has the valid range, is empty, or contains missing values. 
    # 2) Do NOT check the data type - using the isinstance or np.isscalar function is not reliable.
    # Args:
    #   input_data: The data type is numpy.ndarray. This is the data provided by the user to perform DSP. 
    #   output_data: The data type is numpy.ndarray. This is the data processed by the other AI agent. 
    #   sampling_rate: The sampling rate of the data.
    # Output: boolean variable - True or False. If the result does not pass your test, output False. Else, output True.
    
    # Check if the output_data is empty
    if output_data.size == 0:
        return False
    
    # Ensure that output data does not contain missing (NaN) values
    if np.isnan(output_data).any():
        return False

    # Check if all indices are within the range of the input data length
    if np.any(output_data < 0) or np.any(output_data >= len(input_data)):
        return False
    
    return True

inspection(input_data, output_data, sampling_rate=500)

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    # Verify whether detected outlier positions correspond to significant deviations.
    # Args:
    #   input_data: The data type is numpy.ndarray. This is the data provided by the user to perform DSP. 
    #   output_data: The data type is numpy.ndarray. This is the data processed by the other AI agent. 
    #   sampling_rate: The sampling rate of the data.
    # Return: boolean variable - True or False.
    
    # Calculate the IQR and use similar logic to determine bounds
    detrended_data = signal.detrend(input_data)
    q1 = np.percentile(detrended_data, 25)
    q3 = np.percentile(detrended_data, 75)
    iqr_value = iqr(detrended_data)
    
    # Define factor for outlier range
    factor = 1.5  # Common IQR factor for outlier detection
    lower_bound = q1 - (factor * iqr_value)
    upper_bound = q3 + (factor * iqr_value)
    
    # Validate the outliers detected lie beyond the IQR bounds
    valid_outliers = True
    for pos in output_data:
        if not (detrended_data[pos] < lower_bound or detrended_data[pos] > upper_bound):
            valid_outliers = False
            break
    
    return valid_outliers

challenger(input_data, output_data, sampling_rate=500)

### Index 2 ###
def challenger(input_data, output_data, sampling_rate=None):
    # Verify whether detected outlier positions correspond to significant deviations.
    # Args:
    #   input_data: The data type is numpy.ndarray. This is the data provided by the user to perform DSP. 
    #   output_data: The data type is numpy.ndarray. This is the data processed by the other AI agent. 
    #   sampling_rate: The sampling rate of the data.
    # Return: boolean variable - True or False.
    
    # Ensure proper data type and handle non-numeric entries
    input_data = np.asarray(input_data, dtype=np.float64)

    # Remove trend for better anomaly detection comparison
    detrended_data = signal.detrend(input_data)
    
    # Replace NaN or inf with zero or appropriate default
    if np.any(np.isnan(detrended_data)) or np.any(np.isinf(detrended_data)):
        detrended_data = np.nan_to_num(detrended_data)  # Replace NaNs/Infs with zeroes
        print("Warning: Replaced NaN and inf in detrended_data with zeros before checking.")
    
    # Calculate the IQR and use similar logic to determine bounds
    q1 = np.percentile(detrended_data, 25)
    q3 = np.percentile(detrended_data, 75)
    iqr_value = iqr(detrended_data)
    
    # Define factor for outlier range
    factor = 1.5  # Common IQR factor for outlier detection
    lower_bound = q1 - (factor * iqr_value)
    upper_bound = q3 + (factor * iqr_value)
    
    # Validate the outliers detected lie beyond the IQR bounds
    valid_outliers = True
    for pos in output_data:
        if not (detrended_data[pos] < lower_bound or detrended_data[pos] > upper_bound):
            valid_outliers = False
            break
    
    return valid_outliers

challenger(input_data, output_data, sampling_rate=500)

### Index 3 ###
def challenger(input_data, output_data, sampling_rate=None):
    # Verify whether detected outlier positions correspond to significant deviations.
    # Args:
    #   input_data: The data type is numpy.ndarray. This is the data provided by the user to perform DSP. 
    #   output_data: The data type is numpy.ndarray. This is the data processed by the other AI agent. 
    #   sampling_rate: The sampling rate of the data.
    # Return: boolean variable - True or False.
    
    # Ensure proper data type and handle non-numeric entries
    try:
        input_data = np.asarray(input_data, dtype=np.float64)
    except ValueError:
        print("Error: Input data contains non-numeric values.")
        return False

    # Check and sanitize input data before processing
    if np.any(np.isnan(input_data)) or np.any(np.isinf(input_data)):
        input_data = np.nan_to_num(input_data)  # Replace NaNs/Infs with zeroes
        print("Warning: Replaced NaN and inf in input_data with zeros before processing.")

    # Remove trend for better anomaly detection comparison
    detrended_data = signal.detrend(input_data)
    
    # Confirm any remaining NaN or infinite values in detrended data
    if np.any(np.isnan(detrended_data)) or np.any(np.isinf(detrended_data)):
        detrended_data = np.nan_to_num(detrended_data)  # Replace NaNs/Infs with zeroes
        print("Warning: Replaced NaN and inf in detrended_data with zeros before checking.")
    
    # Calculate the IQR and use similar logic to determine bounds
    q1 = np.percentile(detrended_data, 25)
    q3 = np.percentile(detrended_data, 75)
    iqr_value = iqr(detrended_data)
    
    # Define factor for outlier range
    factor = 1.5  # Common IQR factor for outlier detection
    lower_bound = q1 - (factor * iqr_value)
    upper_bound = q3 + (factor * iqr_value)
    
    # Validate the outliers detected lie beyond the IQR bounds
    valid_outliers = True
    for pos in output_data:
        if not (detrended_data[pos] < lower_bound or detrended_data[pos] > upper_bound):
            valid_outliers = False
            break
    
    return valid_outliers

challenger(input_data, output_data, sampling_rate=500)

### Index 4 ###
