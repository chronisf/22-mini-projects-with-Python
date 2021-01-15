def determinant(mat):
    if len(mat)!=2:
        return False,'flase'
    elif len(mat[0])!=2 or len(mat[1])!=2:
        return False,"false'
    det=mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
    turn True,det
input_matrix =[3,6].[4,10]]
flag, res = determinant(input_matrix)
if flag:
    print(res)
else:
    print(res)
