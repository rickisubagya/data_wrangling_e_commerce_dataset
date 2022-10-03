PATH1 = 'Documents/Github/data_wrangling_e_commerce_dataset/data/olist_customers_dataset.csv'
PATH2 = 'Documents/Github/data_wrangling_e_commerce_dataset/data/olist_orders_dataset.csv'
PATH3 = 'Documents/Github/data_wrangling_e_commerce_dataset/data/olist_order_reviews_dataset.csv'
PATH4 = 'Documents/Github/data_wrangling_e_commerce_dataset/data/olist_order_items_dataset.csv'
PATH5 = 'Documents/Github/data_wrangling_e_commerce_dataset/data/olist_products_dataset.csv'
PATH6 = 'Documents/Github/data_wrangling_e_commerce_dataset/data/olist_sellers_dataset.csv'
PATH7 = 'Documents/Github/data_wrangling_e_commerce_dataset/data/marketing_data.xlsx'
PATH8 = 'Documents/Github/data_wrangling_e_commerce_dataset/data/ab.csv'

seg_map = {
    r'[1-2][1-2]': 'Hibernating',
    r'[1-2][3-4]': 'At Risk',
    r'[1-2]5': 'Can\'t Loose',
    r'3[1-2]': 'About to Sleep',
    r'33': 'Need Attention',
    r'[3-4][4-5]': 'Loyal Customers',
    r'41': 'Promising',
    r'51': 'New Customers',
    r'[4-5][2-3]': 'Potential Loyalists',
    r'5[4-5]': 'Champions'
}