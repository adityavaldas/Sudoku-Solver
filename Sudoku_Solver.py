import sys
import os
import csv
import logging

class Sudoku_Solver():
	def __init__(self):
		self.board = []
		self.checkSum = 0
		self.createBoard()

	def createBoard(self):
		inFile = 'input.csv'
		args = sys.argv
		if(len(args)>1):
			for item in args:
				if('.csv' in item):
					inFile = item
		if not (os.path.exists(inFile)):
			log.debug('inFile: {}'.format(inFile))
			log.debug('Please make sure of proper input file')
			exit()
		with open(inFile) as f:
			reader = csv.reader(f)
			self.board = list(reader)
		for i in range(len(self.board)):
			for k in range(len(self.board[i])):
				if(self.board[i][k] == ''):
					self.board[i][k] = 0
				else:
					self.board[i][k] = int(self.board[i][k])
		if(len(self.board)!=9):
			log.debug('There should be exactly 9 rows in the table, please check the input file')
			exit()
		for i in range(len(self.board)):
			if(len(self.board[i])!=9):
				log.debug('There should be exactly 9 columns in each row, please check row:{}'.format(i+1))
				exit()

	def printBoard(self):
		print()
		print(self.board[0][0],self.board[0][1],self.board[0][2],'|',self.board[0][3],self.board[0][4],self.board[0][5],'|',self.board[0][6],self.board[0][7],self.board[0][8])
		print(self.board[1][0],self.board[1][1],self.board[1][2],'|',self.board[1][3],self.board[1][4],self.board[1][5],'|',self.board[1][6],self.board[1][7],self.board[1][8])
		print(self.board[2][0],self.board[2][1],self.board[2][2],'|',self.board[2][3],self.board[2][4],self.board[2][5],'|',self.board[2][6],self.board[2][7],self.board[2][8])
		print('------+-------+-------')
		print(self.board[3][0],self.board[3][1],self.board[3][2],'|',self.board[3][3],self.board[3][4],self.board[3][5],'|',self.board[3][6],self.board[3][7],self.board[3][8])
		print(self.board[4][0],self.board[4][1],self.board[4][2],'|',self.board[4][3],self.board[4][4],self.board[4][5],'|',self.board[4][6],self.board[4][7],self.board[4][8])
		print(self.board[5][0],self.board[5][1],self.board[5][2],'|',self.board[5][3],self.board[5][4],self.board[5][5],'|',self.board[5][6],self.board[5][7],self.board[5][8])
		print('------+-------+-------')
		print(self.board[6][0],self.board[6][1],self.board[6][2],'|',self.board[6][3],self.board[6][4],self.board[6][5],'|',self.board[6][6],self.board[6][7],self.board[6][8])
		print(self.board[7][0],self.board[7][1],self.board[7][2],'|',self.board[7][3],self.board[7][4],self.board[7][5],'|',self.board[7][6],self.board[7][7],self.board[7][8])
		print(self.board[8][0],self.board[8][1],self.board[8][2],'|',self.board[8][3],self.board[8][4],self.board[8][5],'|',self.board[8][6],self.board[8][7],self.board[8][8])
		print()

	def getGridNumbers(self,i,j):
		if(i<3):
			if(j<3):
				# logging.info('Grid 1')
				listt = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
			elif(j>=3 and j<6):
				# logging.info('Grid 2')
				listt = [[0,3],[0,4],[0,5],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5]]
			elif(j>5):
				# logging.info('Grid 3')
				listt = [[0,6],[0,7],[0,8],[1,6],[1,7],[1,8],[2,6],[2,7],[2,8]]
		elif(i>=3 and i<6):
			if(j<3):
				# logging.info('Grid 4')
				listt = [[3,0],[3,1],[3,2],[4,0],[4,1],[4,2],[5,0],[5,1],[5,2]]
			elif(j>=3 and j<6):
				# logging.info('Grid 5')
				listt = [[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]]
			elif(j>5):
				# logging.info('Grid 6')
				listt = [[3,6],[3,7],[3,8],[4,6],[4,7],[4,8],[5,6],[5,7],[5,8]]
		elif(i>=6):
			if(j<3):
				# logging.info('Grid 7')
				listt = [[6,0],[6,1],[6,2],[7,0],[7,1],[7,2],[8,0],[8,1],[8,2]]
			elif(j>=3 and j<6):
				# logging.info('Grid 8')
				listt = [[6,3],[6,4],[6,5],[7,3],[7,4],[7,5],[8,3],[8,4],[8,5]]
			elif(j>5):
				# logging.info('Grid 9')
				listt = [[6,6],[6,7],[6,8],[7,6],[7,7],[7,8],[8,6],[8,7],[8,8]]

		nos = []
		for item in listt:
			nos.append(self.board[item[0]][item[1]])
		return (nos)

	def getRowNumbers(self, i, j):
		return(self.board[i].copy())

	def getColNumbers(self, i, j):
		nos = []
		for a in range(len(self.board)):
			# if(a!=i):
			nos.append(self.board[a][j])
		return nos

	def getAdjRowsCols(self, i):
		groups = [[0,1,2], [3,4,5], [6,7,8]]
		for group in groups:
			if(i in group):
				outt = []
				for no in group:
					if(no != i):
						outt.append(no)
				return outt

	def getCurGridMap(self, i, j):
		rowgroups = [[0,1,2], [3,4,5], [6,7,8]]
		colgroups = [[0,1,2], [3,4,5], [6,7,8]]
		lstt = []
		for rowgroup in rowgroups:
			if(i in rowgroup):
				for colgroup in colgroups:
					if(j in colgroup):
						for row in rowgroup:
							for col in colgroup:
								lstt.append([row, col])
						return(lstt)

	def singleOut(self, item, i, j):
		'''Based on other row, other column to see if this is the only
		place where the item number can be placed'''
		# log.debug('Checking for {} possible at {}x{}'.format(item, i, j))
		gridMap = self.getCurGridMap(i, j)
		# log.debug('gridMap: {}'.format(gridMap))
		possiblePlaces = []
		for a in gridMap:
			# log.debug('a:{}, b:{}'.format(a[0],a[1]))
			if(self.board[a[0]][a[1]]==0):
				# log.debug('Checking if {} can be placed at {}x{}'.format(item,a[0],a[1]))
				if((item not in self.getRowNumbers(a[0], 0)) and (item not in self.getColNumbers(0, a[1]))):
					possiblePlaces.append([a[0],a[1]])
		# log.debug('possiblePlaces for {}: {}'.format(item, possiblePlaces))
		if(len(possiblePlaces) == 1):
			if(i == possiblePlaces[0][0] and j == possiblePlaces[0][1]):
				return True
		return False

	def checkRowSingleMissing(self,i,j):
		rowElems = self.getRowNumbers(i,0)
		if(rowElems.count(0)==1):
			# log.debug('Only one empty box in row')
			# log.debug('rowElems: {}'.format(rowElems))
			self.board[i][j] = 45 - sum(rowElems)
			# log.debug('Inserting {} in {}x{}'.format(self.board[i][j],i,j))
			# self.printBoard()
			# input()

	def checkColSingleMissing(self,i,j):
		colElems = self.getColNumbers(0,j)
		if(colElems.count(0)==1):
			self.board[i][j] = 45 - sum(colElems)
			# log.debug('Inserting {} in {}x{}'.format(self.board[i][j],i,j))
			# self.printBoard()
			# input()

	def SolvePosition(self,i,j):
		# log.debug('Solving for position {}x{}'.format(i,j))
		self.checkRowSingleMissing(i,j)
		self.checkColSingleMissing(i,j)
		possibleChoices = [r for r in range(1,10)]
		gridNumbers = self.getGridNumbers(i,j)
		rowNumbers = self.getRowNumbers(i,j)
		colNumbers = self.getColNumbers(i,j)
		# log.debug('Grid numbers: {}'.format(gridNumbers))
		# log.debug('Row numbers:  {}'.format(rowNumbers))
		# log.debug('Col numbers:  {}'.format(colNumbers))
		numsToRemove = gridNumbers + rowNumbers + colNumbers
		# log.debug('numsToRemove:  {}'.format(numsToRemove))
		for item in numsToRemove:
			if(item in possibleChoices):
				possibleChoices.remove(item)
		# log.debug('Possible Choices: {}'.format(possibleChoices))
		if(len(possibleChoices)==1):
			# log.info('self.board[{}][{}]: {}'.format(i,j,self.board[i][j]))
			self.board[i][j] = possibleChoices[0]
			# log.info('self.board[{}][{}]: {}'.format(i,j,self.board[i][j]))
			# log.debug('Inserting {} in {}x{}'.format(possibleChoices[0],i,j))
			# self.printBoard()
			# input()
		for item in possibleChoices:
			if (self.singleOut(item, i, j)):
				self.board[i][j] = item
				# log.debug('Inserting {} in {}x{} '.format(item, i, j))
				# self.printBoard()
				# input()


	def isGridFull(self):
		for row in self.board:
			for item in row:
				# log.debug('Item: {}'.format(item))
				if(item == 0):
					return False
		log.debug('Finished solving')
		self.printBoard()
		return True

	def VerifySolution(self):
		for i in range(len(self.board)):
			rowNums = self.getRowNumbers(i,0)
			if(sum(rowNums)!=45):
				log.debug('Failed check at row {}'.format(i))
				return False
			colNums = self.getColNumbers(0,i)
			if(sum(colNums)!=45):
				log.debug('Failed check at col {}'.format(i))
				return False
		grids = [[1,1], [4,1], [7,1], [4,1], [4,4], [4,7], [7,1], [7,4], [7,7]]
		for grid in grids:
			gridNums = self.getGridNumbers(grid[0],grid[1])
			if(sum(gridNums)!=45):
				log.debug('Failed check at grid containing {}x{}'.format(i,j))
				return False
		return True

	def getCheckSum(self):
		sum = 0
		for i in range(len(self.board)):
			for j in range(len(self.board)):
				sum+=self.board[i][j]
		return sum

	def Solve(self):
		self.printBoard()
		input('Press Enter to solve the board')
		log.debug('Solving the board')
		while True:
			if(self.checkSum == self.getCheckSum()):
				log.debug('Unable to further solve the board')
				self.printBoard()
				exit()
			if(self.isGridFull()):
				break
			self.checkSum = self.getCheckSum()
			for i in range(len(self.board)):
				for k in range(len(self.board[i])):
					if(self.board[i][k]==0):
						self.SolvePosition(i,k)
		if(self.VerifySolution()):
			log.debug('Verified that the solution is correct')

log = logging.getLogger('simple_example')
log.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# if('--d' in sys.argv):
log = logging.getLogger('simple_example')
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)


formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s','%d-%b-%y %H:%M:%S')
ch.setFormatter(formatter)
log.addHandler(ch)
# os.system('cls')
ss = Sudoku_Solver()
ss.Solve()
