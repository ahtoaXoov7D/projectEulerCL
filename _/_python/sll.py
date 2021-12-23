from node import Node

'''
Exceptions for the SLL class
'''

'''
Overflow exception
TODO: when does this happen?
'''
class OverFlowError(Exception):
	def __init__(self):
		self.message = 'Overflow error!'

	def __str__(self):
		return self.message


'''
UnderFlow exception
TODO: when does this happen?
'''
class UnderFlowError(Exception):
	def __init__(self):
		self.message = 'Underflow error!'

	def __str__(self):
		return self.message



'''
Iterator helper for SLL
'''
class SLLIterator:
	def __init__(self, node=None):
		self.node = node

	def __iter__(self):
		return self


	def next(self):
		if not self.node:
			raise StopIteration
		else:
			tmp = self.node
			# Move iterator to next node for next iteration
			self.node = tmp.next
			return tmp.value



'''
The SLL class
'''
class SLL(object):
	# A default print function if no aggregator is provided
	# for traversal functions
	_default_printfn = lambda x,y : sys.stdout.write(str(y))

	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0


	# for len(sll)
	def __len__(self):
		return self.size


	# for if sll: / if not sll: checks
	def __nonzero__(self):
		return self.head != None


	def __str__(self):
		sll_str = '[' + str(self.size) + ']: '
		trav = self.head
		while (trav):
			sll_str += str(trav) + ' '
			trav = trav.next

		return sll_str.strip()



	def __repr__(self):
		return self.__str__()


	def __iter__(self):
		return SLLIterator(self.head)


	#[]
	def __getitem__(self, index):
		if index < 0:
			# Helper function to return nth item 
			# from the end of the SLL
			def _find_last_nth(sll, n):
				trav = sll.head
				try:
					# Start 'trav' with a headstart of 'n' nodes
					for i in range(n):
						trav = trav.next
				
					# Have 'trail' follow 'trav' until
					# trav 'falls off' end of the SLL
					# placing 'trav' at nth node from the end
					trail = sll.head
					while trav:
						trail = trail.next
						trav = trav.next

					return trail.value
				except: # SLL has <n items
					raise IndexError

			# Call helper to return item at 'index' from the right end of the SLL
			return _find_last_nth(self, -index)
		else: # index: >=0, -0 == +0
			trav = self.head
			try:
				for i in range(index):
					trav = trav.next

				return trav.value
			except:
				raise IndexError



	# Create a SLL from a list
	@staticmethod
	def fromList(lst):
		s = SLL()
		for x in lst:
			s.push_back(x)

		return s


	# Return a List constructed from SLL items
	def toList(self):
		l = []
		for x in self:
			l.append(x)

		return l



	# Traverse and print/aggregate SLL items using the aggregator function specified
	def traverse(self, aggregate_fn=_default_printfn, **kwargs):
		trav = self.head
		while (trav):
			aggregate_fn(kwargs, trav.value)
			trav = trav.next



	# Insert at front
	def push_front(self, value):
		node = Node(value)
		self.size += 1

		node.next = self.head
		self.head = node

		if (not self.tail):
			self.tail = node


	# Insert to the rear
	def push_back(self, value):
		node = Node(value)

		self.size += 1

		# No elements in the list
		if not self.tail:
			self.tail = node
			self.head = node
			return

		self.tail.next = node
		self.tail = node


	# remove first element from the SLL
	def pop_front(self):
		if not self.head:
			raise UnderFlowError
			return None

		self.size -= 1
		value = self.head.value
		self.head = self.head.next

		# We just popped the last element in the SLL,
		# Update tail
		if self.size == 0:
			self.tail = None

		return value


	# remove last element from the SLL	
	def pop_back(self):
		if not self.head:
			raise UnderFlowError
			return None

		self.size -= 1
		value = self.tail.value

		# There was only 1 element in the SLL
		if self.size == 0:
			self.head = self.tail = None
			return value

		trav = self.head
		# traverse until we reach the penultimate node in the SLL
		while trav.next != self.tail:
			trav = trav.next

		# make penultimate node the new tail, and cut old tail from its link
		trav.next = None
		self.tail = trav

		return value



	# find node matching an item and return it
	def findMatchingNode(self, item, comparatorfn=cmp):
		trav = self.head
		while trav:
			if comparatorfn(item, trav.value) == 0:
				return trav
			trav = trav.next

		return None


	# find and return matching item from the SLL, if it exists
	def find(self, item, comparatorfn=cmp):
		node = self.findMatchingNode(item, comparatorfn)
		if not node:
			return None

		return node.value



	# Find and remove a matching node from the SLL
	def remove(self, item, comparatorfn=cmp):
		tmp = self.head
		prev = None
		while tmp and comparatorfn(tmp.value,item) !=0:
			prev = tmp
			tmp = tmp.next

		# Couldn't find item in the queue
		if not tmp:
			return None

		prev.next = tmp.next
		self.size -= 1

		tmp.next = None # sanitize 'tmp' link and remove it from the chain
		if self.size == 0:
			self.head = self.tail = None
		elif tmp == self.tail:
			self.tail = prev
		
		return tmp

	

	# Keep the SLL sorted, every insert places the item at the right place in order to keep the list sorted
	# NOTE: assumes the list is sorted - if all inserts are done using place() it actually would be
	#       A mixture of random push_xxx and place() will not ensure the list is sorted after place()
	#       When in doubt, sort the list first before calling place() for the new item.
	#
	# NOTE: the place() operation _is_ stable
	#    so if (a == b), and place(a) happened before place(b), then index(a) < index(b) in the list
	def place(self, item, comparatorfn=cmp, allowduplicates=True):
		# if comparatorfn is not specified, try to use the item's __cmp__ method,
		# or the default __cmp__ if the item's class hasn't implemented one

		# This is the first item to be 'placed' *OR* 
		# item < head.value => item is less than all elements in the current list,
		# Just add it to the list and return
		if not self.head or comparatorfn(item, self.head.value) < 0:
			self.push_front(item)
			return

		# if (item >= tail.value), append to the end and return
		# Will save traversing all the way to the end, 
		# if 'item' is bigger than all the elements in the current list
		if comparatorfn(item, self.tail.value) >= 0:
			if not allowduplicates and comparatorfn(item, self.tail.value) == 0:
				return
			self.push_back(item)
			return

		trav = self.head
		prev = None
		# Keep traversing until item < trav.value
		while trav and (comparatorfn(item, trav.value) >= 0):
			prev = trav
			trav = trav.next

		# At this point, we have found node trav, s.t
		# prev.value <= item < trav.value
		if not allowduplicates and comparatorfn(item, prev.value) == 0:
			return

		# Insert item between prev and trav
		node = Node(item)
		node.next = trav
		prev.next = node

		# Can't forget to update size
		self.size += 1


	# Reverse an SLL(iterative version)
	# Consider 3 nodes, x->y->z
	# a,b,c = x,y,z
	# Star with reversing a->b to a<-b,
	# then hop onto y,z,..., with a=y,b=z,... and repeat
	def reverse(self):
		if not self.head:
			return None

		a = self.head
		b = a.next
		while b:
			c = b.next

			# Make b->a link
			b.next = a

			a = b
			b = c

		# Mark erstwhile  head.next to None, so the SLL chain ends
		self.head.next = None 

		# When all's done, 'a' is pointing to the 'tail'
		# of the SLL
		# Since we have now reversed, point 'head' to 'a',
		# but before that, Update 'tail' to erstwhile 'head'
		self.tail = self.head
		self.head = a



