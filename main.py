from cal import add


# importing add function only
print(add(1, 3))


# variables
# multiple assignments
x = y = z = 1
sa, sb, sc = 1, 2, "name"
print(sa)

# to delete reference
del sa, x

# splice
x = "hello"
print(x.upper())
print(dir("string"))
print(x[0])
print(x.replace('h', 'w'))
print(x[1:4])

# string formatting
age = 32
name = "alex".upper()
print(f"my name is {age} and my age is {name}")
print("my name is {} and my age is {}".format(name, age))


# list
list1 = [1, 2, 3, 4]
for i in list1:
    print(i)


# tuple (can not be change or manipulated)
x = (1, 2, 3, "red", "yellow")
print("Tuple " + str(x[-1]))


# dictionary
dic = {"number": 123, "name": "someone", "age": 100}
dic["new_value"] = "value"
print("dictionary " + str(dic["number"]) + " " + dic["new_value"])


# booleans
if 5 <= 6:
    print("true")


# arrays
colors = ["red", "yellow", "blue"]
print(colors[1])
print(len(colors))
print(colors.pop())
print(colors.append("black"))
print(colors)
colors.remove("black")
print(colors)

# Operators are the constructs, which can manipulate the value of operands.
# Consider the expression 4 + 5 = 9. Here, 4 and 5 are called operands and + is
# called the operator.
# operations: +, -, /, *, **, //, %
print(2 % 2)
print(2 ** 4)


# assignments operations: =, +=, -=, *=, /=, %=, **=, //=
x = 1
x += 10
print(x)


# comparison operators: ==, !=, >, >=, <, <=
x = 1
print(x == 2)


# logical operators: and, or, not
print(3 > 2 and 5 > 3)
print(not 1 > 2)


# identity operation: is, is not
print(x is x)


# membership operators: in, not in
x = [1, 2, 3]
print(4 not in x)


# methods
def say_hello(name):
    print(name)


def addNumber(num1, num2=0):
    return num1 + num2


say_hello("your name")
print(addNumber(1, 2))


# inout
x = input("write number (x): ")
y = input("write number (y): ")
print(x + ", " + y)


# convectors
c = input("input temp")
c = int(c)
f = (9/5) * c + 32
print(f)


# method parameters
a = input("input for a: ")
b = input("input for b: ")
a = int(a)
b = int(b)
print(addNumber(a, b))
print(addNumber(1))


# common errors: syntax errors, indentation error, type error, name error,
# zero division error, index error, attribute error,
# handling errors and internet

# conditions
x = 3
y = 4
if x == y:
    print("x and y is equal")
elif x <= y or x == 3:
    print("x is less than y")
else:
    print("wrong")

# nested
if x == 2:
    if y == 2:
        print("all equal")
else:
    print("not equal to x")

# loops: for, while, range()
x = [1, 2, 3, 4, 5]
for item in x:
    print(item)

x = 0
while x <= 10:
    print(x)
    x += 1

colors = ["yellow", "blue", "black"]
for color in colors:
    print(color)
    if color == "blue":
        break

for color in colors:
    if color == "blue":
        continue
    print(color)

for x in range(10, 100, 10):
    print(x)

for x in range(1, 100, 1):
    if x == 10:
        print(f"value found: {x}")

names = ["name1", "name2", "name3"]
objects = ["object1", "object2", "object3"]
for name in names:
    for object in objects:
        print(f"{name}, {object}")
