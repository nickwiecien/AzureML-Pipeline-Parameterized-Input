from azureml.core import Run, Workspace, Datastore, Dataset
from azureml.data.datapath import DataPath
import pandas as pd
import numpy as np
import os
import argparse

#Parse Input Arguments
parser = argparse.ArgumentParser("Process Data")
parser.add_argument("--processed_dataset", dest='processed_dataset', required=True)
args, _ = parser.parse_known_args()
processed_dataset = args.processed_dataset

#Get current run and AML workspace
current_run = Run.get_context()
ws = current_run.experiment.workspace

#Get uploaded dataframe
uploaded_file_dataset = current_run.input_datasets['uploaded_data']
uploaded_file_df = uploaded_file_dataset.to_pandas_dataframe()

#ML operations here
uploaded_file_df['NewColumn'] = np.array(len(uploaded_file_df) * ['Hello world'])

#Create output directory for processed dataset
os.makedirs(processed_dataset, exist_ok=True)

#Save transformed dataframe to datastore location
uploaded_file_df.to_csv(os.path.join(processed_dataset, 'processed_dataset.csv'), index=False)

