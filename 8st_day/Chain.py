class Chain(object):
	"""docstring for Chain"""
	def __init__(self, path=''):
		# super(Chain, self).__init__()
		self._path = path
	def __getattr__(self,path):
		return Chain('%s/%s' % (self._path,path))

	def __str__(self):
		return self._path

	__repr__ = __str__

print(Chain().status.user.timeline.list)