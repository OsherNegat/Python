def func(list):
    sum_digits = 0
    for num in list:
        length = len(str(num))
        while num > 0:
            sum_digits += (num % 10)  #
            num //= 10
        print("The length is: " + str(length) + "\nThe sum is:  " + str(sum_digits))
        sum_digits = 0
    return 0

list = []
num = int(input("Enter a number:  "))
while num >= 0:
    list.append(num)
    num = int(input("Enter a number:  "))
print(list)
func(list)