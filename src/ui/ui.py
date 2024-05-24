from src.service.service import Service
from src.service.ComputerPlayer import ComputerStupid, ComputerMiniMax
from src.service.Player import Player
from src.ui.ui_validations import Validations
from src.exceptions.exceptions import UIException, InvalidMove, GameOver

class UI:

    def __init__(self, size, computer_player):
        self.service = Service(size)
        self.validation = Validations()
        self.player = Player(self.service)
        self.computer = computer_player(self.service)

    def get_input(self):
        ExceptionThrown = True
        while ExceptionThrown:
            inp = input("Select cell to move! Syntax: <row, column>\n>>>")
            try:
                self.validation.valid_player_input(inp)
                inp = inp.strip()
                inp = inp.split(" ")
                row = int(inp[0])
                column = int(inp[1])
                return row, column
            except UIException as uiex:
                print(uiex)

    def menu(self):

        GameIsOver = False
        while not GameIsOver:
            print(self.service.repo.get_board())

            next_player_to_move = self.service.next()
            if next_player_to_move == "player":
                ExceptionThrown = True
                while ExceptionThrown:
                    row, column = self.get_input()
                    try:
                        self.player.move(row, column)
                        ExceptionThrown = False
                    except InvalidMove as imov:
                        print(imov)
                self.service.set_next("computer")
            elif next_player_to_move == "computer":
                self.computer.move()
                self.service.set_next("player")

            try:
                self.service.gameover_check()
            except GameOver as gover:
                print(self.service.repo.get_board())
                print(gover)
                print(f"Winner is {self.service.winner.upper()}!!")
                GameIsOver = True