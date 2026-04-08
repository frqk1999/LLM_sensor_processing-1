### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # 1) Check if the output_data has the valid range, is empty, or contains missing values.
    # Here we ensure the output_data matches expectations for a set of indices.
    # Args:
    #   input_data: numpy.ndarray. The data provided by the user to perform DSP.
    #   output_data: numpy.ndarray. The data processed by the other AI agent.
    #   sampling_rate: int, optional. The sampling rate of the data which may be necessary for certain analyses.

    if output_data is None or len(output_data) == 0:
        return False
    
    if np.any(np.isnan(output_data)):  # Check for NaN values.
        return False

    if np.any(output_data < 0) or np.any(output_data >= len(input_data)):
        return False  # Check if outlier positions are within valid index range of input_data.

    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.stats import zscore

    # Calculate z-scores of the input_data
    z_scores = zscore(input_data)

    # Define a threshold for considering a point as an outlier
    outlier_threshold = 3

    # Identify outlier positions based on the threshold
    expected_outlier_positions = np.where(np.abs(z_scores) > outlier_threshold)[0]

    # Determine if the calculated outlier positions match the detected ones
    detected_positions_set = set(output_data)
    expected_positions_set = set(expected_outlier_positions)

    # Check if all detected outliers are in the expected positions
    if detected_positions_set.issubset(expected_positions_set):
        return True

    return False

### Index 2 ###
