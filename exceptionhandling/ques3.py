items = [10, 20, 30]
try:
    print(items[1])
   # print(items[4])
except IndexError:
    print("Index out of range.")
