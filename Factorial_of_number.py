from math import factorial
num=int(input("enter the number "))
factorial=1
if num<0:
    print("factorial doesn't exit")
elif num==0:
    print("zero is the factorial")
else:
    for i in range(1,num+1):
     factorial=factorial*i
print("the factorial of num is ",factorial)
