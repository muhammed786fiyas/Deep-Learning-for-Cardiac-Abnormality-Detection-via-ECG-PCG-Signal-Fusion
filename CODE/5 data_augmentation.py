import scipy.io
import numpy as np
import os
import csv

# Load .mat file
ecg_path = r"E:\MAIN PROJECT\FILTERD CODES\data splitting\filtered data\ECG_filtered"
pcg_path = r"E:\MAIN PROJECT\FILTERD CODES\data splitting\filtered data\PCG_filtered"

peak_dict={}
peak_no={}
n=1

for file_name_ecg in os.listdir(ecg_path):
    
    # Construct the full file path
    file_path_ecg = os.path.join(ecg_path, file_name_ecg)
    file_path_pcg = os.path.join(pcg_path, file_name_ecg)

    # Load data from the current .mat file
    loaded_data_ecg = scipy.io.loadmat(file_path_ecg)
    ecg_data = loaded_data_ecg['ECG_data']
    ecg_data = ecg_data.flatten()[500:]
    
    loaded_data_pcg = scipy.io.loadmat(file_path_pcg)
    pcg_data = loaded_data_pcg['PCG_data']
    pcg_data = pcg_data.flatten()[500:]


    peak_list=[]
    i=0
    k=0

    while(i+6000<len(ecg_data)):
        peak=np.argmax(ecg_data[i:i+2500])
        peak += i 
        peak_list.append(peak)

        ecg_data_divided=ecg_data[peak:peak+6000]
        pcg_data_divided=pcg_data[peak:peak+6000]

        ecg_data_path=f"E:\\MAIN PROJECT\FILTERD CODES\\data splitting\\splitted data\\ECG_split\\a{n:04d}.mat"
        pcg_data_path=f"E:\\MAIN PROJECT\FILTERD CODES\\data splitting\\splitted data\\PCG_split\\a{n:04d}.mat"
        
        ecg_data_to_save = {'ECG_data': ecg_data_divided}
        pcg_data_to_save = {'PCG_data': pcg_data_divided}
        
        # Save the data to a MATLAB .mat file
        scipy.io.savemat(ecg_data_path, ecg_data_to_save)
        scipy.io.savemat(pcg_data_path, pcg_data_to_save)


        i=peak+6000
        k+=1
        n+=1

    peak_dict[file_name_ecg[:5]]=peak_list
    peak_no[file_name_ecg[:5]]=k

print(peak_dict)
print(peak_no)


# Define the CSV file path
csv_file_path_split_no = r"E:\MAIN PROJECT\FILTERD CODES\data splitting\splitted data\split_no.csv"

# Write the dictionary to a CSV file
with open(csv_file_path_split_no, 'w', newline='') as csvfile:
    writer_split_no = csv.writer(csvfile)

    # Write header
    writer_split_no.writerow(['file_name', 'no_of_peaks'])

    # Write key-value pairs
    for key, value in peak_no.items():
        writer_split_no.writerow([key, value])

# Define the CSV file path
csv_file_path_split_peaks = r'E:\MAIN PROJECT\FILTERD CODES\data splitting\splitted data\split_peaks.csv'

# Write the dictionary to a CSV file
with open(csv_file_path_split_peaks, 'w', newline='') as csvfile:
    writer_split_peaks = csv.writer(csvfile)

    # Write header
    writer_split_peaks.writerow(['file_name', 'peak'])

    # Write key-value pairs
    for key, values in peak_dict.items():
        for value in values:
            writer_split_peaks.writerow([key, value])


