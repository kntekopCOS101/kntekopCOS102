import math
import numpy as np
equation = input('''Enter;
1, to solve for quadratic equation
2, to solve for cubic equation
3, to solve for quartic equation ''')

if equation == "1" :
    a = float(input("Kindly enter your choice values for a in ax^2 + bx + c "))
    b = float(input("Kindly enter your choice values for b in ax^2 + bx + c "))
    c = float(input("Kindly enter your choice values for c in ax^2 + bx + c "))
    discriminant = b**2 - 4 * a * c

    if discriminant > 0 :
        root1 = (-b + math.sqrt(discriminant)) / 2 * a
        root2 = (-b - math.sqrt(discriminant)) / 2 * a

        print(f"The roots of your quadratic equation are {root1} and {root2}")

    elif discriminant == 0 :
        root1 = -b / (2 * a)

        print(f"The root of your quadratice equation is {root1}")

    else :
        root1 = (-b + math.sqrt(-discriminant)) / 2 * a
        root2 = (-b - math.sqrt(-discriminant)) / 2 * a


elif equation == "2" :
    a = float(input("Kindly enter your choice values for a in ax^3 + bx^2 + cx + d "))
    b = float(input("Kindly enter your choice values for b in ax^3 + bx^2 + cx + d "))
    c = float(input("Kindly enter your choice values for c in ax^3 + bx^2 + cx + d "))
    d = float(input("Kindly enter your choice values for d in ax^3 + bx^2 + cx + d "))

    values = [a, b, c, d]
    roots = np.roots(values)
    print(f"These are the values for your roots {roots}")


else :
    a = float(input("Kindly enter your choice values for a in ax^4 + bx^3 + cx^2 + dx + e "))
    b = float(input("Kindly enter your choice values for b in ax^4 + bx^3 + cx^2 + dx + e "))
    c = float(input("Kindly enter your choice values for c in ax^4 + bx^3 + cx^2 + dx + e "))
    d = float(input("Kindly enter your choice values for d in ax^4 + bx^3 + cx^2 + dx + e "))
    e = float(input("Kindly enter your choice values for e in ax^4 + bx^3 + cx^2 + dx + e "))

    values = [a, b, c, d, e]
    roots = np.roots(values)
    print(f"These are the roots of your quartic equation {roots}")


