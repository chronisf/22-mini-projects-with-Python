prot = input('word:')
spaces =[]
for index,i  in enumarate(prot):
    if i =='':
        spaces.append(index)
print(spaces)
words=[]
kstart = 0
for k in spaces:
    words.append(prot[kstart:k])
    kstart = k+1
else:
    words.append(prot[kstart:]0
print(words)
