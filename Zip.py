#The National University conducts an examination of N students in X subjects.
#Your task is to compute the average scores of each student.
_ , n = map(int, input().split())
lista = [list(map(float, input().split())) for _ in range(n)]

for i in zip(*lista):
    print(sum(i)/n)