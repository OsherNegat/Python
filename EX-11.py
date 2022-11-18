#0-510 Kw/h = 0.90 ILS | 510+ Kw/h = 0.90 ILS Until 510 Kw/h + 1.10 ILS For Each Kw/h that is above 510
Kwh = float(input("Enter the Kwh consumed this month: \n"))
if Kwh <= 510 :
    price = Kwh * 0.90
    print("The Price is: " + str(price) + " ILS")
elif Kwh > 510 :
    price = 510 * 0.90 + ((Kwh - 510) * 1.10)
    print("The Price is: " + str(price) + " ILS")