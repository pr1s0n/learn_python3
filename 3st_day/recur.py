def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num-1,num * product)
print(fact(5))

#利用递归函数移动汉诺塔
def move(n,a,b,c):
    if n == 1:
        print("move",a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
move(4,'A','B','C')
