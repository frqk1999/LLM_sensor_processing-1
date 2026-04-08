### Index 0 ###
def inspection(input_data, output_data, sampling_rate=None):
    # Inspect the output_data and output True/False. 
    # 1) Check if the output_data has the valid range, is empty, or contains missing values. 
    # 2) Do NOT check the data type - using the isinstance or np.isscalar function is not reliable.
    # Args:
    #   input_data: The data type is numpy.ndarray. This is the data provided by the user to perform DSP. 
    #   output_data: The data type is numpy.ndarray. The variable is provided through the function interface for you. This is the data processed by the other AI agent. 
    #   sampling_rate: The sampling rate of the data. sampling_rate is mandatory for speech, ecg, ppg, and gait data. It could be optional for others.
    # Output: boolean variable - True or False. If the result does not pass your test, output False. Else, output True.
    
    import numpy as np

    # Check if the output_data is empty
    if output_data.size == 0:
        return False

    # Check for missing values in output_data
    if np.any(np.isnan(output_data)):
        return False
    
    # Check if values in output_data are within a reasonable range
    # ECG values are typically within a range, assuming normalized data here for simplicity
    if np.any(output_data > 5) or np.any(output_data < -5):  # Example range check
        return False

    return True

### Index 1 ###
def challenger(input_data, output_data, sampling_rate=None):
    import numpy as np
    from scipy.signal import welch

    # Calculate Welch power spectral density estimate for input data
    f_input, Pxx_input = welch(input_data, fs=sampling_rate)
    # Calculate Welch power spectral density estimate for output data
    f_output, Pxx_output = welch(output_data, fs=sampling_rate)

    # Define the frequency range for baseline drift and QRS complex
    drift_freq_range = (0, 0.5)  # Typically baseline drift is <0.5 Hz
    qrs_freq_range = (5, 15)     # Approximate frequency range for QRS complex

    # Calculate power in the drift frequency range for input and output
    drift_power_input = np.sum(Pxx_input[(f_input >= drift_freq_range[0]) & (f_input <= drift_freq_range[1])])
    drift_power_output = np.sum(Pxx_output[(f_output >= drift_freq_range[0]) & (f_output <= drift_freq_range[1])])

    # Calculate power in the QRS frequency range for input and output
    qrs_power_input = np.sum(Pxx_input[(f_input >= qrs_freq_range[0]) & (f_input <= qrs_freq_range[1])])
    qrs_power_output = np.sum(Pxx_output[(f_output >= qrs_freq_range[0]) & (f_output <= qrs_freq_range[1])])

    # Check if the drift power is reduced in the output while QRS power is preserved
    drift_reduction_check = drift_power_output < 0.5 * drift_power_input
    qrs_preservation_check = qrs_power_output > 0.7 * qrs_power_input

    # Return True if both the drift is attenuated and the QRS complex is preserved
    return drift_reduction_check and qrs_preservation_check

### Index 2 ###
