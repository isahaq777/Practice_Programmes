if __name__ == "__main__":
    n = int(input())
    str_arr = []
    for i in range(0,n):
        str_arr.append(input())

    for i in range(0,n):
        print(*["".join([str_arr[i][j] for j in range(0,len(str_arr[i])) if j%2==0]),"".join([str_arr[i][j] for j in range(0,len(str_arr[i])) if j%2!=0])], sep=" ")