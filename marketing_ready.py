import pandas as pd

from helper.data_check_preparation_excel import read_and_check_data_excel
from helper.feature_engineering_marketing import feature_engineering_marketing
from helper.constant import PATH7

def clean_data():
    # read and check data
    df7 = read_and_check_data_excel(PATH7)
    
    # feature engineering
    print('Start claning data')
    marketing_ready = feature_engineering_marketing(df7)
    print('Done cleaning data\nStart saving result cleaning data')
    marketing_ready.to_excel('Documents/Github/data_wrangling_e_commerce_dataset/artefacts/marketing_ready.xlsx', index=False)
    
if __name__=="__main__":
    print('START RUNNING PIPELINE!')
    clean_data()
    print('FINISH RUNNING PIPELINE!')