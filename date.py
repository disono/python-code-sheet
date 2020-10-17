import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print("Day: " + x.strftime("%A") + ", " + x.strftime("%a"))
