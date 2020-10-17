# opening and reading file
file = open("./file.text", "r")
x = file.read()
print(x)


# writing file
w = open("writefile.txt", "w")
w.write("test\nnew line")
w.close()


w = open("writefilecolors.txt", "w")
items = ["red", "white", "black"]
for item in items:
    w.write(item + "\n")
w.close()


# appending to file
w = open("writefile.txt", "a")
w.write("\nother")
w.close()
