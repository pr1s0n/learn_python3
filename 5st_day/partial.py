import functools
sorted2 = functools.partial(sorted,key=abs)
L = [1,2,-3,23,6,-4]
print(sorted2(L))