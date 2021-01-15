def add(*args):
    print(args)
    s = 0
    for i in args:
        s +=i
    return s
suma = add(5,10)
print(suma)
sumb = add(5,10,15,20)
print(sumb)
