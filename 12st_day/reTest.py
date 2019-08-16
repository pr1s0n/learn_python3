import re
test = 'abc'
if re.match(r'^a',test):
	print('ok')
else:
	print('failed')