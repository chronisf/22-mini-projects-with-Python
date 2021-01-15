import math
x = float(input('x='))
y = float(input('y='))
r = math.sqrt(x**2+y**2)
h = math.degrees(math.atan(y/x))
print('r=',r,'h=',h)
