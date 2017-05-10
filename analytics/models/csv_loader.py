import pandas as pd
from .settings import file_names, column_rename
from ..helpers import dataset_helper


def load_dataset(site_name, survey_type, columns):
    dataset = pd.read_csv(file_names[site_name][survey_type])
    dataset = trim_heading_rows(dataset=dataset, rows=2)
    # dataset = get_dataset_columns(dataset=dataset, columns=dataset)
    # return dataset
    return dataset


def trim_heading_rows(dataset, rows):
    if len(dataset) < rows:
        raise Exception('Dataset length is less then the number of rows to remove')
    return dataset[rows:]


def fetch_original_column_names(site_name, survey_type, columns):
    columns_set = column_rename[site_name][survey_type]
    return {key: val for key, val in columns_set.items() if val in columns}


# def get_dataset_columns(dataset, columns):
#     return 1