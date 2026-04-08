### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Check if the output_data has valid range, isn't empty, and contains no missing values.
    if output_data.size == 0:
        return False
    if np.any(np.isnan(output_data)):
        return False
    if not np.isfinite(output_data).all():
        return False
    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=500):
    import numpy as np
    import scipy.signal as signal

    # Calculate the Power Spectral Density (PSD) of the input_data and output_data
    freqs_input, psd_input = signal.welch(input_data, fs=sampling_rate)
    freqs_output, psd_output = signal.welch(output_data, fs=sampling_rate)

    # Find the power at 50 Hz in both input and output
    input_power_50Hz = psd_input[np.argmin(np.abs(freqs_input - 50))]
    output_power_50Hz = psd_output[np.argmin(np.abs(freqs_output - 50))]

    # Check if the power at 50 Hz has been significantly reduced in the output
    power_reduction = output_power_50Hz < (input_power_50Hz * 0.1)  # True if reduced by at least 90%

    return power_reduction

### Index 2 ###
