/**
https://www.interviewbit.com/problems/sudoku/

Sudoku

Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'
You may assume that there will be only one unique solution.

+===+===+===+===+===+===+===+===+===+
❚ 5 | 3 |   ❚   | 7 |   ❚   |   |   ❚
+---+---+---+---+---+---+---+---+---+
❚ 6 |   |   ❚ 1 | 9 | 5 ❚   |   |   ❚
+---+---+---+---+---+---+---+---+---+
❚   | 9 | 8 ❚   |   |   ❚   | 6 |   ❚ 
+===+===+===+===+===+===+===+===+===+
❚ 8 |   |   ❚   | 6 |   ❚   |   | 3 ❚
+---+---+---+---+---+---+---+---+---+
❚ 4 |   |   ❚ 8 |   | 3 ❚   |   | 1 ❚
+---+---+---+---+---+---+---+---+---+
❚ 7 |   |   ❚   | 2 |   ❚   |   | 6 ❚
+===+===+===+===+===+===+===+===+===+
❚   | 6 |   ❚   |   |   ❚ 2 | 8 |   ❚
+---+---+---+---+---+---+---+---+---+
❚   |   |   ❚ 4 | 1 | 9 ❚   |   | 5 ❚
+---+---+---+---+---+---+---+---+---+
❚   |   |   ❚   | 8 |   ❚   | 7 | 9 ❚
+===+===+===+===+===+===+===+===+===+

A sudoku puzzle,

+===+===+===+===+===+===+===+===+===+
❚ 5 | 3 | 𝟜 ❚ 𝟞 | 7 | 𝟠 ❚ 𝟡 | 𝟙 | 𝟚 ❚
+---+---+---+---+---+---+---+---+---+
❚ 6 | 𝟟 | 𝟚 ❚ 1 | 9 | 5 ❚ 𝟛 | 𝟜 | 𝟠 ❚
+---+---+---+---+---+---+---+---+---+
❚ 𝟙 | 9 | 8 ❚ 𝟛 | 𝟜 | 𝟚 ❚ 𝟝 | 6 | 𝟟 ❚ 
+===+===+===+===+===+===+===+===+===+
❚ 8 | 𝟝 | 𝟡 ❚ 𝟟 | 6 | 𝟙 ❚ 𝟜 | 𝟚 | 3 ❚
+---+---+---+---+---+---+---+---+---+
❚ 4 | 𝟚 | 𝟞 ❚ 8 | 𝟝 | 3 ❚ 𝟟 | 𝟡 | 1 ❚
+---+---+---+---+---+---+---+---+---+
❚ 7 | 𝟙 | 𝟛 ❚ 𝟡 | 2 | 𝟜 ❚ 𝟠 | 𝟝 | 6 ❚
+===+===+===+===+===+===+===+===+===+
❚ 𝟡 | 6 | 𝟙 ❚ 𝟝 | 𝟛 | 𝟟 ❚ 2 | 8 | 𝟜 ❚
+---+---+---+---+---+---+---+---+---+
❚ 𝟚 | 𝟠 | 𝟟 ❚ 4 | 1 | 9 ❚ 𝟞 | 𝟛 | 5 ❚
+---+---+---+---+---+---+---+---+---+
❚ 𝟛 | 𝟜 | 𝟝 ❚ 𝟚 | 8 | 𝟞 ❚ 𝟙 | 7 | 9 ❚
+===+===+===+===+===+===+===+===+===+

and its solution numbers marked in red.

Example :
For the above given diagrams, the corresponding input to your program will be
	[[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]
and we would expect your program to modify the above array of array of characters to
	[[534678912], [672195348], [198342567], [859761423], [426853791], [713924856], [961537284], [287419635], [345286179]]
*/

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

/* print a sudoku board */
void print(char **grid)
{
	int row=0, col=0;
	for (row=0; row<9; row++) {
		for (col=0; col<9; col++) {
			printf("%c ", ((char (*)[9])grid)[row][col]);
		}
		printf("\n");
	}
}

/**
 * check if it's safe to put in
 * 'n' in the grid at (x,y)
 */
int is_safe(char **pgrid, int x, int y, int n)
{
	char (*grid)[9] = (char (*)[9])pgrid;
	int i, j;

	// check row x
	for (j=0; j<9; j++)
		if (grid[x][j] == n)
			return 0;

	// check column y
	for (i=0; i<9; i++)
		if (grid[i][y] == n)
			return 0;

	// check the 3x3 grid
	// The 3x3 grids are
	// (0,0)->(2,2), (0,3)->(2,5), (0,6)->(2,8)
	// (3,0)->(5,2), (3,3)->(5,5), (3,6)->(5,8)
	// (6,0)->(8,2), (6,3)->(8,5), (6,6)->(8,8)
	// cell(4,5) is grid (3,3)->(5,5)
	//  (4/3),(5/3) == 1,1 -> *3 = 3,3 (start)
	// cell(7,6) is grid(6,6)->(8,8)
	// (7/3),(6/3) == 2,2 -> *3 == 6,6 (start)
	for (i=0; i<3; i++)
		for (j=0; j<3; j++)
			if ( grid[(x/3)*3+i][(y/3)*3+j] == n )
				return 0;

	return 1;
}

