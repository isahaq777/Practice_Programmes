"""You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A
Your task is to execute those operations and print the sum of elements from set A"""
a = input("Enter the number of elements in a set A: ")
aa = set(input("Enter the line contains the space separated list of elements in set A: ").split(' '))
b = int(input("Enter the integer, the number of other sets.: "))
"""The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set."""
e = [eval(f"aa.{input().split(' ')[0]}({set(input().split(' '))})") for x in range(b)]
print(sum(map(int, aa)))