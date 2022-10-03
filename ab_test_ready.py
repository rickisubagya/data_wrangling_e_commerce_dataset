import pandas as pd

from helper.data_check_preparation_csv import read_and_check_data_csv
from helper.feature_engineering_ab import feature_engineering_ab
from helper.constant import PATH8

def clean_data():
    # read and check data
    df8 = read_and_check_data_csv(PATH8)
    
    # feature engineering
    print('Start claning data')
    ab_test_ready = feature_engineering_ab(df8)
    print('Done cleaning data\nStart saving result cleaning data')
    ab_test_ready.to_excel('Documents/Github/data_wrangling_e_commerce_dataset/artefacts/ab_test_ready.xlsx', index=False)
    
if __name__=="__main__":
    print('START RUNNING PIPELINE!')
    clean_data()
    print('FINISH RUNNING PIPELINE!')