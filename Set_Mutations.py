a = input()
aa = set(input().split(' '))
b = int(input())
e = [eval(f"aa.{input().split(' ')[0]}({set(input().split(' '))})") for x in range(b)]
print(sum(map(int, aa)))