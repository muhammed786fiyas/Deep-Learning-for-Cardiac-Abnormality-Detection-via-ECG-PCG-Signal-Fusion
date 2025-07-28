import csv

# Read values from the first CSV file
values_file_path = r'E:\MAIN PROJECT\FILTERD CODES\data splitting\splitted data\split_no.csv'
labels = []

with open(values_file_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        for i in range(int(row[1])):
            labels.append(row[2])


# CSV file path
csv_file = r'E:\MAIN PROJECT\FILTERD CODES\data splitting\splitted data\label.csv'

# Open the CSV file in append mode
with open(csv_file, 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    
    # Write the labels list to the CSV file
    for i in range (len(labels)):
        if (labels[i]=='-1'):
            writer.writerow('0')
        else:
            writer.writerow('1')


print(len(labels))