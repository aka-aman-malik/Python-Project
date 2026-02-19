import pandas as pd

df= pd.read_csv('E:/Data analytics/PYTHON/P7/olist_order_payments_dataset.csv/olist_order_payments_dataset.csv')

df = df.drop(columns=['payment_sequential'])
print(df.head())

df.to_csv('E:/Data analytics/PYTHON/P7/cleaned_order_payments_dataset.csv', index=False)