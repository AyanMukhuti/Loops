Range=int(input("Enter a last number of range:"))
num=int(input("Enter number to be used as divisor:"))
for i in range(1,Range+1):
    if i%num==0:
        print(i)

