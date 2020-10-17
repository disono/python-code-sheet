import numpy as np
from matplotlib import pyplot as plt

x = [[[1, 2], [3, 4], [5, 6], [6, 7]], [[1, 2], [3, 4], [5, 6], [6, 7]]]
y = np.array(x)

print(y)

a = [1, 2, 3, 4, 5, 6]
b = [[1, 2], [3, 4], [5, 6], [6, 7]]
a = np.array(a)
b = np.array(b)
print(b)
print(np.zeros((100, 1, 7)) -5)
print(np.ones((1, 2)))
print(np.eye(4, 3, 1))

ar = np.arange(50).reshape(5, 10)
print(ar)

linear = np.linspace(0, 10, 3)
print(linear)

# slicing
li = np.arange(1, 100)
print(li[-20:-2])

ma = np.arange(25).reshape(5,5)
print(ma)
print(ma[0][4])
print(ma[0, 4])
print(ma[0:2, 2:4])

# conditional selection
print(ma[ma > 10])

# operations
c = np.arange(10)
d = np.arange(10, 20)
print(c + d)

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x = arr[(arr % 2) == 1]
print(x)

# polyfit
x = np. array([1, 3, 5, 7])
y = np. array([6, 3, 9, 5])
m, b = np. polyfit(x, y, 1) # m = slope, b = intercept.
print(m, b)
plt.plot(x, y, 'o') # create scatter plot.
plt.plot(x, m * x + b) # add line of best fit.
plt.show()
