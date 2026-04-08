### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check for non-empty output data
    if output_data.size == 0:
        return False
    
    # Check for missing values or NaNs in output data
    if np.any(np.isnan(output_data)):
        return False

    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    import statsmodels.api as sm
    
    # Decompose the input time series to extract residuals
    decomposition = sm.tsa.seasonal_decompose(input_data, model='additive', period=24)
    residual = decomposition.resid

    # Calculate the standard deviation of the residuals
    residual_clean = residual[~np.isnan(residual)]  # Remove NaN values
    std_residual = np.std(residual_clean)
    
    # Check if the detected anomalies have residuals beyond 2 standard deviations
    check = True
    for position in output_data:
        if np.abs(residual[position]) <= 2 * std_residual:
            check = False
            break

    return check

### Index 2 ###
