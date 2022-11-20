grade1 = int(input("Enter your grade: \n"))
grade2 = int(input("Enter your grade: \n"))
grade3 = int(input("Enter your grade: \n"))
Avg_Grade = (grade1+grade2+grade3)/3
if Avg_Grade>95 and (grade1 and grade2 and grade3 > 90):
    print("Pass")
else:
    print("Sorry, We aren't Accepting you! Good Luck :)")