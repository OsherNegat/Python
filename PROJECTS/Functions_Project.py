from time import sleep

def menu():
    while True:
        print("------------\nWelcome To The MENU!\nPress 1 Print Your Dog Details\nPress 2 Print Your Friend List"
              "\nPress 3 Print Factorial Number (!)")
        choose = int(input())
        if choose == 1:
            dog_name = input("Enter your dog's name:  ")
            dog_age = int(input("Enter your dog's age:  "))
            print(dog_f(dog_name, dog_age))
        elif choose == 2:
            print(friends_f())
        elif choose == 3:
            print(n_a())
        else:
            print("Please choose numbers between 1-4 only!")
            print("Do you want to restart the PROGRAM?(Y/N)")
            choice = input()
            if choice == 'y' or choice.lower() == 'yes':
                continue
            else:
                print("Qutting...")
                sleep(1)
                raise SystemExit
        print("Do you want to restart the PROGRAM?(Y/N)")
        choice = input()
        if choice == 'y' or choice.lower() == 'yes':
            continue
        else:
            print("Qutting...")
            sleep(1)
            raise SystemExit

def dog_f(dog_name, dog_age):
    new_age = dog_age * 7
    print(f"{dog_name}'s age in human's is: ", new_age)
    sleep(2)
    return "Done\n------------"

def friends_f():
    print("Enter how much friends do you want to set in your friends list: ")
    count = int(input())
    friends = []
    for i in range(count):
        friend = input("Enter your friend's name: ")
        friends.append(friend)
    print(friends)
    new = input("Enter Extra friend:  ")
    if new in friends:
        print(f"{new} is already in your friends list!")
    else:
        friends.append(new)
        print("Your new list is:  ", friends)
    sleep(2)
    return "Done!\n------------"

def n_a():
    num = int(input("Enter a number:  "))
    sum = 1
    for i in range(1, num+1):  # 1 - 23
        sum = sum * i   # sum = 1*1 >> sum = 1*2 >> sum = 1*3
    print("The sum is: ", sum)
    sleep(2)
    return "Done!\n------------"

print(menu())