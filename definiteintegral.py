def f(x):
    return x**2
def frange(start, end, step):
    num=start
    while num<end:
        yield num
        num+=step
emv=o
x0=0
xfin=1
dx=0.01
for x in frange(x0,xfin,dx):
    emv+=f(x)*dx
print(round(emv,4))
