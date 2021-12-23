'''
A heap data structure implemented using a list
'''

'''
Heap Empty exception
'''
class HeapEmptyError(Exception):
	def __init__(self, message='Heap is empty!'):
		self.message = message

	def __str__(self):
		return self.message



'''
The heap class
implements a min-heap
'''
class Heap(object):
	def __init__(self, comparatorfn=None):
		self.items = []

		# helper functions to get parent, left and right nodes of a node at index, i
		self.parent = lambda i:  (i-1)/2
		self.left = lambda i:  2*i+1
		self.right = lambda i:  2*i+2

		self.comparatorfn = comparatorfn if comparatorfn else cmp
		self.isHeap = self.isHeap_r # use recursive version by default


	# A default print function if no aggregator is provided
	# for traversal functions
	@staticmethod
	def _default_printfn(item):
		print str(item) + " ",

	def __str__(self):
		hstr = "[%d]: " %(len(self.items))
		for item in self.items:
			hstr += "%s " %(item)
		return hstr.strip()

	def __repr__(self):
		return repr(self.items)


	def __len__(self):
		return len(self.items)


	'''
	decorator to ensure heap is not empty
	on heap operations that modify the heap
	'''
	def check_empty(func):
		def f(self, *args, **kwargs):
			if len(self.items) == 0:
				raise HeapEmptyError("HeapEmptyError: '%s(): Heap is empty'" %(func.__name__))
			rv = func(self, *args, **kwargs)
			return rv
		return f


	# []
	@check_empty
	def __getitem__(self, i):
		if (i < 0 or i >= len(self.items)):
			raise IndexError
		return self.items[i] 



	@check_empty
	def peek(self):
		return self.items[0]


	'''
	All items after index: n/2-1 are leaf nodes in a heap
	'''
	@staticmethod
	def isLeaf(i, n):
		return i > (n-2)/2


	'''
	Do the items form a heap (satisfy the heap property)?
	Recursively check if a subtree rooted at 'i' is a heap
	i.e. all its children are < the parent
	'''
	def isHeap_r(self, i=0):
		# Leaf nodes are heaps by default
		if self.isLeaf(i, len(self.items)):
			return True

		# Do a preorder traversal checking if root < left,right
		# and then check for left and subtrees
		l,r = self.left(i), self.right(i)
		if l < len(self.items) and not self.comparatorfn(self.items[i], self.items[l]) <= 0:
			return False
		if r < len(self.items) and not self.comparatorfn(self.items[i], self.items[r]) <= 0:
			return False

		return self.isHeap_r(l) and self.isHeap_r(r)


	'''
	Do the items form a heap (satisfy the heap property)?
	Iteratively check all non-leaf nodes are heaps
	i.e. all its children are < the parent
	'''
	def isHeap_i(self):
		n = len(self.items)
		for i in xrange((n-2)/2+1):
			l,r = self.left(i), self.right(i)
			if l < len(self.items) and not self.comparatorfn(self.items[i], self.items[l]) <= 0:
				return False
			if r < len(self.items) and not self.comparatorfn(self.items[i], self.items[r]) <= 0:
				return False

		return True



	'''
	Bubble up item at index, 'i' all the way up
	till the heap property is restored
	'''
	def bubble_up(self, i):
		while (i > 0) and self.comparatorfn(self.items[i], self.items[self.parent(i)]) < 0:
			self.items[i], self.items[self.parent(i)] = self.items[self.parent(i)], self.items[i]
			i = self.parent(i)


	'''
	Bubble-down an item at 'i'
	to its rightful place, and the heap property is restored
	Assumes left and right subtrees are already heaps.

	Typically used after extracting the top of the heap,
	the last item in the heap replaces the top of the heap
	and is bubbled down, until heap property is restored.
	'''
	def bubble_down_r(self, n, i=0):
		l, r = self.left(i), self.right(i)
		smaller_of = lambda i,j: i if self.comparatorfn(self.items[i], self.items[j])<0 else j

		smallest = i
		# Find the smallest of left, right and root items
		if l < n:
			smallest = smaller_of(smallest, l)

		if r < n:
			smallest = smaller_of(smallest, r)

		# swap root of the subtree with the smallest of the left and right children
		if (smallest != i):
			self.items[i], self.items[smallest] = self.items[smallest], self.items[i]
			self.bubble_down_r(n, smallest)


	'''
	Bubble-down: Iterative version
	Bubble-down an item at 'i'
	to its rightful place, and the heap property is restored
	Assumes left and right subtrees are already heaps.

	Typically used after extracting the top of the heap,
	the last item in the heap replaces the top of the heap
	and is bubbled down, until heap property is restored.
	'''
	def bubble_down(self, n, i=0):
		smaller_of = lambda i,j: i if self.comparatorfn(self.items[i], self.items[j])<0 else j

		l, r = self.left(i), self.right(i)

		# Bubble-down until item at 'i' is a leaf-node
		# (no left-child, therefore no right-child either)
		# OR
		# when item at 'i' is bubbled down far enough, no more changes are needed
		# to maintain the heap property
		while l < n:
			if not r < n:
				# No right-child, l is the smaller child
				idx = l
			else:
				# Pick smaller of the left and right children to swap with parent, i
				idx = smaller_of(l, r)

			if (smaller_of(i, idx) == i):
				# parent 'i' is in its rightful place
				# bubble-down complete
				break

			# item at 'i' > its children => bubble-down
			self.items[i], self.items[idx] = self.items[idx], self.items[i]
			i = idx
			l, r = self.left(i), self.right(i)


	'''
	Add an item to the heap
	Start by adding item to the end to the list,
	then bubble up until it's in its rightful place, and 
	the heap property is restored.
	'''
	def add(self, item):
		self.items.append(item)
		self.bubble_up(len(self.items)-1)


	
	'''
	remove the top of the heap
	'''
	@check_empty
	def remove(self):
		top = self.items[0]
		self.items[0] = self.items[-1]
		self.items.pop()
		self.bubble_down(len(self.items), 0)

		return top



	'''
	Decrease key of item at index 'i' to new
	new should be <  items[i]
	'''
	def decreaseKey(self, i, new):
		if not self.comparatorfn(new, self.items[i]) < 0:
			raise ValueError("%s: %s() - New key should be less than current value" %('ValueError', self.decreaseKey.__name__))
		self.items[i] = new
		self.bubble_up(i)


	'''
	Increase key of item at index 'i' to new
	new should be >  items[i]
	NOTE: decreaseKey() is the common operation because it promotes an item up the tree in a heap
	However, there's no reason why increaseKey() cannot be supported.
	NOTE: increaseKey() promotes up the tree for a maxheap.
	'''
	def increaseKey(self, i, new):
		if not self.comparatorfn(new, self.items[i]) > 0:
			raise ValueError("%s: %s() - New key should be greater than current value" %('ValueError', self.increaseKey.__name__))
		self.items[i] = new
		self.bubble_down(len(self.items), i)


	'''
	[] : update item at index i
	'''
	@check_empty
	def __setitem__(self, i, value):
		if (i < 0 and i >= len(self.items)):
			raise IndexError

		if self.comparatorfn(value, self.items[i]) < 0:
			# If new value is lesser, Use decreaseKey() to bubble up
			self.decreaseKey(i, value)
		elif self.comparatorfn(value, self.items[i]) > 0:
			# If new value is greater, Use increaseKey() to bubble down
			self.increaseKey(i, value)
		else:
			self.items[i] = value


	'''
	Uses bubble_down to build heap out of a list/iterable starting from 
	first non-leaf node from the bottom 
	'''
	@classmethod
	def build_heap(cls, l):
		# heap[(n-2)/2 .. 0] are non-leaf nodes
		# foreach i: (n-2)/2 .. 0, bubble_down(i)

		# Instantiate current class
		# will instantiate derived class if build_heap is called
		# from one of the Heap's child classes
		heap = cls()
		n = len(l)
		heap.items = l
		for i in xrange((n-2)/2, -1, -1):
			heap.bubble_down(n, i)

		return heap


	'''
	Repeatedly call remove() to get a sorted list
	'''
	def sorted(self, aggregatorfn=None, *args, **kwargs):
		if not aggregatorfn:
			aggregatorfn = self._default_printfn

		while self:
			aggregatorfn(self.remove(), *args, **kwargs)


