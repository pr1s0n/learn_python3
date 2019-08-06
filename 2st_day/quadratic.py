import math
def quadratic(a,b,c):
    d = b*b-4*a*c
    if d>0:
        num1 = (-b+math.sqrt(d))/(2*a)
        num2 = (-b-math.sqrt(d))/(2*a)
        return num1,num2
    elif d == 0:
        num3 = (-b)/(2*a)
        return num3
    else:
        return "no"

print('quadratic(2,3,1)=',quadratic(2,3,1))
print('quadratic(1,3,-4)',quadratic(1,3,-4))

if quadratic(2,3,1) != (-0.5,-1.0):
    print('false')
elif quadratic(1,3,-4) != (1.0,-4.0):
    print('false')
else:
    print('success')

