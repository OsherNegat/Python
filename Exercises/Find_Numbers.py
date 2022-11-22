def value(string):
    list = []
    for i in range(len(string)):
        if string[i].isdigit():  # Check if the string in index i is Numeric Value
            list.append(string[i])  # Add the value to the list
    print("The numbers in the string are:  " + str(list))
    return any(char.isdigit()for char in string)  # Check every char in the string, if it's a digit return it

string = input("Enter a string:  ")
print(value(string))