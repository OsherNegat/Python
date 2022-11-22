num = int(input("Enter a number:  "))  # Numeric Input
result = []  # Create a list to store the values
while num > 0:  # Whenever the number is above 0 enter the while loop
    if num % 2 == 0:  # Check if the number has remainder
        result.append('0') # Returns '0' because there's no remainder
    else:
        result.append('1') # Returns '1' because there's a remainder
    num //= 2  # Returns the rounded value of the number and ignores the remainder
    if num < 1:  # if the number is less than 1, than it's irrelevant
        break
print("The number in Base 2 is:  " + str(result[::-1]))   # Prints the reversed list