a=int(input("Enter length of first side:"))
b=int(input("Enter length of second side:"))
c=int(input("Enter length of third side:"))
if a+b>c and a+c>b and b+c>a:
    print("Formation of triangle is possible.")
else:
    print("Formation of triangle is not possible.")
s=(a+b+c)/2
import math
b=s*(s-a)*(s-b)*(s-c)
Area= math.sqrt(b)
print(Area,"is the area of the givel triangle.")
    
