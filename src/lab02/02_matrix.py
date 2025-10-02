def transpose(mat):
    if mat == []:
        return mat
    else:
        l_mat = len(mat[0])
        for i in mat:
            ok = 1
            if i != l_mat:
                ok = 0
        if ok == 1:
            trans = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    return trans

def row_sums(mat):
    return mat

def col_sums(mat):
    return mat

print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
print('_______________')
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
print('_______________')
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))