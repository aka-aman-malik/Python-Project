import pandas as pd

df = pd.read_csv('E:/Data analytics/PYTHON/P7/olist_customers_dataset.csv/olist_customers_dataset.csv')

print(df.isna().sum())
df['customer_city']= df['customer_city'].str.upper()
print(df['customer_city'].head())

df_clean = df.drop(columns=['customer_id'])
print(df_clean.head())

df_clean.to_csv('E:/Data analytics/PYTHON/P7/cleaned_customers_dataset.csv', index=False)



