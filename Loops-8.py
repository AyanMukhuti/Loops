lst=[]
for i in range(10):
    a=int(input("Enter an integer:"))
    lst.append(a)
print("Given integers are:",lst)
for j in lst:
    if j==0:
        print("Zero is neither even nor odd, neither positive nor negative.")
    if j>0:
        print("Positive numbers are:",j)
    elif j<0:
        print("Negative numbers are:",j)
    elif j%2!=0:
        print("Odd numbers are:",j)
    elif j%2==0:
        print("Even numbers are:",j)
    
