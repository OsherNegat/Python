import random
NAME = input("Enter your name: ")
print("WELCOME " + NAME + '!' + "\nEnter how much money you've got ")
money = int(input("Your money in ILS:  "))
profit = 0
if money - 3 > 0:
    print("Your Exchange is: " + str(money - 3) + " ILS\n")
elif money < 3:
    print("Sorry, You don't have enough money to play!")
    raise SystemExit
else:
    print("\nYou Don't have Exchange!")
    print("You can play only 1 round!\n")
print("How much rounds do you want to play?\n(Every round costs 3 ILS)")
rounds = int(input("Enter number of rounds: "))

for num_of_round in range(rounds):
    print("-------------")
    print("ROUND", num_of_round + 1, ':')
    if money < 3:
        print(f"Sorry {NAME} you can't play anymore!")
        break
    cube_1 = random.randint(1, 6)
    cube_2 = random.randint(1, 6)
    print("The generated numbers are: ", cube_1, cube_2)
    if cube_2 == cube_1:
        print("Congarts!\nYou won 100 ILS!")
        profit += 100
    elif (cube_2 == cube_1) == 6:
        print("Congarts!\nYou won 1000 ILS!")
        profit += 1000
    elif cube_2 != cube_1 and cube_2 == 2:
        print("Congarts!\nYou won 40 ILS!")
        profit += 40
    elif cube_2 != cube_1 and cube_1 == 1:
        print("Congarts!\nYou won 20 ILS!")
        profit += 20
    else:
        print("YOU LOST!")
    money -= 3
    print("-------------")
print("Your Total Earnings: ", str(profit) + ' ILS')