def create_input(n):
    '''Fungsi ini mengembalikan matriks ketetanggaan berukuran nxn sebagai input eksperimen.
    Bentuk graf sesuai gambar yang ada di file `dataset.md`'''
    arr = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i].append(0)
    for i in range(n - 1):
        arr[i][i + 1] = 1
        arr[i + 1][i] = 1
    return arr