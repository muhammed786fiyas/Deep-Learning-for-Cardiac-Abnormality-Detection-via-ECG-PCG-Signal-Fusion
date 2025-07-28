import csv
import os
import shutil

# Mapping dictionary for labels to directory names
label_mapping = {'0': 'normal', '1': 'abnormal'}

# CSV file path
csv_file = r"E:\MAIN PROJECT\FILTERD CODES\data_splitting_9000\scalogram data\label.csv"
# Directory containing data files
data_directory = r"E:\MAIN PROJECT\FILTERD CODES\data_splitting_9000\scalogram data\PCG_scalogram"
divided_directory= r"E:\MAIN PROJECT\FILTERD CODES\data_splitting_9000\scalogram data\PCG_scalogram_divided"

# Check if the CSV file exists
if os.path.exists(csv_file):   
    # Read the CSV file and extract labels and corresponding data file names
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            label = row['label']
            filename = row['file_name']
            
            # Create a directory for the label if it doesn't already exist
            label_directory = os.path.join(divided_directory, label_mapping[label])
            if not os.path.exists(label_directory):
                os.makedirs(label_directory)
            
            # Move or copy the data file to the directory corresponding to its label
            source_file = os.path.join(data_directory, filename+".png")
            destination_file = os.path.join(label_directory, filename+".png")
            # shutil.move(source_file, destination_file)  # Use this if you want to move the files
            shutil.copy(source_file, destination_file)  # Use this if you want to copy the files
else:
    print("CSV file does not exist.")
