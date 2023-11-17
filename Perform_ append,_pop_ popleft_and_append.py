#Perform append, pop, popleft and appendleft methods on an empty deque
from collections import deque
d = deque()
for i in range(int(input("Enter the number of times operation need to be performed: "))):
    c = input("Enter the commands and values: ").split()
    method = getattr(d, c[0])
    if len(c) == 2:
        method(c[1])
    else:
        method()
print(" ".join(d))