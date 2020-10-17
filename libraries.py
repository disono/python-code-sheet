import numpy as np
import matplotlib.pyplot as plt
from cal import add
import json

x = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(x)

a = np.array(x)
print(a)

# %matplotlib inline
x = np.linspace(0, 10, 100)
y = x ** 2
plt.plot(x, y)

# from cal import add
print(add(1, 3))

# json
x = {"name": "Name 1"}
y = json.dumps(x)
print(y)
