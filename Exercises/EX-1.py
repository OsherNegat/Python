def func(list):
    sum_digits = 0
    num_digits = 0



list = []
i=0
while i == 0:
    num = int(input("Enter a number:  "))
    if num < 0:
        print("The number isn't POSITIVE...\nResuming the Program....")
        break
    list.append(num)
print(list)
print(func(list))