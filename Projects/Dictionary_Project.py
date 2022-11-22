my_dict = {"osher": "50", "Moshe": "100", "Idan": "65", "Yarin": "75", "Yoni": "90"}
sum_money = 0
list = list(my_dict.values())
for i in range(len(list)):
    if i == 0 or i == 4:
        sum_money += int(list[i])
print("The Total money of the first and last in ILS is:  " + str(sum_money))

new_dict = {"Yossi": "140"}
my_dict.update(new_dict)
print("The UPDATED Dictionary is:  " + str(my_dict))
counter = 0

for i in range(len(my_dict)):
    counter += 1
print("There are: " + str(counter) + " Tuples in Dictionary")
print("idan" in my_dict.keys())  # Checks if idan is a tuple inside the Dictionary