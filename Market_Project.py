print('Welcome to our supermarket...\nDo you want to buy some ingredients?(Y/N)')
if input() == 'Y' or 'y':
    print("Great! Let's Have a look at our Menu\n------------")
else:
    print("Ok, Bye!")
    exit
print("Here's the Menu:\n1. Tomato = 3 ILS\n2. Cucumber = 2 ILS\n3. Coca-Cola = 5 ILS\n4. Chicken = 20 ILS Per KG\n------------")
bill = 0
for i in range(5):
    if i == 1:
        print("How much Tomatoes do you wish to buy?")
        bill += int(input()) * 3
        i += 1
    elif i == 2:
        print("How much Cucumbers do you wish to buy?")
        bill += int(input()) * 2
        i += 1
    elif i == 3:
        print("How much Coca-Cola bottles do you wish to buy?")
        bill += int(input()) * 5
        i += 1
    elif i == 4:
        print("How much KG of Chicken do you wish to buy?")
        bill += int(input()) * 20
        i += 1
    i += 1
print("Thanks for buying, Here's your bill without tax:  "+str(bill) + ' ILS')
print("Thanks for buying, Here's your bill with tax:  "+str("%.2f" % (bill*1.17)) + ' ILS')