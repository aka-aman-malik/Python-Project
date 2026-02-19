import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('E:\\Data analytics\\PYTHON\\P10\\Book1.csv')
print(df.head())

#print(df.isna().sum())
df = df.dropna()
print(df.isna().sum())
print(df.info())

#Survival Rate
df['alive'] = df['alive'].replace({'yes': 1, 'no': 0})
survival_rate = df['alive'].mean()*100
print(f"Overall Survival Rate: {survival_rate:.2f}%")

#survival rate by gender, passenger class, and age. Calculate mean, median, and count for relevant columns.
relation_of_survivals = df.groupby(['sex', 'pclass','age'])[['alive']].agg(['mean', 'median', 'count'])
print(relation_of_survivals)

#Create at least 3 simple visualizations (bar chart, histogram, count plot)
sns.histplot(df['age'], bins=20)
plt.show()

sns.countplot(x='pclass', data=df)
plt.show()

sns.barplot(x='sex', y='alive', data=df)
plt.show()

conclusions = """
1. The overall survival rate of passengers is approximately {survival_rate:.2f}%.
2. The survival rate varies significantly by gender, with females having a higher survival rate than males.
3. The survival rate also varies by passenger class, with first-class passengers having a higher survival rate than second and third-class passengers.
4. Age distribution shows that children had a higher survival rate compared to adults.
5. The data suggests that gender and passenger class were strong indicators of survival on the Titanic.
"""
print(conclusions)