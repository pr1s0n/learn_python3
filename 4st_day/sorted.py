L = [('Bob',78),('lisa',89),('lihua',92)]
def by_name(t):
	return t[0]
def by_score(t):
	return -t[1]
L2 = sorted(L,key=by_name)
L3 = sorted(L,key=by_score)
print(L2)
print(L3)