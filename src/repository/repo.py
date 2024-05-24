from src.domain.board import Board


class Repository:

    def __init__(self, size: int):
        self.__board = Board(size)

    def get_board(self):
        return self.__board

    def get_value(self, x:int, y:int):
        return self.__board[x][y]

    def empty_count(self):
        '''
        :return: return no. of empty cells
        '''
        return self.__board.empty_cellcount

    def __block_adjacent(self, x:int, y:int, symbol:chr):
        '''
        :param x: row dest of move
        :param y: column dest of move
        :return: blocks neighbouring empty celss
        '''
        size = self.__board.size
        for change_row in (-1, 0, 1):
            for change_column in (-1, 0, 1):
                row = x + change_row
                column = y + change_column
                if 1 <= row <= size and 1 <= column <= size and self.__board[row][column] == " ":
                    self.__board[row][column] = f"[{symbol}]"
                    self.__board.empty_cellcount -= 1
        a = 1

    def move(self, x:int, y:int, symbol:chr):
        '''
        :param x: row of dest
        :param y: column of dest
        :param symbol: symbol of player
        :return: performs player move, blocks adjacent cells
        '''
        self.__board[x][y] = symbol
        self.__board.empty_cellcount -= 1
        self.__block_adjacent(x, y, symbol)
