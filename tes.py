def create_arr(n):
    arr = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i].append(0)
    for i in range(n - 1):
        arr[i][i + 1] = 1
        arr[i + 1][i] = 1
    print('[')
    for i in arr:
        print(i, end=',\n')
    print(']')

create_arr(20)