'''
https://leetcode.com/problems/maximum-width-of-binary-tree/

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:
Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).


Example 2:
Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).

Example 3:
Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).

Example 4:
Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Example 5:
Input: 

          1
         / \
        3   2
             \  
              9 
               \
                7
Output: 2
Explanation:The maximum width existing in the second level with the length 2 (3,2)


Note: Answer will in the range of 32-bit signed integer.
'''


'''
Solution outline:
  0. Do a BFS
  1. Capture number of nodes at each level
     Keep a track of the left-most position where a non-empty node exists,
	 Keep updating of right-most position where a non-empty node end in the level
	 width at end of any level = (right - left + 1)
  3. Return max of width at any level
'''



class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.value)

	def __repr__(self):
		return str(self.value)


class Solution(object):
	def widthOfBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0

		curr_level = 0
		max_width = 0
		all_nodes = 0
		left_position = None
		right_position = None

		q = [(0,root)]
		while q:
			(level,node) = q.pop(0)
			if node:
				q.append((level+1, node.left))
				q.append((level+1, node.right))
			else:
				q.append((level+1, None))
				q.append((level+1, None))

			# We have moved to the next level
			# Check if previous level's width is higher than all widths seen so far
			if curr_level != level:
				curr_level = level

				# There were no nodes at previous level
				# we have covered all levels in the tree
				if left_position is None:
					break

				# Current level's width > max
				curr_width = right_position - left_position + 1
				if curr_width > max_width:
					max_width = curr_width

				# reset current level nodes
				all_nodes = 0
				left_position = None
				right_position = None

			all_nodes +=1
			if node:
				if left_position is None:
					left_position = all_nodes

				right_position = all_nodes

		return max_width


if __name__ == '__main__':
	s = Solution()
	root = Node(1)
	root.right = Node(2)
	assert s.widthOfBinaryTree(root) == 1

	root = Node(1)
	root.left = Node(3)
	root.right = Node(2)
	root.left.left = Node(5)
	root.left.right = Node(3)
	root.right.right = Node(9)
	assert s.widthOfBinaryTree(root) == 4

	root2 = Node(1)
	root2.left = Node(3)
	root2.left.left = Node(5)
	root2.left.right = Node(3)
	assert s.widthOfBinaryTree(root2) == 2

	root3 = Node(1)
	root3.left = Node(3)
	root3.left.left = Node(5)
	root3.right = Node(2)
	assert s.widthOfBinaryTree(root3) == 2

	root4 = Node(1)
	root4.right = Node(2)
	root4.left = Node(3)
	root4.left.left = Node(5)
	root4.right.right = Node(9)
	root4.left.left.left = Node(6)
	root4.right.right.right = Node(7)
	assert s.widthOfBinaryTree(root4) == 8

	root5 = Node(1)
	root5.right = Node(2)
	root5.left = Node(3)
	root5.right.right = Node(9)
	root5.right.right.right = Node(7)
	assert s.widthOfBinaryTree(root5) == 2
