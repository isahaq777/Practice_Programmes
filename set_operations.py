#you have a non-empty set s , and you have to execute N commands given in N lines. The commands will be pop, remove and discard. 
n = int(input())
s = set(map(int, input().split()))
n2 = int(input())
for c in range(n2):
    list = []
    s1 = input()
    list = s1.split()
    try:
        if len(list) > 1:
            command = f's.{list[0]}({int(list[1])})'
            eval(command)
        else:
            command = f's.{list[0]}()'
            eval(command)
    except KeyError:
        pass
print(sum(s))