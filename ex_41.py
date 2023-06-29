import math

# Prompt the user for input
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Calculate the discriminant
discriminant = b ** 2 - 4 * a * c

# Compute the real roots
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("Two distinct real roots:")
    print("Root 1:", root1)
    print("Root 2:", root2)
elif discriminant == 0:
    root = -b / (2 * a)
    print("One real root:")
    print("Root:", root)
else:
    print("No real roots exist.")
