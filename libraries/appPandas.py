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
df['P'] = df['Y'] + df['Z']
print(df)
# drop row
df.drop('e', inplace = True)
print(df)
# drop column
df.drop('Z', axis = 1, inplace = True)
print(df)
# accessing dataframes
print(df['Y'])
print(df.loc['a'])
print(df.iloc[1])
print(df.loc['a', 'Y'])
# conditional
print(df[df['W'] > 3]['W'])
print(df[(df['W'] > 3) & (df['Y'] > 3)])
print(df[(df['W'] > 3) | (df['Y'] > 1)])
