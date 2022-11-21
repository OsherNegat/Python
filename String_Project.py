name = input("Enter your full name:  ")
mail = input("Enter your mail:  ")
age = int(input("Enter your age:  "))
print("\n\nYour full name is:  " + name + "\nYour mail address is:  " + mail + "\nYour age is:  " + str(age))
print("Reversed name:  " + name[::-1] + "\nYour age multiplied by 3:  " + str(age*3))
names = "idan ben dudu yuval avi benny gadi gal yael shahar osher"
print(name in names)
