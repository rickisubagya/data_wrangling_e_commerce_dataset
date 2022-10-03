import numpy as np
import pandas as pd

def read_data_csv(PATH):
    '''
    Read data from dataset from path with encoding type
    
    Parameters
    ----------
    PATH : str
        path source of cleaning data, csv.
        
    ENCODING_TYPE : str
        encoding type
    
    Returns
    -------
    data : pd.DataFrame
        Data to cleaning
    '''
    data = pd.read_csv(PATH)
        
    return data
    
def read_and_check_data_csv(path):
    '''
    Read data
    '''
    print('Start import data')
    df = read_data_csv(path)
    print('Done import data')
    
    return df