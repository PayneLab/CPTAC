#   Copyright 2018 Samuel Payne sam_payne@byu.edu
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import pandas as pd

def unionize_indicies(dataset):
    """Return a union of all indicies in a dataset, without duplicates.

    Parameters:
    dataset (dict of str: pandas DataFrame): The data dictionary containing the dataset.

    Returns:
    pandas Index: Union of all indicies in the dataset, without duplicates.
    """
    indicies = [df.index for df in dataset.values()]
    master_index = pd.Index([])
    for index in indicies:
        master_index = master_index.union(index)
        master_index = master_index.drop_duplicates()
    return master_index

def add_sample_status_col(df, tumor_test)
    """Add a Sample_Status column to a dataframe.

    Parameters:
    df (pandas DataFrame): The dataframe to add Sample_Status column to.
    tumor_test (function): A function that takes a given Patient_ID and returns a bool indicating whether it corresponds to a tumor sample.

    Returns:
    pandas DataFrame: A copy of df, with the Sample_Status column inserted.
    """

def generate_sample_id_map(master_index):
    """Generate sample ids for all samples in a dataset, and map them to the existing index.

    Parameters:
    master_index (pandas Index): Union of all the indicies in the dataset, without duplicates.

    Returns:
    dict: A dictionary with the old index values as the keys, and their corresponding sample ids as the values.
    """
    sample_id_dict = {}
    for i in range(len(master_index)):
        patient_id = master_index[i]
        sample_id_dict[patient_id] = "S{:0>3}".format(i + 1) # Use string formatter to give each sample id the format S*** filled with zeroes, e.g. S001, S023, or S112
    return sample_id_dict

def reindex_dataframe(df, reindex_map, new_index_name, keep_old): # This can reindex from Patient_ID to Sample_ID, and also reindex the renalccrcc transcriptomics dataframe
    """Reindex a dataframe based on a mapping of the old index values to new ones. Returns None if mapping fails.

    Parameters:
    df (pandas DataFrame): The dataframe to reindex.
    reindex_map (dict): A dictionary with the old index values as the keys, and the new ones as the values.
    new_index_name (str): The desired name for the new index.
    keep_old (bool): Whether to retain the old index in the dataframe as a column.

    Returns:
    pandas DataFrame: A copy of the given dataframe, with the new index. None if mapping failed.
    """
    df_name = df.name

    new_index = pd.Index(name=new_index_name)
    for row in df.index:
        if row in reindex_map.keys():
            new_index.append(reindex_map[row]) # TODO: Does this work?
        else:
            return None

    if keep_old:
        df = df.reset_index() # This gives the dataframe a default numerical index and makes the old index a column, preventing it from being dropped when we set the new index.
    df = df.reindex(new_index)
    df = df.sort_index()
    df.name = df_name
    return df

def unname_col_axes_in_dataset(dataset):
    """Set None for the name of all column axes of all dataframes in a dataset.

    Parameters:
    dataset (dict of str: pandas DataFrame): The dataset to unname the column axes of.

    Returns: None
    """