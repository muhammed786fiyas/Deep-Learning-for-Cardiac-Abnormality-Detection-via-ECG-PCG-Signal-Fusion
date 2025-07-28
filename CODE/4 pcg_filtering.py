import scipy.io
from scipy import signal
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

"""loading and filtering pcg signals"""

pcg_path=r"E:\MAIN PROJECT\FILTERD CODES\base data\PCG ECG common\PCG_full"
for file_name in os.listdir(pcg_path):
    if file_name.endswith(".mat"):

      # Construct the full file path
      file_path = os.path.join(pcg_path, file_name)


      # Load data from the current .mat file
      loaded_data = scipy.io.loadmat(file_path)
      pcg_data = loaded_data['pcg_data']
      pcg_data = pcg_data.transpose()

      # Define the lower and upper cutoff frequencies for the bandpass filter (in Hz)
      lower_cutoff = 25
      upper_cutoff = 400
      sampling_freq=2000

      # Normalize the cutoff frequencies with respect to the Nyquist frequency
      normalized_lower_cutoff = lower_cutoff / (0.5 * sampling_freq)
      normalized_upper_cutoff = upper_cutoff / (0.5 * sampling_freq)

      # Design a bandpass Butterworth filter
      b, a = signal.butter(4, [normalized_lower_cutoff, normalized_upper_cutoff], btype='band')

      # Apply the filter to the PCG signal
      filtered_pcg_signal = signal.filtfilt(b, a, pcg_data)


      mat_file_path = f"E:\\MAIN PROJECT\\FILTERD CODES\\data splitting\\filtered data\\PCG_filtered\\{file_name}"
      # Convert the list to a dictionary with a variable name
      data_to_save = {'PCG_data': filtered_pcg_signal}

      # Save the data to a MATLAB .mat file
      scipy.io.savemat(mat_file_path, data_to_save)

print(filtered_pcg_signal.shape)
print(filtered_pcg_signal)

