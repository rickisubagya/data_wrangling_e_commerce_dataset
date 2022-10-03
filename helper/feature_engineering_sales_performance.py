import numpy as np
import pandas as pd


def feature_engineering_sales_performance(df1, df2, df3, df4, df5, df6):
    
    customers = df1
    orders = df2
    order_review = df3
    order_items = df4
    products = df5
    sellers = df6
    # Convert into datetime format
    orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
    orders['order_approved_at'] = pd.to_datetime(orders['order_approved_at'])
    orders['order_delivered_carrier_date'] = pd.to_datetime(orders['order_delivered_carrier_date'])
    orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
    orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])
    
    # Sort order_purchase_timestamp by ascending
    orders = df2.sort_values('order_purchase_timestamp').reset_index(drop=True)
    
    # Create column year_order_purchase
    orders['year_order_purchase'] = orders['order_purchase_timestamp'].dt.year
    
    # Input missing value with ffill method
    orders = orders.fillna(method='ffill', axis=1)
    
    # Merge Orders and Customers dataset
    sales_performance = pd.merge(customers, orders, how='inner',  on='customer_id')
    
    # Input missing value with ffill method
    order_review = order_review.fillna('unknown')
    
    # Convert into datetime format
    order_review['review_creation_date'] = pd.to_datetime(order_review['review_creation_date'])
    order_review['review_answer_timestamp'] = pd.to_datetime(order_review['review_answer_timestamp'])
    
    # Merge Orders, Customers, and Order Review dataset
    sales_performance = pd.merge(sales_performance, order_review, how='inner', on='order_id')
    
    # Convert into datetime format
    order_items['shipping_limit_date'] = pd.to_datetime(order_items['shipping_limit_date'])
    
    # Merge Orders, Customers, Order Review, and Order Items dataset
    sales_performance = pd.merge(order_items, sales_performance, how='inner', on='order_id')
    
    # Input missing value with ffill method
    products = products.fillna('unknown')
    
    # Merge Orders, Customers, Order Review, Order Items, and Products dataset
    sales_performance = pd.merge(sales_performance, products, how='inner', on='product_id')
    
    # Merge Orders, Customers, Order Review, Order Items, and Sellers
    sales_performance = pd.merge(sales_performance, sellers, how='inner', on='seller_id')
    
    # Sort order_purchase_timestamp by ascending
    sales_performance = sales_performance.sort_values('order_purchase_timestamp')
    
    # Drop some row
    row_to_drop = sales_performance[sales_performance['order_purchase_timestamp'] >= '2018-09-01'].index.values[0]
    sales_performance = sales_performance.drop(index=row_to_drop)
    
    # Convert product category name value into titlecase
    sales_performance['product_category_name'] = sales_performance['product_category_name'].str.title()
    
    return sales_performance