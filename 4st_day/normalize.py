def normalize(name):
	return str.capitalize(name)

L1 = ['Admin','LISA','barT']
L2 = list(map(normalize,L1))
print(L2)