#A Program to deteremin the roots of a qaudratic function

#accept inputs for a,b and c
a = int(input("Enter a value for a:"))
b = int(input("Enter a value for b:"))
c = int(input("Enter a value for c:"))

d = b**2 - 4*a*c

if (d<0):
    print("Quadratic  function with a = ",a, ", b =",b," and c =",c,
          " will evaluate to complex roots")


else:
    x1 = (-b+d**0.5)/(2*a)
    x2 = (-b-d**0.5)/(2*a)
    print("The real roots to quadratic funtion with a = ",a, ", b =",b,
          " and c =",c, "are:")
    print("x1 = \t",x1,"\nx2 = \t",x2)
