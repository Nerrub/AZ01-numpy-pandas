import pandas as pd

# df = pd.read_csv('hh.csv')
#
# df['Test'] = [new for new in range (29)]
#
# print(df)
#
# df.drop(28, axis = 0, inplace=True)
#
# print(df)

df = pd.read_csv('animal.csv')
print(df)

# df.fillna(0, inplace=True)
# print(df)
#
# df.dropna(inplace=True)
# print(df)

group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
print(group)