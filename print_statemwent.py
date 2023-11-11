#the included #code stub will read an integer,
#, from STDIN.
#Without using any string methods, try to print the following:
#Note that "
#" represents the consecutive values in between.
#Output Format
#Print the list of integers from
#through as a string, without spaces and also another case where numbers are in next line.
if __name__ == '__main__':
    r = int(input("Enter the r value: "))
    n = int(input("Enter the n value: "))
    if(r<=n):
        while(r<=n):
            print(r,end='')
            r=r+1
    else:
        while(r>n):
            print(n)
            n=n+1