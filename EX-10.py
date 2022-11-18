#Max Delivery Weight=>50Kg
#Cost is 10 ILS for each KG
#0-20 kg=> 1 ILS for Kg | 21-40 => 2 ILS for kg | 41+ => 3 ILS for kg
Weight_Package = int(input("Enter the weight of the package in Kg: \n"))
if Weight_Package <= 20 :
    price = Weight_Package * 1
    print("The Price is: " + str(price) + " ILS")
elif Weight_Package <= 21 :
    price = Weight_Package * 2
    print("The Price is: " + str(price) + " ILS")
elif Weight_Package <= 41 :
    price = Weight_Package * 3
    print("The Price is: " + str(price) + " ILS")