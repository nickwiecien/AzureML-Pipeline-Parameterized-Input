from azureml.core import Run, Workspace, Datastore, Dataset
from azureml.data.datapath import DataPath
import pandas as pd
import os
import argparse


#Parse input arguments
parser = argparse.ArgumentParser("Register Uploaded File Data")
parser.add_argument('--uploaded_file_path_param', type=str, required=True)
parser.add_argument('--uploaded_file_dataset', dest='uploaded_file_dataset', required=True)


args, _ = parser.parse_known_args()
uploaded_file_path_param = args.uploaded_file_path_param
uploaded_file_dataset = args.uploaded_file_dataset

#Get current run
current_run = Run.get_context()

#Get associated AML workspace
ws = current_run.experiment.workspace

#Get default datastore
ds = ws.get_default_datastore()

#Get temporary directory
tempdir = './tmp'
os.makedirs(tempdir, exist_ok=True)

#Download files to tempory directory
ds.download(tempdir, prefix=uploaded_file_path_param)

#Get files in flat structure
files = []
for dirpath, dirnames, filenames in os.walk(tempdir):
    for filename in [f for f in filenames]:
        files.append(os.path.join(dirpath, filename))

#Assume uploaded file is a CSV
csv_file_path = [x for x in files if x.endswith('.csv')][0]

print(csv_file_path)

#Read file data into pandas dataframe
file_df = pd.read_csv(csv_file_path)

#Make directory on mounted storage
os.makedirs(uploaded_file_dataset, exist_ok=True)

#Upload modified dataframe
file_df.to_csv(os.path.join(uploaded_file_dataset, 'uploaded_file_data.csv'), index=False)

