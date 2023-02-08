lst=[]
lower=int(input("Enter a lower range:"))
upper=int(input("Enter an upper range:"))
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
            else:
               lst.append(num)
print(lst)
