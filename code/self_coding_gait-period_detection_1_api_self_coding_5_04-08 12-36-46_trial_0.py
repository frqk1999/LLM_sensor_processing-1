### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data is valid
    if output_data is None or len(output_data) != 1:
        return False
    if np.isnan(output_data).any() or output_data < 0:
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import find_peaks, detrend

    # Step 1: Detrend the data
    detrended_data = detrend(input_data)

    # Step 2: Find peaks with similar settings to those used in the solver
    peaks, _ = find_peaks(detrended_data, height=np.mean(detrended_data) + np.std(detrended_data) * 0.5, distance=sampling_rate/2)

    # Verify if enough peaks were detected
    if len(peaks) <= 1:
        return False

    # Calculate periods (differences in indices of consecutive peaks)
    periods = np.diff(peaks) / sampling_rate  # Convert sample index distance to time
    estimated_average_period = np.mean(periods)

    # Verify the calculated period against the output data
    # Ensure the estimated period is close to the provided output_data period, allowing small tolerance
    if not np.isclose(estimated_average_period, output_data[0], rtol=0.1):
        return False

    return True

### Index 2 ###
