num = int(input('Enter a number: '))
list = []
while num > 0:
    if num % 2 == 0:  # Checks if the number has remainder
        list.append("0")
    else:
        list.append("1")
    num //= 2
    if num < 1:
        break
print(str(list))