// recursive helper to solve the board
void solveSudokuHelper(char **pgrid, char soln[9][9])
{

	char (*grid)[9] = (char (*)[9])pgrid;
	int i, j, x;
	for (i=0; i<9; i++) {
		for (j=0; j<9; j++) {
			if (grid[i][j] != '.')
				continue;

			for (x=1; x<10; x++)  {
				if (is_safe((char **)grid, i, j, x+'0')) {
					assert(grid[i][j] == '.');
					grid[i][j] = x+'0';
					solveSudokuHelper((char **)grid, soln);
					grid[i][j] = '.'; // backtrack
				}
			}
			return;
		}
	}

	// We have a complete board
	// print((char **)grid);
	for (i=0; i<9; i++)
		for (j=0; j<9; j++)
			soln[i][j] = grid[i][j];
}


/**
 * @input A : 2D char array 
 * @input n11 : char array's ( A ) rows
 * @input n12 : char array's ( A ) columns
 * 
 * @Output Void. Just modifies the args passed by reference 
 */
void solveSudoku(char **pgrid, int n11, int n12)
{
	char (*grid)[9] = (char (*)[9])pgrid;
	char soln[9][9];
	int i, j;

	solveSudokuHelper(pgrid, soln);

	for (i=0; i<9; i++)
		for (j=0; j<9; j++)
			grid[i][j] = soln[i][j];
}


int main(void)
{

	char completed[9][9] = 
			{
				{'5', '3', '4', '6', '7', '8', '9', '1', '2'},
				{'6', '7', '2', '1', '9', '5', '3', '4', '8'},
				{'1', '9', '8', '3', '4', '2', '5', '6', '7'},
				{'8', '5', '9', '7', '6', '1', '4', '2', '3'},
				{'4', '2', '6', '8', '5', '3', '7', '9', '1'},
				{'7', '1', '3', '9', '2', '4', '8', '5', '6'},
				{'9', '6', '1', '5', '3', '7', '2', '8', '4'},
				{'2', '8', '7', '4', '1', '9', '6', '3', '5'},
				{'3', '4', '5', '2', '8', '6', '1', '7', '9'}
			};

	
	{
		char grid[9][9] = 
		{
			{'5', '3', '.', '.', '7', '.', '.', '.', '.'},
			{'6', '.', '.', '1', '9', '5', '.', '.', '.'},
			{'.', '9', '8', '.', '.', '.', '.', '6', '.'},
			{'8', '.', '.', '.', '6', '.', '.', '.', '3'},
			{'4', '.', '.', '8', '.', '3', '.', '.', '1'},
			{'7', '.', '.', '.', '2', '.', '.', '.', '6'},
			{'.', '6', '.', '.', '.', '.', '2', '8', '.'},
			{'.', '.', '.', '4', '1', '9', '.', '.', '5'},
			{'.', '.', '.', '.', '8', '.', '.', '7', '9'}
		};
		assert( is_safe((char **)grid, 0, 2, '6') == 0);
		assert( is_safe((char **)grid, 0, 2, '1') == 1);
		assert( is_safe((char **)grid, 6, 8, '1') == 0);
		assert( is_safe((char **)grid, 6, 8, '1') == 0);
		assert( is_safe((char **)grid, 6, 8, '3') == 0);

		solveSudoku((char **)grid, 9, 9);
		print((char **)grid);

		for (int i=0; i<9; i++)
			for (int j=0; j<9; j++)
				assert (grid[i][j] == completed[i][j]);
	}
	{
		char grid[9][9] = 
		{
			{'5', '3', '.', '.', '7', '.', '.', '.', '.'},
			{'6', '.', '.', '1', '9', '5', '.', '.', '.'},
			{'.', '9', '8', '.', '.', '.', '.', '6', '.'},
			{'8', '.', '.', '.', '6', '.', '.', '.', '3'},
			{'4', '.', '.', '8', '.', '3', '.', '.', '1'},
			{'7', '.', '.', '.', '2', '.', '.', '.', '6'},
			{'.', '6', '.', '.', '.', '.', '2', '8', '.'},
			{'.', '.', '.', '4', '1', '9', '.', '.', '5'},
			{'.', '.', '.', '.', '8', '.', '.', '7', '9'}
		};

		/** Initialize using malloc */
		char (*pgrid)[9] = (char (*)[9])malloc(9*9*sizeof(char));
		for (int i=0; i<9; i++)
			for (int j=0; j<9; j++)
				 pgrid[i][j] = grid[i][j];

		//print((char **)pgrid);
		solveSudoku((char **)pgrid, 9, 9);
		//print((char **)pgrid);
		for (int i=0; i<9; i++)
			for (int j=0; j<9; j++)
				assert (pgrid[i][j] == completed[i][j]);
		free(pgrid);
	}

	return 0;
}


