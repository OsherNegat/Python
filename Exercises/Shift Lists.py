steps = int(input("Enter number of steps:  "))  # The number of times you want to SHIFT the list
                                                # Positive value = Shift Left
                                                # Negative value = Shift Right
list = [4,5,6,7,8,9,0]
print("The ORIGINAL list:  " + str(list))  # Print the Original list, so we can see the changes afterwards
list = list[-steps:] + list[:-steps]  # list[steps:] >> Go to the list and start the list with the value of the variable steps
                                    # And finish the list at the end of the original list
                                    # list[:steps] >> Go to the list and start it from index 0 till the value of the variable steps
                                    # And finish it with the value of the variable steps
                                    # After these 2 actions combine them together and create a new list
                                    # EXAMPLE: steps = 2
                                    # list[steps:] = The output will be: [6,7,8,9,0]
                                    # list[:steps] = The output will be: [4,5]
                                    # list = list[steps:] + list[:steps] = Output: [6,7,8,9,0,4,5]

print("The SHIFTED list:  " + str(list))