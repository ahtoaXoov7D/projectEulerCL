# A Binary Tree

import sys

sys.path.append("../../../")
from data_structures.sll.queue import Queue # import just the Queue, as sll.Node will conflict with binary_tree.node
from data_structures.sll.sll import SLL
from node import Node
from  data_structures.sll.sll import UnderFlowError
from data_structures.dll.deque import Deque

class BinaryTree:
	# A default print function if no aggregator is provided
	# for traversal functions
	_default_printfn = lambda x,y : sys.stdout.write(str(y))

	def __init__(self, root=None, size=0):
		self.root = root
		self.size = size

		# Use path_1 as the default implementation for path()
		self.path = self.path_1


	'''
	Create a binary tree from an array representation of items in the tree
	'''
	@staticmethod
	def fromList(array):
		from tree_maker import TreeMaker
		return TreeMaker.fromList(array)


	'''
	Create a binary tree from inorder and preorder traversals
	'''
	@staticmethod
	def from_traversal(inorder, preorder=None, postorder=None):
		from tree_maker import TreeMaker

		# Inorder traversasl is required to build an unique tree
		if not inorder:
			return None

		if preorder:
			return TreeMaker.from_traversal_in_pre(inorder, preorder)
		elif postorder:
			return TreeMaker.from_traversal_in_post(inorder, postorder)

		# atleast one of preorder/postorder traversal is needed to build the tree
		return None


	'''
	Calculate height of the binary tree
	'''
	def height(self):
		# helper function to calculate height of a subtree rooted at 'root'
		def _height(root):
			if (not root):
				return 0

			if root.isLeaf():
				return 1
			return (1 + max(_height(root.left), _height(root.right)))

		# call helper function to calculate height of the entire tree
		return _height(self.root)


	'''
	Calculate width of the binary tree
	width = max number of nodes at any level
	'''
	def width(self):
		if not self.root:
			return 0

		q = Queue()
		q.enqueue((0, self.root))

		curr_level = 0
		curr_level_nodes = 0
		max_width = 0
		while q.length() != 0:
			level, node = q.dequeue()

			q.enqueue((level+1, node.left))  if node.left else None
			q.enqueue((level+1, node.right)) if node.right else None

			# Start of a new level
			# Check if number of nodes at previous level > mqx nodes at any level
			if level != curr_level:
				if curr_level_nodes > max_width:
					max_width = curr_level_nodes

				# start counting nodes for the current level
				curr_level_nodes = 0

			curr_level_nodes += 1
			curr_level = level

		# Check last level
		if curr_level_nodes > max_width:
			max_width = curr_level_nodes
		return max_width



	'''
	Calculate span of the binary tree, i.e. 
	the max left + right widths of any node from root
	Do a bfs traversal, capturing left and right widths
	span = max(left width) + max(right width)
	'''
	def span(self):
		if not self.root:
			return 0

		q = Queue()
		min_width = 0
		max_width = 0
		q.enqueue((0, self.root))

		while q.length() != 0:
			width, node = q.dequeue()

			if width < min_width:
				min_width = width
			elif width > max_width:
				max_width = width

			q.enqueue((width-1, node.left))  if node.left else None
			q.enqueue((width+1, node.right)) if node.right else None

		return max_width - min_width




	'''
	preorder traversal: (R,l,r, l:left, r:right, R:Root)
	Traverse binary tree nodes in pre-order and return their values
	if no aggregate function callback is specified,
	just print the current node's contents
	'''
	def preorder_traversal(self, aggregate_fn=_default_printfn, **kwargs):
		# helper function to traverse a Binary subtree rooted at 'root', in preorder
		def _preorder_traversal(root, aggregate_fn, **kwargs):
			if not root:
				return

			aggregate_fn(kwargs, root.value)
			_preorder_traversal(root.left, aggregate_fn, **kwargs) 
			_preorder_traversal(root.right, aggregate_fn, **kwargs)

		# Call the helper function to do the actual traversal
		_preorder_traversal(self.root, aggregate_fn, **kwargs)



	'''
	post-order traversal (l,r,R, l:left, r:right, R:Root)
	Traverse binary tree nodes in post-order and return their values
	if no aggregate function callback is specified,
	just print the current node's contents
	'''
	def postorder_traversal(self, aggregate_fn=_default_printfn, **kwargs):
		# helper function to traverse a Binary subtree rooted at 'root', in postorder
		def _postorder_traversal(root, aggregate_fn, **kwargs):
			if not root:
				return

			_postorder_traversal(root.left, aggregate_fn, **kwargs) 
			_postorder_traversal(root.right, aggregate_fn, **kwargs)
			aggregate_fn(kwargs, root.value)

		# Call the helper function to do the actual traversal
		_postorder_traversal(self.root, aggregate_fn, **kwargs)



	'''
	In-order traversal (l,r,R, l:left, r:right, R:Root)
	Traverse binary tree nodes in in-order and return their values
	if no aggregate function callback is specified,
	just print the current node's contents
	'''
	def inorder_traversal(self, aggregate_fn=_default_printfn, **kwargs):
		# helper function to traverse a Binary subtree rooted at 'root', in In-order
		def _inorder_traversal(root, aggregate_fn, **kwargs):
			if not root:
				return

			_inorder_traversal(root.left, aggregate_fn, **kwargs) 
			aggregate_fn(kwargs, root.value)
			_inorder_traversal(root.right, aggregate_fn, **kwargs)

		# Call the helper function to do the actual traversal
		_inorder_traversal(self.root, aggregate_fn, **kwargs)



	'''
	Level-order traversal
	Traverse binary tree nodes level by level, and return their values
	if no aggregate function callback is specified,
	just print the current node's contents
	'''
	def levelorder_traversal(self, aggregate_fn=_default_printfn, **kwargs):
		if not self.root:
			return

		q = Queue()
		q.enqueue(self.root)
		while q.length() != 0:
			tmp = q.dequeue()
			aggregate_fn(kwargs, tmp.value)

			q.enqueue(tmp.left)  if tmp.left else None
			q.enqueue(tmp.right) if tmp.right else None



	'''
	Left-view of a binary tree
	Return tree items that would be seen from the left side of the binary tree
	'''
	def left_view(self, aggregate_fn=_default_printfn, **kwargs):
		if not self.root:
			return

		q = Queue()
		levels_done = None
		q.enqueue((0, self.root))
		while q.length() != 0:
			curr_level, node = q.dequeue()

			# Nothing has been printed in this level so far
			# NOTE: (None < 0) in python
			if curr_level > levels_done:
				aggregate_fn(kwargs, node.value)
				levels_done = curr_level

			q.enqueue((curr_level+1, node.left))  if node.left else None
			q.enqueue((curr_level+1, node.right)) if node.right else None



	'''
	Right-view of a binary tree
	Return tree items that would be seen from the right side of the binary tree
	'''
	def right_view(self, aggregate_fn=_default_printfn, **kwargs):
		if not self.root:
			return

		q = Queue()
		q.enqueue((0, self.root))
		while q.length() != 0:
			curr_level, node = q.dequeue()

			q.enqueue((curr_level+1, node.left))  if node.left else None
			q.enqueue((curr_level+1, node.right)) if node.right else None

			# peek next node in the queue to see if this is the last node in the current level
			# if yes, print it
			try:
				(level,next_entry) = q.front()
			except UnderFlowError:
				(level,next_entry) = (None, None)


			# Queue is either empty, in which case this is the rightmost node in the last level
			# *OR*, next entry in the queue is for the level after this one, so this is the rightmost in the current level
			# In both cases, current node would be visible in a right-view.
			if (not next_entry) or (level > curr_level):
				aggregate_fn(kwargs, node.value)



	'''
	Top-view of a binary tree
	Return the node items that would be seen from the top of the binary tree
	NOTE: The left-right and right-left grandchildren-nodes of a node overlap, and are masked by the grandfather node
	e.g.
	    a
	   / \
      b   c
	 /  \/ \
	d   ef  g
	Top-view of the tree rooted at a, node 'a' masks nodes LR-grandchild node 'e', and RL-grandchild node 'f'
	
	Vizualize the algorithm as an cone increasing in diameter, and printing all the nodes on the edge of the cone,
	(assume the tree is completely full), and ignoring everything within the cone itself as they would be masked by
	the outer nodes when viewed from the top.
	'''
	def top_view(self, aggregate_fn=_default_printfn, **kwargs):
		if not self.root:
			return

		q = Queue()
		min_width = 0
		max_width = 0
		q.enqueue((0, self.root))

		# Top-view begins with the root node
		aggregate_fn(kwargs, self.root.value)
		while q.length() != 0:
			width, node = q.dequeue()

			if width < min_width:
				min_width = width
				aggregate_fn(kwargs, node.value)
			elif width > max_width:
				max_width = width
				aggregate_fn(kwargs, node.value)

			# NOTE: width 0, is root, would already be filled in at root,
			# and in a top-view is not going to replaced

			q.enqueue((width-1, node.left))  if node.left else None
			q.enqueue((width+1, node.right)) if node.right else None



	'''
	Top-view of a binary tree, but ordered from Left->Right, width-wise
	Return the node items that would be seen from the top of the binary tree, but after ordering them from left->right
	NOTE: The left-right and right-left grandchildren-nodes of a node overlap, and are masked by the grandfather node
	e.g.
	    a
	   / \
      b   c
	 /  \/ \
	d   ef  g
	Top-view of the tree rooted at a, node 'a' masks nodes LR-grandchild node 'e', and RL-grandchild node 'f'
	In the sample tree above,
	traditional top-view (level by level) would be
	  a b c d g
	whereas, a L-R top-view would yield
	 d b a c g
	'''
	def top_view_LR(self, aggregate_fn=_default_printfn, **kwargs):
		if not self.root:
			return

		# Queue to help with level-order traversal
		q = Queue()

		# Store L/R width of a node and its value if it is visible in the top-view, in a sorted list
		# ordered by the width
		# at the end of the level-order traversal the list would contain
		# [(-max_left_width, node value), ...., (0, root.value), ... (max_right_width, node value)]
		slist = SLL()

		# pairs a(w1, node_val1) vs b(w2, node_val2) are valued against each other
		# depending on w1 vs w2 (where w1 and w2 are widths, so slist is kept sorted by the nodes' L/R widths)
		pair_comparator = lambda (w1, node_val1), (w2, node_val2): cmp(w1, w2)

		min_width = 0
		max_width = 0
		q.enqueue((0, self.root))

		# Top-view begins with the root node
		slist.place((0, self.root.value))
		while q.length() != 0:
			width, node = q.dequeue()

			if width < min_width:
				min_width = width
				slist.place((width, node.value))
			elif width > max_width:
				max_width = width
				slist.place((width, node.value))

			# NOTE: width 0, is root, would already be filled in at root,
			# and in a top-view is not going to replaced

			q.enqueue((width-1, node.left))  if node.left else None
			q.enqueue((width+1, node.right)) if node.right else None


		# At the end of the level-order traversal,
		# slist is ordered by width, so
		# (-max_left_width, ..., 0, ..., max_right_width)
		# Just retrieve the SLL L-R for the top view (L-R)
		while slist.size!= 0:
			width, item = slist.pop_front()
			aggregate_fn(kwargs, item)



	'''
	Bottom-view of a binary tree
	Return the nodes that would be seen from the bottom side of the binary tree
	'''
	def bottom_view(self, aggregate_fn=_default_printfn, **kwargs):
		if not self.root:
			return

		q = Queue()

		# A hash table that stores a map of L/R width to a node's item
		# We traverse the tree in level-order, and keep replacing slist[width] if we find a new node with the same width
		# At the end of the traversal, every slist[width] from {-max_left_width, ...,  0, ..., max_right_width} will contain the
		# node items that would be visible from a bottom view of the binary tree
		slist = {}

		min_width = 0
		max_width = 0
		q.enqueue((0, self.root))

		# Star with placing root at width 0
		slist[0] = self.root.value
		while q.length() != 0:
			width, node = q.dequeue()

			# As we traverse level-by-level, keep replacing
			# item at L/R width
			slist[width] = node.value

			# Track max_left_width, max_right_width
			# so we don't need to sort the hash table slist,
			# Just retrieve slist[{-max_left_width, ...,  0, ..., max_right_width}]
			if width < min_width:
				min_width = width
			elif width > max_width:
				max_width = width

			q.enqueue((width-1, node.left))  if node.left else None
			q.enqueue((width+1, node.right)) if node.right else None

		# At the end of the level-order traversal,
		# Just 'aggregate' slist[{-max_left_width, ...,  0, ..., max_right_width}]
		for i in range(min_width, max_width+1):
			aggregate_fn(kwargs, slist[i])



	'''
	Use a deque for an intermediate structure, defer traversing any level until all the nodes from that level are in the deque
	Always enqueue from the rear end.
	Dequeue from front if odd (LIFO), else back (FIFO)
	    a
	   / \
      b   c
	 /  \/ \
	d   ef  g
   /         \
  h           i
	traversal = []

	bfs_q: {(a,0)}
	pop: (a,0)
	 add to deque:
	 deq: [a]
	bfs_q: add (b,1), (c,1)
	  bfs_q level: 1 > 0 ==> flush deque (L-R)
	  traversal = [a]
	
	pop(bfs_q): (b,1)
	  add to deque: [b]
	bfs_q: add(d,2), (e.2) 
	bfs_q: {(c,1), (d,2), (e,2)}

	pop(bfs_q): (c,1)
	 add to deque: [b, c]
	bfs_q: add(f,2), (g.2) 
	bfs_q: {(d,2), (e,2), (f,2), (g,2)}
	  q_level: 2 > 1 => flush deque (R-L)
	  traversal = [a,c,b]

	pop(bfs_q): (d,2)
	  add to deque: [d]
	bfs_q: add(h,3)
	bfs_q: {(e,2), (f,2), (g,2), (h,3)}

	pop(bfs_q): (e,2)
	  add to deque: [d,e]
	bfs_q: {(f,2), (g,2), (h,3)}

	pop(bfs_q): (f,2)
	  add to deque: [d,e,f]
	bfs_q: {(g,2), (h,3)}

	pop(bfs_q): (g,2)
	  add to deque: [d,e,f,g]
	bfs_q: add(i, 3)
	bfs_q: {(h,3), (i,3)}
	  q_level: 3 > 2 => flush deque (L-R)
	  traversal = [a,c,b,d,e,f,g]

	pop(bfs_q): (h,3)
	  add to deque: [h]
	bfs_q: {(i,3)}

	pop(bfs_q): (i,3)
	  add to deque: [h,i]
	bfs_q: {}

	current level: 3 => flush deque (R-L)
	  traversal = [a,c,b,d,e,f,g,i,h]
	'''
	def zigzag_levelorder_traversal(self, aggregate_fn=_default_printfn, **kwargs):
		# Helper function to flush deque
		def flush():
			# odd: R-L
			if curr_level & 1:
				while deq:
					aggregate_fn(kwargs, deq.pop_back())
			else: # even: L-R
				while deq:
					aggregate_fn(kwargs, deq.pop_front())


		# start zig-zag traversal
		if not self.root:
			return

		bfs_q = Queue()
		deq = Deque()

		bfs_q.enqueue((0, self.root))
		curr_level = 0
		while bfs_q:
			curr_level, node = bfs_q.dequeue()
			deq.push_back(node.value)
			bfs_q.enqueue((curr_level+1, node.left)) if node.left else None
			bfs_q.enqueue((curr_level+1, node.right)) if node.right else None

			# We just popped the last node for current level
			# flush deque L-R if curr_level is even
			# R-L if curr_level is odd
			if bfs_q and bfs_q.front()[0] > curr_level:
				flush()
			

		# At the end, we are left with nodes from the last level in the deque
		flush()



	'''
	Return a path, as a list of nodes, from root to the specified node in the binary tree
	'''
	def path_n(self, data):
		'''
		Find path to 'node' from the subtree rooted at 'root'
		and append each node in the path to the list
		Steps:
		  1. Start a pre-order traversal
		  2. Find path to node in left subtree, if not found, find in the right subtree
		  3. If either of the left subtree/ right subtree returns True, indicating subtree contains the node,
		       add current root node to list and return True to higher level calls
		  4. If a subtree's root matches node, we have hit the node we were looking for, start constructing
		     path from here -> add node to list. return True
		'''
		def path_helper(root, node, path_nodes):
			if not root:
				return False
			
			# Found node in the subtree
			# add it to the path and return true
			# else, recursively look for it in the left/right subtree
			if root.value == node.value:
				path_nodes.insert(0, root)
				return True
			elif path_helper(root.left, node, path_nodes):
				path_nodes.insert(0, root)
				return True
			elif path_helper(root.right, node, path_nodes):
				path_nodes.insert(0, root)
				return True

				
		if not data:
			return []

		# Find path to a node with value mentioned in 'data'
		if not isinstance(data, Node):
			node = Node(data)
		else:
			node = data

		paths = []
		path_helper(self.root, node, paths)
		return paths



	'''
	Return a path, as a list of node items, from root to the specified item in the binary tree
	'''
	def path_1(self, data):
		'''
		Find path to 'item' from the subtree rooted at 'root'
		and append each item in the path to the list
		Steps:
		  1. Start a pre-order traversal
		  2. Find path to item in left subtree, if not found, find in the right subtree
		  3. If either of the left subtree/ right subtree returns True, indicating subtree contains the item,
		       add current root node to list and return True to higher level calls
		  4. If a subtree's root matches item, we have hit the node we were looking for, start constructing
		     path from here -> add item to list. return True
		'''
		def path_helper(root, item, path):
			if not root:
				return False
			
			# Found item in the subtree
			# add it to the path and return true
			# else, recursively look for it in the left/right subtree
			if root.value == item:
				path.insert(0, item)
				return True
			elif path_helper(root.left, item, path):
				path.insert(0, root.value)
				return True
			elif path_helper(root.right, item, path):
				path.insert(0, root.value)
				return True

				
		if not data:
			return []

		paths = []
		path_helper(self.root, data, paths)
		return paths



	'''
	Return a path, as a list of node items, from root to the specified item in the binary tree
	'''
	def path_2(self, data):
		'''
		Find path to 'item' from the subtree rooted at 'root'
		and append each item in the path to the list
		Steps:
		  1. Start a pre-order traversal
		  2. Add prefix indicating current path until a match is found.
		     the prefix stores the path to the current node from root
		     using the recursion stack to add and remove paths
		'''
		def path_helper(root, item, prefix, path):
			if not root:
				return
			
			# Found item in the subtree
			# copy all items from the prefix so far + current item
			# else, recursively look for it in the left/right subtree
			if root.value == item:
				path += prefix + [item]
				return

			path_helper(root.left, item, prefix + [root.value], path)
			path_helper(root.right, item, prefix + [root.value], path)
				
		if not data:
			return []

		paths = []
		path_helper(self.root, data, [], paths)
		return paths



	'''
	Return a node that is the Lowest common ancestor
	between two 2 nodes in the binary tree
	Algorithm: (paths-based)
	  Get paths from root to both nodes
	  Compare nodes in the paths until they diverge
	   the node at which they diverge is the LCA node
	'''
	def lca_p(self, node1, node2):
		path1 = self.path_n(node1)
		path2 = self.path_n(node2)
		lca_node = None
		i = 0
		try:
			while path1[i] == path2[i]:
				lca_node = path1[i]
				i += 1
		except IndexError:
			# Do nothing on reaching the end of either paths
			# proceed to return stored lca, if any
			pass

		return lca_node


	'''
	Return a node that is the Lowest common ancestor
	between two 2 nodes in the binary tree
	Algorithm: (Efficient version)
	  Instead of getting paths to either nodes and return the lca as the 
	  last node that diverges in their paths, (using additional storage for paths)
	  Traverse the tree pre-order, and return the node whose left and right children return n1 and n2
	  Each node returns 
	    None if its subtree does not contain neither n1 or n2
	    n1 if its subtree contains n1, n2 if its subtree contains n2
	    if its subtree contains both, returns node itself as LCA
	    We return the (non-null) node returned to root as LCA
	NOTE: As an optimization, anytime an lca is already found, we check if the subtree's return value is neither n1 nor n2
	      and stop computing lca
	      eg
             a
          /     \
         b       c
       /   \    /  \
      d     e  f    g
	  LCA(d,e) = b
	  LCA(b,d,e) == b
	  LCA(root, d,e) == b != e,d => we have found LCA
	  dont have to look in the right subtree
	'''
	def lca(self, n1, n2):
		# Helper function to recursively find lca
		def _lca_(root, node1, node2):
			if not root:
				return None

			# Located either node1 or node2
			if root.value == node1.value or root.value == node2.value:
				return root

			left = _lca_(root.left, node1, node2)

			# return value of left subtree is neither node1 or node2
			# => LCA has been found
			# Just propagate this LCA up, no new calls needed
			if left and left.value != node1.value and left.value != node2.value:
				return left

			right = _lca_(root.right, node1, node2)

			# Found LCA
			if left is not None and right is not None:
				return root

			# Either both left and right subtrees returned None at this point
			# or one of left/right subtrees returned None
			# return non-None node if possible, 
			# else return None if both were None (indicating neither n1/n2 were found in this subtree)
			return left if left else right


		# wrap n in an node if its a data item
		# else return node as-is if its of type Node.
		wrap_node = lambda n: Node(n) if not isinstance(n, Node) else n
		node1 = wrap_node(n1)
		node2 = wrap_node(n2)
		return _lca_(self.root, node1, node2)


