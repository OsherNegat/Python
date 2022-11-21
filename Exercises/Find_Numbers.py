def value(string):
    list = []
    for i in range(len(string)):
        if string[i].isdigit():
            list.append(string[i])
    print("The numbers in the string are:  " + str(list))
    return any(char.isdigit()for char in string)

string = input("Enter a string:  ")
print(value(string))