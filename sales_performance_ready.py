import pandas as pd

from helper.data_check_preparation_csv import read_and_check_data_csv
from helper.feature_engineering_sales_performance import feature_engineering_sales_performance
from helper.constant import PATH1, PATH2, PATH3, PATH4, PATH5, PATH6

def clean_data():
    # read and check data
    df1 = read_and_check_data_csv(PATH1)
    df2 = read_and_check_data_csv(PATH2)
    df3 = read_and_check_data_csv(PATH3)
    df4 = read_and_check_data_csv(PATH4)
    df5 = read_and_check_data_csv(PATH5)
    df6 = read_and_check_data_csv(PATH6)
    
    # feature engineering
    print('Start claning data')
    sales_performance_ready = feature_engineering_sales_performance(df1, df2, df3, df4, df5, df6)
    print('Done cleaning data\nStart saving result cleaning data')
    sales_performance_ready.to_excel('Documents/Github/data_wrangling_e_commerce_dataset/artefacts/sales_performance_ready.xlsx', index=False)
    
if __name__=="__main__":
    print('START RUNNING PIPELINE!')
    clean_data()
    print('FINISH RUNNING PIPELINE!')