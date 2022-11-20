num=int(input("Enter a number:  "))
if num<=1000 and num<10000:
    print('Invalid Value...\nPlease Restart the program')
    exit()
Thousands=num//1000
Hundreds=((num//100)%10)
Tens=((num//10)%10)
Ones=num%10
print("Thousands = "+str(Thousands) +'\n'+"Hundreds = "+str(Hundreds)+'\n'+"Tens = "+str(Tens)+'\n'+"Ahadot = "+str(Ones))