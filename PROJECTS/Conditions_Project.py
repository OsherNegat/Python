from time import sleep

print("Welcome to my MENU!"
      "\nPRESS 1 to triple a number\nPRESS 2 for Insert IP's to a list"
      "\nPRESS 3 to print DNS Dictionary\nPRESS 4 to Insert a string and check if it's Polindrom")
choose = int(input("Your choice:  "))
if 4 < choose or choose < 1:
    print("Invalid range, The program will exit now...")
    raise SystemExit

if choose == 1:
    num = int(input("Enter a number:  "))
    print(num**3)

elif choose == 2:
    IP = []
    for i in range(4):
        IP.append(input("Enter an IP ADDRESS:  "))
    print("The IP's are:  " + str(IP))

elif choose == 3:
    DNS_dict = {}
    for i in range(4):
        DNS_dict.update({input('Enter a URL:  ') : input('Enter IP ADDRESS:  ')})
    print("There are " + str(len(DNS_dict)) + " Entries\n" + "Printing....\n" + str(DNS_dict))

else:
    str = input("Enter a string:  ")
    if str == str[::-1]:  # CHECKS IF THE STRING IS EQUALS TO THE REVERSED STRING
        print(True)
    else:
        print(False)