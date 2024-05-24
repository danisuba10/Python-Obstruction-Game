
class UIException(Exception):
    '''
    ServiceException class for exceptions related to the service
    '''

    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return "UI Exception: " + self.__msg


class ServiceException(Exception):
    '''
    ServiceException class for exceptions related to the service
    '''

    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return "Service exception: " + self.__msg

class PlayerException(Exception):
    '''
    PlayerException class for exceptions related to the player
    '''

    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return "Player exception: " + self.__msg

class InvalidMove(PlayerException):
    '''
    InvalidMove class for exceptions related to invalid move, inheriths PlayerException
    '''

    def __init__(self):
        super().__init__("Invalid move!")


class GameOver(Exception):
    '''
    PlayerException class for exceptions related to the player
    '''

    def __init__(self):
        pass

    def __str__(self):
        return "Game over! "