n = int(input())
phoneBook = {}
for _ in range(n):

    nombre, telefono = input().split()
    phoneBook[nombre] = telefono

while True:
    try:
        nombre = input()
        if not nombre:
            break
        if nombre in phoneBook:
            print(f"{nombre}={phoneBook[nombre]}")
        else:
            print("Not found")
    except EOFError:
        break