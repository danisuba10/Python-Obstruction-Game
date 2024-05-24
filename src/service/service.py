from src.repository import repo
from src.service.service_validations import ServiceValidation
from src.exceptions.exceptions import ServiceException, InvalidMove, GameOver


class Service:

    def __init__(self, size):
        self.size = size
        self.repo = repo.Repository(size)
        self.validations = ServiceValidation(self.repo, size)
        self.next_player = "player"
        self.winner = "-"

    def next(self):
        '''
        :return: returns next player
        '''
        return self.next_player

    def set_next(self, next):
        '''
        :param next: next player
        :return: sets next player
        '''
        self.next_player = next

    def move(self, x:int, y:int, symbol:chr):
        '''
        :param x: row of dest
        :param y: column of dest
        :param symbol: symbol of player
        :return: performs player move, raises exception otherwise
        '''
        try:
            self.validations.valid_move(x, y)
            self.repo.move(x, y, symbol)
        except InvalidMove:
            raise

    def gameover_check(self):
        '''
        :return: checks if game is over, if it is, raises exception
        '''
        empty_cells = self.repo.empty_count()
        if empty_cells == 0:
            if self.next_player == "computer":
                self.winner = "player"
            elif self.next_player == "player":
                self.winner = "computer"
            raise GameOver

