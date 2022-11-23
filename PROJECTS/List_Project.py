my_list = []
for i in range(4):
    if i == 0:
        my_list.append(input("Enter your full name:  "))
    elif i == 1:
        my_list.append(input("Enter your age:  "))
    elif i == 2:
        my_list.append(input("Enter your mail:  "))
    elif i == 3:
        my_list.append(input("Enter your phone number:  "))
print("Your personal list is:  " + str(my_list))

ip = []
for i in range(2):
    ip.append(input("\nEnter IP address:  "))
print("Your ip addresses are:  " + str(ip))

for i in range(3):
    ip.append(input("Enter additional IP Address:  "))
print("Additional IP Addresses:  " + str(ip))

ip.pop(2)
print("We have " + str(len(ip)) + " IP's:")
print(ip)
