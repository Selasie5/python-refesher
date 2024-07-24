from math import sqrt
print("****Pythagoras Theorem Calculator***")
adjacent = int(input("Please enter the value of the adjacent of the triangle: "))
opposite = int(input("Please enter the value of the oppoosit of the triangle: "))
print("Just a sec, hypotenuse is equal to ....")
hypotenuse = sqrt((adjacent**2) + (opposite**2))
print(f'The hypotenuse is {hypotenuse}')