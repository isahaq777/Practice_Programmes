n=int(input("Enter the number: "))
def fib(n):
    if n<0:
        print("incorrect input")
    elif n==0:
        return o
    elif n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(n))
