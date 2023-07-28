a = int(input("Please enter the value of a: "))
b = int(input("Please enter the value of b: "))
c = int(input("Please enter the value of c: "))

discriminant = ((b*b) - (4*a*c))

if discriminant == 0:
    print("The quadratic equation has 1 real solution.")
elif discriminant > 0:
    print("The quadratic equation has 2 real solutions.")
else:
    print("The quadratic equation has 2 complex solutions.")