def create_adj(n):
    for i in range(n):
        for j in range(n):
            if j == i + 1 or j + 1 == i:
                print(1, end=' ')
            else:
                print(0, end=' ')
            if j == n - 1:
                if i != n - 1:
                    print(' \\\\')
            else:
                print('&', end=' ')
create_adj(20)