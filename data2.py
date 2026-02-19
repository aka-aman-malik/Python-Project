import pandas as pd

df = pd.read_csv('E:/Data analytics/PYTHON/P7/olist_order_items_dataset.csv/olist_order_items_dataset.csv')


df= df.drop(columns=['order_item_id', 'product_id', 'seller_id'])
print(df.head())
print(df.info())
print(df.columns)

df['shipping_limit_date'] = pd.to_datetime(df['shipping_limit_date'])
print(df.info())
df.to_csv('E:/Data analytics/PYTHON/P7/cleaned_order_items_dataset.csv', index=False)