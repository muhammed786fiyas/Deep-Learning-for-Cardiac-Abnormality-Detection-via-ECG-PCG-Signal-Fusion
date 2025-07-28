% Specify the folder path
folderPath = "E:\MAIN PROJECT\DATASET\physionet raw data\training-a";
save_path="E:\MAIN PROJECT\DATASET\matlab data\training a\PCG";
% Get a list of files in the folder
files = dir(fullfile(folderPath, '*.wav'));

% Loop through each file and load/save
for i = 1:length(files)
    % Construct the full file path
    filePath = fullfile(folderPath, files(i).name);
    
    % Load the data from the file
    [pcg_data,sampling_rate] = audioread(filePath);
    
    % Perform any processing or analysis on the data if needed
    
    % Save the processed data (e.g., as .mat file)
    [~, fileName, ~] = fileparts(files(i).name);
    save(fullfile(save_path, [fileName, '.mat']),'pcg_data');
end