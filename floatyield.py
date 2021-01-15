def frange(start=0.1,end=1.0step=0.1):
    num=start
    while num<=end:
        yield num
        num +=step
for i in frange():
    print(i)
