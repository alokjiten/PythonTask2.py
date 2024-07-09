import pandas as pd

data = pd.read_csv('/Users/mrunalikale/Downloads//task2.csv')

print(type(data))

data.info
print(data)

data.describe() 
print(data)

data = data.drop_duplicates()
print(data)

data.isnull()
print(data)

data.isnull().sum()
print(data)

data.notnull()
print(data)

data.isnull().sum().sum()
print(data)

data2 = data.fillna(value=0)
print(data2)

data2.isnull().sum().sum()
print(data2)

data3 = data.fillna(method='pad') #forward filling
print(data3)

data4 = data.fillna(method='bfill') #backward filling
print(data4)
