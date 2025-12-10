def transpose(mat):
    if mat == []:
        return mat
    else:
        # Проверка на рванность
        l_mat = len(mat[0])
        ok = 1
        for i in mat:
            if len(i) != l_mat:
                ok = 0
            else:
                ok = 1
        # Проверка на рванность
        if ok == 1:

            trans = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
            return trans
        else:
            return "ValueError"


def row_sums(mat):
    # Проверка на рванность
    l_mat = len(mat[0])
    ok = 1
    for i in mat:
        if len(i) != l_mat:
            ok = 0
        else:
            ok = 1
    # Проверка на рванность
    if ok == 1:
        t = list()
        for i in mat:
            s = sum(i)
            t = t + [s]
        return t
    else:
        ("ValueError")


def col_sums(mat):
    # Проверка на рванность
    l_mat = len(mat[0])
    ok = 1
    for i in mat:
        if len(i) != l_mat:
            ok = 0
        else:
            ok = 1
    # Проверка на рванность
    if ok == 1:
        t = list()
        i_num_sum = 0
        for num in range(0, l_mat):
            for i in mat:
                i_num_sum = i_num_sum + i[num]

            t = t + [i_num_sum]
            i_num_sum = 0
        return t


print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
print("_______________")
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
print("_______________")
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
