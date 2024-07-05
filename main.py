import pandas as pd
1
# data = [1, 2, 3, 4, 5]
# series = pd.Series(data)
# print(series)
2
# data = {
#     'Name' : ['Alice', 'Bob', 'Roma', 'Anna'],
#     'Age' : [23, 45, 17, 24],
#     'City' : ['New York', 'LA', 'Chicago', 'Moskow']
# }
#
# df = pd.DataFrame(data)
# print(df)

df = pd.read_csv('World-happiness-report-2024.csv')
print(df.loc[56])