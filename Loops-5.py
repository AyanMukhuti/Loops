a=int(input("Enter number of rows:"))
for i in range(65,65+a):
    k=i
    for j in range(65,i+1):
        print(chr(k),end="")
        k=k+1
    print()
