import pandas as pd

df = pd.read_csv('CVS_Health.csv')

print(df.head())
print(df.info())
print(df.describe())