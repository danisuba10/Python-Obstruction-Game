from src.service.service import Service, InvalidMove

class Player:

    def __init__(self, service:Service):
        self.service = service

    def move(self, row:int, column:int):
        '''
        :param row: row dest
        :param column: column dest
        :return: moves to cell if correct, raises exception otherwise
        '''
        try:
            self.service.move(row, column, "X")
        except InvalidMove:
            raise