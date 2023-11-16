#You are given an integer,N. Your task is to print an alphabet rangoli of size.N
#Below is the example for size 3
"""----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----"""
import string
def print_rangoli(size):
    alphabet = string.ascii_lowercase
    width = size*2-1 + (size-1) * 2
    for i in range(1-size, size):
        sublist = list(alphabet[abs(i):size])
        prelist = list(reversed(sublist[1:]))
        wholelist = prelist + sublist
        print('-'.join(wholelist).center(width, '-'))
    # your code goes here

if __name__ == '__main__':
    n = int(input("Enter the postive integer greater than 0 for alphabetic rangoli: "))
    print_rangoli(n)