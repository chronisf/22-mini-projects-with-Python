import math
total = 0
asum = 0
asum_roots = 0
while True:
    num = input('num or q:')
    if num == 'q':
        break
    else:
        num = float(num)
    total+=1
    asum+=num
    asum_roots=math.sqrt(num)
