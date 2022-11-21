num = int(input("Enter a number:  "))
for i in range(8):
    if num % 2 == 0:
        print('0')
    else:
        print('1')
    num = num / 2
    if num < 1:
        break