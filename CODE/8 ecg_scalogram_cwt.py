import scipy.io
import os
import numpy as np
import matplotlib.pyplot as plt
import pywt
from PIL import Image

# Directory containing your ECG signal files
ecg_dir = r"E:\MAIN PROJECT\FILTERD CODES\data splitting\splitted data\ECG_split"

# Create a directory to save the CWT results
output_dir = r"E:\MAIN PROJECT\FILTERD CODES\data splitting\scalogram data\ECG_scalogram"
os.makedirs(output_dir, exist_ok=True)

sampling_rate = 2000  # Sampling rate of the PCG signal (in Hz)
scaling_parameter_range = (20, 500)  # Range of scaling parameter for Morlet wavelet
mother_wavelet = 'cmor1.5-1.0'  # Morlet wavelet
scales = np.arange(*scaling_parameter_range)

for filename in os.listdir(ecg_dir):
    if filename.endswith(".mat"):  # Assuming ECG signals are in .mat format
        file_path = os.path.join(ecg_dir, filename)
        
        # Load the ECG signal from the .mat file
        ecg_data = scipy.io.loadmat(file_path)
        ecg_signal = ecg_data['ECG_data'].flatten()  # Adjust the key based on your .mat structure

        coefficients, frequencies = pywt.cwt(ecg_signal, scales, mother_wavelet, sampling_period=1/sampling_rate)

        # Plot the scalogram
        plt.figure(figsize=(10, 6))
        plt.imshow(np.abs(coefficients), extent=[0, len(ecg_signal), frequencies[-1], frequencies[0]], cmap='jet', aspect='auto')

        # Save the scalogram image
        image_output_path = os.path.join(output_dir, f'{filename[:-4]}.png')
        plt.savefig(image_output_path, bbox_inches='tight')  # Save the scalogram image
        plt.close()