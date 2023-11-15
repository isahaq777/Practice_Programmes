#Given sets of integers, and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either or but do not exist in both.
m = int(input("Enter the inputs for M: "))
m_set = set(map(int,input("Enter the M space-separated integers: ").split()))
n =int(input("Enter the inputs for N: "))
n_set = set(map(int,input("Enter the N space-separated integers: ").split()))
result = sorted(m_set.union(n_set) - m_set.intersection(n_set))
for i in result:
    print(i)