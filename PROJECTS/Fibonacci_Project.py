fibo = []
lst_len = int(input("Enter length of list: "))
for i in range(lst_len):
    num = int(input("Enter numbers for list: "))
    fibo.append(num)

for i in range(len(fibo)):
    while i == 2:
        if fibo[i] != fibo[i-1] + fibo[i-2]:  # if this isn't true: break because this isn't fibo
            print("This isn't Fibo!")
            break
        else:
            print("This is Fibo!")
            break