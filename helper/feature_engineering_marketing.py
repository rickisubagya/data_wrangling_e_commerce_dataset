import numpy as np
import pandas as pd
from helper.constant import seg_map


def feature_engineering_marketing(df7):
    
    marketing = df7
    
    # Convert into datetime format
    marketing['Year_Birth'] = pd.to_datetime(marketing['Year_Birth'])
    marketing['Dt_Customer'] = pd.to_datetime(marketing['Dt_Customer'])
    marketing['Year_Birth'] = marketing['Year_Birth'].dt.strftime('%Y')
    
    # Rename column Income
    marketing = marketing.rename(columns={marketing.columns[4]:'Income'})
    
    # Input missing value with median
    marketing['Income'] = marketing['Income'].str.replace('$', '', regex=True).str.replace(',', '', regex=True).str.replace('.', '', regex=True).astype('float')/100
    median_income = round(marketing['Income'].median(), 0)
    marketing['Income'] = marketing['Income'].fillna(median_income)
    
    # RFM Segmentation
    marketing['Monetary'] = marketing[['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts']].sum(axis=1)
    marketing['Recency_Rating'] = pd.cut(marketing['Recency'],
                                         5,
                                         labels=[5, 4, 3, 2, 1])
    marketing['Monetary_Rating'] = pd.cut(marketing['Monetary'],
                                          5,
                                          labels=[1, 2, 3, 4, 5])
    marketing['Frequency_Rating'] = pd.cut(marketing['NumWebPurchases'],
                                           5,
                                           labels=[1, 2, 3, 4, 5])
    marketing['Segment'] = (marketing['Recency_Rating'].astype(str) + marketing['Frequency_Rating'].astype(str)).replace(seg_map, regex=True)
    
    return marketing