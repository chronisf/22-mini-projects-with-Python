def fseq(n,k):
    if k<1:
        return print('k<1')
    for i in range(1,k+1):
        yield n*i
for x in fseq(10,3):
    print(x)
