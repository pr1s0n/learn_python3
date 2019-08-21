def generator_1(titles):
	yield titles

def generator_2(titles):
	yield from titles

titles = ['Python','JavaScript','C']
for title in generator_1(titles):
	print('生成器1: %s' % title)
for title in generator_2(titles):
	print('生成器2: %s' % title)