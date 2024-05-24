from src.exceptions.exceptions import UIException


class Validations():
    def __init__(self):
        pass

    def valid_player_input(self, inp:str):
        '''
        :param inp: input string
        :return: checks if input string is correct, if not, raises exception
        '''
        inp = inp.strip()
        inp = inp.split(" ")
        if len(inp) != 2:
            raise UIException("Incorrect input length!")
        try:
            row = int(inp[0])
            column = int(inp[1])
        except:
            raise UIException("One of the coordinates is not an integer!")