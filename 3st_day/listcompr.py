# -*- coding:utf-8 -*-
L1 = ['hello','world','apple',18,None]
L2 = [i.lower() for i in L1 if isinstance(i,str)]
print(L2)
if L2 == ['hello','world','apple']:
    print('success')
else:
    print('false')

