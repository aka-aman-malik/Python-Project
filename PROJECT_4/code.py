import pandas as pd

df = pd.read_csv('E:/Data analytics/PYTHON/P6/googleplaystore.csv/googleplaystore.csv')
print(df.head())
print(df.columns)

df['Installs'] = df['Installs'].str.replace('+', '', regex=False).str.replace(',', '', regex=False)
df['Installs']= pd.to_numeric(df['Installs'], errors='coerce')
print(df['Installs'].head())
print(df['Installs'].dtype)

print(df['Size'].head())
df['Size'] = df['Size'].str.replace('M', '', regex=False).str.replace('k', '', regex=False)
df['Size'] = pd.to_numeric(df['Size'], errors='coerce')
print(df['Size'].head())
print(df['Size'].dtype)

df['Price'] = df['Price'].str.replace('$', '', regex=False)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
print(df['Price'].head())
print(df['Price'].dtype)
