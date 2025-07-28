import scipy.io
from scipy import signal
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

"""loading and filtering ecg files"""

ecg_path=r"E:\MAIN PROJECT\FILTERD CODES\base data\PCG ECG common\ECG_full"
for file_name in os.listdir(ecg_path):
    if file_name.endswith(".mat"):

      # Construct the full file path
      file_path = os.path.join(ecg_path, file_name)

      # Load data from the current .mat file
      loaded_data = scipy.io.loadmat(file_path)
      ecg_data = loaded_data['data']
      ecg_data = ecg_data.transpose()

      # Sampling frequency of the ECG signal (in Hz)
      sampling_freq = 2000

      # Define the cutoff frequency for the low-pass filter (in Hz)
      cutoff_freq = 20

      # Normalize the cutoff frequency with respect to the Nyquist frequency
      normalized_cutoff_freq = cutoff_freq / (0.5 * sampling_freq)

      # Design a low-pass Butterworth filter
      b, a = signal.butter(4, normalized_cutoff_freq, btype='low')

      # Apply the filter to the ECG signal
      filtered_ecg_signal = signal.filtfilt(b, a, ecg_data)

      mat_file_path = f"E:\\MAIN PROJECT\\FILTERD CODES\\data splitting\\filtered data\\ECG_filtered\\{file_name}"
      # Convert the list to a dictionary with a variable name
      data_to_save = {'ECG_data': filtered_ecg_signal}

      # Save the data to a MATLAB .mat file
      scipy.io.savemat(mat_file_path, data_to_save)

print(ecg_data.shape)
print(len(ecg_data[0]))



