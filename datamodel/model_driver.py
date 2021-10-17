from datacleanser import cleanseData
from multiclass_model import generateSaveModel

# This is not a right approach but as this is not a production based code, going with simple if conditions
## Ideal approach can be through properties file with profile settings like profile==prod or profile=local

input_data_set      = "file:///datavol/raw/newsfeeds/*.csv"
cleansed_output_dir = "file:///datavol/cleansed/"
model_output_dir    = "file:///datavol/trained/"

if __name__ == "__main__":
    cleanseData(input_data_set,cleansed_output_dir)
    generateSaveModel(cleansed_output_dir,model_output_dir)