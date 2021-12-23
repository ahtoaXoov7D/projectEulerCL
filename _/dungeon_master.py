#encoding: utf-8

'''
https://open.kattis.com/problems/dungeon

You are trapped in a 3D dungeon and need to find the quickest way out! The dungeon is composed of unit cubes which may or may not be filled with rock. It takes one minute to move one unit north, south, east, west, up or down. You cannot move diagonally and the maze is surrounded by solid rock on all sides.

Is an escape possible? If yes, how long will it take?

Input Specification
The input file consists of a number of dungeons. Each dungeon description starts with a line containing three integers 𝐿, 𝑅 and 𝐶 (all limited to 30 in size). 𝐿 is the number of levels making up the dungeon. 𝑅 and 𝐶 are the number of rows and columns making up the plan of each level.

Then there will follow 𝐿 blocks of 𝑅 lines each containing 𝐶 characters. Each character describes one cell of the dungeon. A cell full of rock is indicated by a ’#’ and empty cells are represented by a ’.’. Your starting position is indicated by ’S’ and the exit by the letter ’E’. There’s a single blank line after each level. Input is terminated by three zeroes for 𝐿, 𝑅 and 𝐶.

Output Specification
Each maze generates one line of output. If it is possible to reach the exit, print a line of the form
Escaped in <x> minute(s).
where <x> is replaced by the shortest time it takes to escape. If it is not possible to escape, print the line
Trapped!

Sample Input 1
3 4 5
S....
.###.
.##..
###.#

#####
#####
##.##
##...

#####
#####
#.###
####E

1 3 3
S##
#E#
###

0 0 0

Sample Output 1
Escaped in 11 minute(s).
Trapped!
'''

# Upon finding the end cell, the BFS solve() method raises this exception
# to avoid any further processing
# and return the result immediately
class FoundEndCellError(Exception):
	def __init__(self):
		pass


class Dungeon(object):
	def __init__(self, l, r, c):
		self.l, self.r, self.c = l, r, c
		self.dungeon = [[[None] * c for _ in xrange(r)] for _ in xrange(l)]
		self.start = None
		self.end = None

	def read_map(self, local_input=None):
		dungeon = self.dungeon
		l, r, c = self.l, self.r, self.c
		for i in xrange(l):
			for j in xrange(r):
				row = raw_input()
				for k in xrange(c):
					dungeon[i][j][k] = row[k]
					if row[k] == 'S':
						# Mark start cell as visited
						# right at the outset
						dungeon[i][j][k] = '#'
						self.start = (i,j,k)
					if row[k] == 'E':
						self.end = (i,j,k)
			_ = raw_input() # blank lines between levels


	# Find a minimum-distance path from start -> end
	# and return the time
	def solve(self):
		try:
			bfs_q = [(self.start, 0)]
			while bfs_q:
				current, t = bfs_q.pop(0)

				# helper function to add to the bfs queue
				# mark current grid as '#' so its not revisited again
				def add_to_queue(x,y,z):
					if self.end == (x,y,z):
						# Found end grid in the dungeon
						print 'Escaped in {0} minute(s).'.format(t+1)
						raise FoundEndCellError
					self.dungeon[x][y][z] = '#'
					bfs_q.append(((x,y,z), t+1))


				i,j,k = current
				# Enqueue up and down levels
				add_to_queue(i+1, j, k) if (i+1 < self.l and self.dungeon[i+1][j][k] != '#') else None
				add_to_queue(i-1, j, k) if (i-1 >= 0 and self.dungeon[i-1][j][k] != '#') else None

				# Enqueue left, right, top, below grids in the same level
				add_to_queue(i, j+1, k) if (j+1 < self.r and self.dungeon[i][j+1][k] != '#') else None
				add_to_queue(i, j-1, k) if (j-1 >= 0 and self.dungeon[i][j-1][k] != '#') else None
				add_to_queue(i, j, k+1) if (k+1 < self.c and self.dungeon[i][j][k+1] != '#') else None
				add_to_queue(i, j, k-1) if (k-1 >= 1 and self.dungeon[i][j][k-1] != '#') else None

			# Couldn't reach end cell
			print 'Trapped!'
		except FoundEndCellError:
			return


if __name__ == '__main__':
	while True:
		l, r, c = map(int, raw_input().split())
		# 0 0 0 => terminate input
		if (l,r,c) == (0,0,0):
			break

		d = Dungeon(l,r,c)
		d.read_map()
		d.solve()

