my_dict = {"Osher": "50", "Moshe": "40", "Roy": "300", "Yossi": "40", "Ben": "30"}
sum_money = 0
list = list(my_dict.values())
for i in range(len(list)):
    if i == 0 or i == 4:
        sum_money += int(list[i])
print("The sum money of the first person and last is:  " + str(sum_money))

dict2 = {"Gal": sum_money}
my_dict.update(dict2)
print(my_dict)

print("The number of entries are:  " + str(len(my_dict)))
print("idan" in my_dict)  # Checks if idan is in the dictionary (as a KEY)