# AzureML-Pipeline-Parameterized-Input

Sample Azure Machine Learning pipeline demonstrating how to register and process a file dataset using parameterized pipeline arguments.

This pipeline accepts one variable argument in the form of a `PipelineParameter` which is used to specify the location of a file present in an Azure Machine Learning datastore to be processed. This sample is one piece of a larger solution where a file of interest is automatically moved from Azure Blob Storage into an AML Datastore via Azure Data Factory which can also be used to trigger the pipeline execution.

![AML Pipeline](img/adfaml.png?raw=true "AzureML-Pipeline-Parameterized-Input")

## Environment Setup
<b>Note:</b> Recommend running this notebook using an Azure Machine Learning compute instance using the preconfigured `Python 3.6 - AzureML` environment.

To build and run the sample pipeline contained in `SamplePipeline.ipynb` the following resources are required:
* Azure Machine Learning Workspace
