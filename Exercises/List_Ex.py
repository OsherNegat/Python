steps = int(input("Enter number of steps:  "))
list = [4,5,6,7,8,9,0]
list = list[steps:] + list[:steps]
print(list)