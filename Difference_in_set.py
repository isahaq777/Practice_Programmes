#Your task is to find the total number of people use product A only.
Product_A = int(input("number of people who use item A: "))
serial_num_A = set(map(int, input("Serial numbers for the people who use item A: ").split()))
Product_B = int(input("number of people who use item B: "))
serial_num_B = set(map(int, input("Serial numbers for the people who use item B: ").split()))
result = serial_num_A.difference(serial_num_B)
print("The total number of people use product A only: ", len(result))