import numpy as np
import pandas as pd

x = ['a', 'b', 'c', 'd', 'e']
x2 = ['a', 'b', 'c', 'd', 'e']
y = [1, 2, 3, 4, 5]
z = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

s = pd.Series(y, x)
s2 = pd.Series(x2)
print(s[:'b'])

# dataframes
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [9, 0, 1, 2]
d = [3, 4, 5, 6]
e = [7, 8, 9, 0]
df = pd.DataFrame([a, b, c, d, e], ['a', 'b', 'c', 'd', 'e'], ['W', 'X', 'Y', 'Z'])
print(df)
# add new column
print('Add column')
df['P'] = df['Y'] + df['Z']
print(df)
# drop row
print('Drop row')
df.drop('e', inplace = True)
print(df)
# drop column
print('Drop Column')
df.drop('Z', axis = 1, inplace = True)
print(df)
# accessing dataframes
print('Accessing Dataframes')
print(df['Y'])
print(df.loc['a'])
print(df.iloc[1])
print(df.loc['a', 'Y'])
# conditional
print('Conditional')
print(df[df['W'] > 3]['W'])
print(df[(df['W'] > 3) & (df['Y'] > 3)])
print(df[(df['W'] > 3) | (df['Y'] > 1)])
# missing data
print('Missing Data')
d = {'a': [1,2,3], 'b': [2,3,np.nan], 'c': [3,np.nan,np.nan]}
df = pd.DataFrame(d)
# df = df.dropna(thresh = 3) # drop with threshold, greater thant 3 data
# df = df.fillna(1); # fill missing data with 1 or any number
df = df['b'].fillna(value = df['b'].mean())
print(df)
# grouping
print('Grouping')
p = {'items': ['apple', 'orange', 'grapes', 'apple'], 'days': ['mon', 'tue', 'wed', 'thur'], 'sales': [100, 30, 50, 10]}
df = pd.DataFrame(p)
x = df.groupby('items')
#print(x.mean())
#print(x.count())
print(x.describe().transpose())
