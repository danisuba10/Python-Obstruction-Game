import copy
import random
from src.service.service import Service, InvalidMove

class ComputerStupid:

    def __init__(self, service):
        self.service = service

    def move(self):
        '''
        :return: performs a random computer move, if move is not correct, it generates a new
        destination pair
        '''
        ExceptionThrown = True
        while ExceptionThrown:
            row = random.randint(1, self.service.size)
            column = random.randint(1, self.service.size)
            try:
                self.service.move(row, column, "O")
                ExceptionThrown = False
                print(f"Computer moved to {row} {column}")
            except InvalidMove:
                ExceptionThrown = True

class ComputerMiniMax:

    def __init__(self, service):
        self.service = service
        self.size = self.service.size
        self.board = copy.deepcopy(self.service.repo.get_board())
        self.winner = "-"
        a = 1

    def __get_empty_cells(self):
        '''
        :return: return empty cells of board
        '''
        empty_cells = []

        for row in range(1, self.size + 1, 1):
            for column in range(1, self.size + 1, 1):
                if self.board[row][column] == " ":
                    empty_cells.append([row, column])

        return empty_cells

    def __is_valid_move(self, row, col):
        '''
        :param row: row dest
        :param col: col dest
        :return: checks if move is valid
        '''
        return 1 <= row <= self.size and 1 <= col <= self.size and self.board[row][col] == ' '

    def __make_move(self, row, col, player):
        '''
        :param row: row dest of move
        :param col: column dest of move
        :param player: player making the move
        :return: performs move
        '''
        if self.__is_valid_move(row, col):
            self.board[row][col] = player
            self.__block_adjacent(row, col, player)

    def __block_adjacent(self, x:int, y:int, symbol:chr):
        '''
        :param x: row dest of move
        :param y: column dest of move
        :param symbol symbol of moving player
        :return: blocks neighbouring empty celss
        '''
        size = self.board.size
        for change_row in (-1, 0, 1):
            for change_column in (-1, 0, 1):
                row = x + change_row
                column = y + change_column
                if 1 <= row <= size and 1 <= column <= size and self.board[row][column] == " ":
                    self.board[row][column] = f"[{symbol}]"

    def __unblock_adjacent(self, x, y):
        '''
        :param x: row dest of move
        :param y: column dest of move
        :return: blocks neighbouring empty celss
        '''
        size = self.board.size
        for change_row in (-1, 0, 1):
            for change_column in (-1, 0, 1):
                row = x + change_row
                column = y + change_column
                if 1 <= row <= size and 1 <= column <= size and "[" in self.board[row][column] and "]" in self.board[row][column]:
                    self.board[row][column] = " "

    def __undo_move(self, row, col):
        '''
        :param row: row of move
        :param col: column of move
        :return: undos move
        '''
        self.board[row][col] = ' '
        self.__unblock_adjacent(row, col)

    def __is_game_over(self):
        '''
        :return: checks if game is over
        '''
        return not self.__get_empty_cells()

    def __get_blocked_moves(self):
        '''
        :return: counts how many cells were blocked by x and o and then return the counts
        '''
        x_blocked_moves = 0
        o_blocked_moves = 0

        for row in range(1, self.size + 1, 1):
            for column in range(1, self.size + 1, 1):
                if self.board[row][column] == "[O]":
                    o_blocked_moves += 1
                elif self.board[row][column] == "[X]":
                    x_blocked_moves += 1

        return x_blocked_moves, o_blocked_moves


    def __evaluate(self, winner):
        '''
        :param winner: winner player if game is over
        :return: returns an evaluated number for game
        '''
        if winner == "maxi":
            return 999999
        elif winner == "mini":
            return -999999

        center_value = 1.339674

        x_moves = len([(i, j) for i in range(self.size) for j in range(self.size) if self.board[i][j] == 'X'])
        o_moves = len([(i, j) for i in range(self.size) for j in range(self.size) if self.board[i][j] == 'O'])

        center_moves = [(2,2), (2,3), (2,4), (3,2), (3,3), (3,4), (4,2), (4,3), (4,4)]

        center_x_moves = len([(i, j) for i in range(self.size) for j in range(self.size) if self.board[i][j] == 'X'
                              and (i, j) in center_moves])
        center_o_moves = len([(i, j) for i in range(self.size) for j in range(self.size) if self.board[i][j] == 'O'
                              and (i, j) in center_moves])

        blocked_value = 3.323123

        x_blocked_moves, o_blocked_moves = self.__get_blocked_moves()

        return ((o_moves - x_moves) + center_value * (center_o_moves - center_x_moves) + blocked_value *
                (o_blocked_moves - x_blocked_moves))

    def __minimax(self, depth, alpha, beta, maximizing_player):
        '''
        :param depth: depth for minimax
        :param alpha: alpha for alpha beta opt
        :param beta: beta for alpha beta opt
        :param maximizing_player: symbol of maximising player
        :return:
        '''
        if depth == 0 or self.__is_game_over():
            winner = "-"
            if depth != 0 and maximizing_player:
                winner = "mini"
            elif depth != 0 and not maximizing_player:
                winner = "maxi"
            return self.__evaluate(winner)

        if maximizing_player:
            max_eval = float('-inf')
            for move in self.__get_empty_cells():
                self.__make_move(move[0], move[1], 'O')
                eval = self.__minimax(depth - 1, alpha, beta, False)
                self.__undo_move(move[0], move[1])
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.__get_empty_cells():
                self.__make_move(move[0], move[1], 'X')
                eval = self.__minimax(depth - 1, alpha, beta, True)
                self.__undo_move(move[0], move[1])
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def calculate_depth(self):
        '''
        :return: calculates different depth for minimax based on no. of empty cells leftf
        '''
        num_empty_cells = len(self.__get_empty_cells())
        if num_empty_cells > 20:
            return 3
        elif num_empty_cells > 15:
            return 3
        elif num_empty_cells > 10:
            return 4
        else:
            return 5

    def find_best_move(self):
        '''
        :return: finds the best move for the maximising player using minimax algorithm
        '''
        best_val = float('-inf')
        best_move = None
        alpha = float('-inf')
        beta = float('inf')
        depth = self.calculate_depth()
        empty_cells = self.__get_empty_cells()
        random.shuffle(empty_cells)
        for move in empty_cells:
            self.__make_move(move[0], move[1], 'O')
            move_val = self.__minimax(depth , alpha, beta, False)  # Adjust depth as needed
            self.__undo_move(move[0], move[1])
            if move_val > best_val:
                best_move = move
                best_val = move_val
            elif move_val < best_val:
                pass
        return best_move

    def move(self):
        '''
        :return: performs move based on best move
        '''
        self.board = copy.deepcopy(self.service.repo.get_board())

        best_move = self.find_best_move()
        row = int(best_move[0])
        column = int(best_move[1])
        try:
            self.service.move(row, column, "O")
        except InvalidMove:
            #TEMPORARY CODE
            print("INVALID COMPUTER MOVE")

