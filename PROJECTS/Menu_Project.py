from random import randint
from time import sleep

while True:
    print("Welcome to our Menu!\nPress 1: To print 100 numbers\nPress 2: To check Fibonacci for a received list\n"
          "Press 3: Draw numbers until you get 12 or count 10 times\n")
    ans = int(input())
    if ans == 1:
        for num in range(100):
            print(num)
    elif ans == 2:
        fibo = []
        lst_len = int(input("Enter length of list: "))
        for i in range(lst_len):
            num = int(input("Enter numbers for list: "))
            fibo.append(num)

        for i in range(len(fibo)):
            while i == 2:
                if fibo[i] != fibo[i - 1] + fibo[i - 2]:  # if this isn't true: break because this isn't fibo
                    print("This isn't Fibo!")
                    break
                else:
                    print("This is Fibo!")
                    break
    elif ans == 3:
        for count in range(10):
            draw = randint(1, 20)
            print(draw)
            if draw == 12:
                print("You've got 12...The program will Exit now...")
                break
    print("DONE!\nDo you want to Restart the program? (Y/N)")
    choose = input()
    if choose == 'y' or choose.lower() == 'yes':
        print("Restarting the program...")
        sleep(1)
    else:
        break