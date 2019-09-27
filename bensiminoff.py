import random
from copy import deepcopy
import math

class BotPlayer:

	""" Your custom player code goes here, but should implement
		all of these functions. You are welcome to implement
		additional helper functions. You may wish to look at board.py
		to see what functions are available to you.
	"""


	"""
		This strategy revolves around counting how many blank spaces are left on the board. While more than 1/4
		of the board is blank, the algorithm attempts to own the corners and moves pieces to be around the corner.
		When less than 1/4 of the board is blank, the algorithm switches and goes into end of game mode. Here, it
		will iterate through all possible boards and choose the one that creates the most number of new correctly
		colored pieces

	"""

	def __init__(self, gui, color="white"):
		self.color = color
		self.gui = gui

	def get_current_board(self, board):
		self.current_board = board

	def size_move_calc(self, wantMin, valid_moves):
		#stoneCount = count_stones()
		#whiteCount = stoneCount[0]
		#blackCount = stoneCount[1]
		#emptyCount= stoneCount[2]
		#iterofBoards = self.current_board.next_states(self.color)
		#li = dict()
		#for i in iterofBoards:
			#newCount = i.count_stones()
			#if self.color == "black":
			#li[newCount[1]] = i
			#else:
				#li[newCount[0]] = i
		#bestBoardCount = max(li)
		newMoves = dict()
		for move in valid_moves:
			newBoard = deepcopy(self.current_board)
			newBoard.apply_move(move, self.color)
			newCount = newBoard.count_stones()
			if self.color == 2:
				newMoves[newCount[1]] = move
			else:
				newMoves[newCount[0]] = move
		if wantMin:
			bestBMove = min(newMoves)
			return newMoves[bestBMove]
		else:
			bestBMove = max(newMoves)
			return newMoves[bestBMove]




	def calc_distance_to_corner(self,x, y):
		return min([math.sqrt(x**2 + y**2), math.sqrt((x-7)**2 + y**2), math.sqrt(x**2 + (y-7)**2), math.sqrt((x-7)**2 + (y-7)**2)])

	def closest_to_corner(self):
		possible_moves = self.current_board.get_valid_moves(self.color)
		d = dict()
		for i in possible_moves:
			#print(i)
			x = i[0]
			y = i[1]
			d[self.calc_distance_to_corner(x, y)] = i
		return d[min(d)]

	def get_other_color(self, col):
		if col == 1:
			return 2
		else:
			return 1


	def num_traps(self, moves):
		TRAP_SPOTS = [(0,1), (1,0), (0,6), (6,0), (6,1), (1,6), (1,7), (7,1)]
		count = 0
		for i in TRAP_SPOTS:
			for b in moves:
				if b == i:
					count += 1
		return count

	def give_traps(self, better_moves):
		TRAP_SPOTS = [(0,1), (1,0), (0,6), (6,0), (6,1), (1,6), (1,7), (7,1)]
		trM = []
		for i in better_moves:
			newBoard = deepcopy(self.current_board)
			newBoard.apply_move(i, self.color)
			other_col_moves = newBoard.get_valid_moves(self.get_other_color(self.color))
			if len(other_col_moves) <= 1:
				return i
			else:
				d = list()
				for b in other_col_moves:
					d.append((self.num_traps(b), b))
				best_move = max(d)
				trM.append((best_move[0], i))
		if len(trM) == 0:
			return better_moves[0]
		else:
			return max(trM)[1]





	def avoidSquare(self):
		SQUARE_TO_AVOID = [(0,1), (1,0), (6,0),(7,1),(7,6),(6,7),(1,7),(0,6),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(2,1),
		(3,1),(4,1),(5,1),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(5,6),(4,6),(3,6),(2,6)]
		possible_moves = self.current_board.get_valid_moves(self.color)
		better_moves = []
		for i in possible_moves:
			if i not in SQUARE_TO_AVOID:
				better_moves.append(i)
		if len(better_moves) == 0:
			return self.size_move_calc(True, possible_moves)
		else:
			trap_moves = self.give_traps(better_moves)
			return trap_moves







	def get_move(self):
		CORNERS = [(0,0), (7,7), (0,7), (7,0)]
		SQUARE_TO_AVOID = [(0,1), (1,0), (6,0),(7,1),(7,6),(6,7),(1,7),(0,6),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(2,1),
		(3,1),(4,1),(5,1),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(5,6),(4,6),(3,6),(2,6)]
		"""if self.current_board.count_stones()[2] >= 45:
			move = self.closest_to_corner()
			self.current_board.apply_move(move, self.color)
			return 0, self.current_board
		else:
			move = self.max_size_move()
			self.current_board.apply_move(move, self.color)
			return 0, self.current_board"""
		possible_moves = self.current_board.get_valid_moves(self.color)
		for i in possible_moves:
			if i in CORNERS:
				self.current_board.apply_move(i, self.color)
				return 0, self.current_board
			elif self.current_board.count_stones()[2] == 3:
				move = self.size_move_calc(False, self.current_board.get_valid_moves(self.color))
				self.current_board.apply_move(move, self.color)
				return 0, self.current_board
			else:
				move = self.avoidSquare()
				self.current_board.apply_move(move, self.color)
				return 0, self.current_board


			##NEW NOTES
			#Avoid inside square and next to corners



		#possible_moves = self.current_board.get_valid_moves(self.color)
		#for i in possible_moves:
		#	print(i)
		#moves = random.sample(self.current_board.get_valid_moves(self.color), 1)
		#self.current_board.apply_move(moves[0], self.color)
		#return 0, self.current_board
