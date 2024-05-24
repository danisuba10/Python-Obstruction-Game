from src.domain.board import Board
from src.repository.repo import Repository
from src.exceptions.exceptions import ServiceException, InvalidMove

class ServiceValidation:

    def __init__(self, repo:Repository, size):
        self.__size = size
        self.__repo = repo
        pass

    def valid_move(self, x:int, y:int):
        '''
        :param x: row dest
        :param y: column dest
        :return: raises InvalidMove exception if move is not correct
        (out of bounds, not empty)
        '''

        if not(1 <= x <= self.__size) or not(1 <= y <= self.__size):
            raise InvalidMove

        if not(self.__repo.get_value(x, y) == " "):
            raise InvalidMove()