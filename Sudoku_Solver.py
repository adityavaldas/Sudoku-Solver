import sys

with open(sys.argv[-1]) as f:
	board = f.read().splitlines()

for i in range(len(board)):
	board[i] = board[i].split(',')
	for j in range(len(board[i])):
		board[i][j] = int(board[i][j])

def solveBoard(bo):
	find = findEmptyBox(bo)
	if not find:
		return True
	else:
		row, col = find
	for i in range(1,10):
		if isBoardValid(bo, i, (row, col)):
			bo[row][col] = i
			if solveBoard(bo):
				return True
			bo[row][col] = 0
	return False

def isBoardValid(bo, num, pos):
	for i in range(len(bo[0])):
		if bo[pos[0]][i] == num and pos[1] != i:
			return False

	for i in range(len(bo)):
		if bo[i][pos[1]] == num and pos[0] != i:
			return False

	box_x = pos[1] // 3
	box_y = pos[0] // 3

	for i in range(box_y*3, box_y*3 + 3):
		for j in range(box_x * 3, box_x*3 + 3):
			if bo[i][j] == num and (i,j) != pos:
				return False
	return True

def printBoard(boo):
	print()
	print(boo[0][0],boo[0][1],boo[0][2],'|',boo[0][3],boo[0][4],boo[0][5],'|',boo[0][6],boo[0][7],boo[0][8])
	print(boo[1][0],boo[1][1],boo[1][2],'|',boo[1][3],boo[1][4],boo[1][5],'|',boo[1][6],boo[1][7],boo[1][8])
	print(boo[2][0],boo[2][1],boo[2][2],'|',boo[2][3],boo[2][4],boo[2][5],'|',boo[2][6],boo[2][7],boo[2][8])
	print('------+-------+-------')
	print(boo[3][0],boo[3][1],boo[3][2],'|',boo[3][3],boo[3][4],boo[3][5],'|',boo[3][6],boo[3][7],boo[3][8])
	print(boo[4][0],boo[4][1],boo[4][2],'|',boo[4][3],boo[4][4],boo[4][5],'|',boo[4][6],boo[4][7],boo[4][8])
	print(boo[5][0],boo[5][1],boo[5][2],'|',boo[5][3],boo[5][4],boo[5][5],'|',boo[5][6],boo[5][7],boo[5][8])
	print('------+-------+-------')
	print(boo[6][0],boo[6][1],boo[6][2],'|',boo[6][3],boo[6][4],boo[6][5],'|',boo[6][6],boo[6][7],boo[6][8])
	print(boo[7][0],boo[7][1],boo[7][2],'|',boo[7][3],boo[7][4],boo[7][5],'|',boo[7][6],boo[7][7],boo[7][8])
	print(boo[8][0],boo[8][1],boo[8][2],'|',boo[8][3],boo[8][4],boo[8][5],'|',boo[8][6],boo[8][7],boo[8][8])
	print()

def findEmptyBox(bo):
	for i in range(len(bo)):
		for j in range(len(bo[0])):
			if bo[i][j] == 0:
				return (i, j)
	return None

printBoard(board)
solveBoard(board)
print("Solving the board")
printBoard(board)
