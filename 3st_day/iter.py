def findMinAndMax(L):
    if len(L)==0:
        return (None,None)
    else:
        min = L[0]
        max = L[0]
        for i in L:
            if i < min:
                min = i
            elif i >max:
                max = i
        return(min,max)
print(findMinAndMax([7,1,2]))
if findMinAndMax([]) != (None, None):
    print('false')
elif findMinAndMax([7]) != (7, 7):
    print('false')
elif findMinAndMax([7, 1]) != (1, 7):
    print('false')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('false')
else:
    print('success')

