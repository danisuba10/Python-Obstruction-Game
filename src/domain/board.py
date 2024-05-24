import texttable

class Board:

    def __init__(self, size:int):
        self.empty_cellcount = size * size
        self.size = size
        self.__board = []
        self.__initialise_board()

    def __initialise_board(self):
        '''
        :return: initialises bboard based on size, fills headers on first row and first column
        '''
        header = [" "]
        for i in range(1, self.size + 1, 1):
            header.append(str(i))

        self.__board.append(header)

        for row in range(1, self.size + 1, 1):
            temp_row = [str(row)]
            for column in range(1, self.size + 1, 1):
                temp_row.append(" ")
            self.__board.append(temp_row)

    def __str__(self):
        '''
        :return: transforms to texttable
        '''
        table = texttable.Texttable()
        for row in range(0, self.size + 1, 1):
            temp_row = []
            for column in range(0, self.size + 1, 1):
                cell = self.__board[row][column]
                if "[" in cell and "]" in cell:
                    temp_row.append("[]")
                else:
                    temp_row.append(cell)
            table.add_row(temp_row)
        return table.draw()

    def __getitem__(self, item):
        return self.__board[item]

    def __setitem__(self, key, value):
        self.__board[key[0]][key[1]] = value
