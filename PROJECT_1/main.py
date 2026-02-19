import pandas as pd

df1= pd.read_csv('E:/Data analytics/PYTHON/P7/cleaned_customers_dataset.csv')
df2= pd.read_csv('E:/Data analytics/PYTHON/P7/cleaned_order_items_dataset.csv')
df3= pd.read_csv('E:/Data analytics/PYTHON/P7/cleaned_order_payments_dataset.csv')
merged_df = df2.merge(df3, on='order_id', how='outer')
print(merged_df.head())
print(df1.columns)
print(df2.columns)
print(df3.columns)
