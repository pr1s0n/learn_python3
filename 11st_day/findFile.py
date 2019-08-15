import os
dir = os.path.abspath('.')
def fileFound(seq, filedir):
    li = os.listdir(filedir)
    for x in li:
        path = os.path.join(filedir,x)
        if os.path.isfile(path) and seq in x:
            print(os.path.abspath(path))
            #str.replace(old, new[, max])
        if os.path.isdir(path):
            fileFound(seq, path)
fileFound('F',dir)
