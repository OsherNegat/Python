Month_4 = int(input("Enter the baybie's mass in grams Before: \n"))
This_Month = int(input("Enter the baybie's mass in grams Today: \n"))
if This_Month > Month_4:  
    Weight_Gained = This_Month - Month_4
    print("Weight Gained: \n" + str(Weight_Gained))
elif This_Month == Month_4: print("The baby is in the same weight")
else: print("Weight Lost: \n" + str(Month_4-This_Month))
