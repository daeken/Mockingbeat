indent = 0

def line(*args):
	print '\t' * indent + ' '.join(map(str, args))

def modIndent(amount):
	global indent
	indent += amount

class ScopedTransform(object):
	def __init__(self, func, *args):
		self.func = func
		self.args = args

	def __call__(self, *args):
		return ScopedTransform(self.func, *args)

	def __enter__(self):
		line('%s(%s) {' % (self.func, ', '.join(map(str, self.args))))
		modIndent(+1)

	def __exit__(self, type, value, traceback):
		modIndent(-1)
		line('}')

	def __getattr__(self, name):
		def sub(*args):
			self.__enter__()
			value = globals()[name](*args)
			self.__exit__(None, None, None)
			return value
		return sub

	def __getitem__(self, ranges):
		if not isinstance(ranges, tuple):
			ranges = (ranges, )
		return StackedTransform([self] + list(ranges))

class StackedTransform(object):
	def __init__(self, transforms):
		self.transforms = transforms

	def __enter__(self):
		for tf in self.transforms:
			tf.__enter__()

	def __exit__(self, type, value, traceback):
		for tf in self.transforms[::-1]:
			tf.__exit__(type, value, traceback)

class Function(object):
	def __init__(self, func, *transforms):
		self.func = func
		self.transforms = transforms

	def __call__(self, *args):
		for tf in self.transforms:
			tf.__enter__()
		self.func(*args)
		for tf in self.transforms[::-1]:
			tf.__exit__(None, None, None)

	def __getitem__(self, ranges):
		if not isinstance(ranges, tuple):
			ranges = (ranges, )
		return Function(self.func, *(list(self.transforms) + list(ranges)))

@Function
def cube(dimensions):
	try:
		dimensions[0]
	except:
		dimensions = [dimensions, dimensions, dimensions]
	line('cube([%s]);' % ', '.join(map(str, dimensions)))

@Function
def cylinder(height, d1, d2):
	line('cylinder(%s, d1=%s, d2=%s);' % (str(height), str(d1), str(d2)))

def fn(v):
	print '$fn = %s;' % v

difference = ScopedTransform('difference')
intersection = ScopedTransform('intersection')
union = ScopedTransform('union')
ghost = ScopedTransform('%union')
hull = ScopedTransform('hull')

mirror = ScopedTransform('mirror')
rotate = ScopedTransform('rotate')
scale = ScopedTransform('scale')
translate = ScopedTransform('translate')

right = lambda x: translate([x, 0, 0])
left = lambda x: translate([-x, 0, 0])

forward = lambda y: translate([0, y, 0])
back = lambda y: translate([0, -y, 0])

up = lambda z: translate([0, 0, z])
down = lambda z: translate([0, 0, -z])
