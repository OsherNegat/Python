my_list = []
name = input("Enter your full name:  ")
age = input("Enter your age:  ")
mail = input("Enter your mail:  ")
phone = input("Enter your phone number:  ")
my_list.append(name)
my_list.append(age)
my_list.append(mail)
my_list.append(phone)
print("Your personal list is:  " + str(my_list))
ip = []
for i in range(2):
    ip_a = input("Enter IP address:  ")
    ip.append(ip_a)
print("Your ip addresses are:  " + str(ip))
for i in range(3):
    ip_b = input("Enter additional IP Address:  ")
    ip.append(ip_b)
print("Additional IP Addresses:  " + str(ip))
ip.pop(2)
print("We have " + str(len(ip)) + " IP's:")
print(ip)
