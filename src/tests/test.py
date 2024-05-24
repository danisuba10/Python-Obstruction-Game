import unittest
import texttable
from src.domain.board import Board
from src.repository.repo import Repository
from src.service.service import Service, ServiceValidation, InvalidMove, GameOver
from src.service.Player import Player
from src.service.ComputerPlayer import ComputerStupid, ComputerMiniMax

class BoardTest(unittest.TestCase):

    def test_str(self):
        board = Board(6)
        self.assertEquals(board[0][3], "3")
        board[3][3] = "O"
        self.assertEquals(board[3][3], "O")

class RepositoryTest(unittest.TestCase):

    def test_repo(self):
        repo = Repository(3)
        repo.move(1, 1, "O")
        table = texttable.Texttable()
        row1 = [" ", "1", "2", "3"]
        row2 = ["1", "O", "[]", " "]
        row3 = ["2", "[]", "[]", " "]
        row4 = ["3", " ", " ", " "]
        table.add_row(row1)
        table.add_row(row2)
        table.add_row(row3)
        table.add_row(row4)
        st = table.draw()
        self.assertEquals(st, repo.get_board().__str__())

class ServiceTest(unittest.TestCase):

    def testservice(self):
        service = Service(3)
        invalidmove = False
        try:
            service.move(13, 13, "O")
        except InvalidMove:
            invalidmove = True
        self.assertEquals(invalidmove, True)
        gameover = False
        try:
            service.gameover_check()
        except GameOver:
            gameover = True
        self.assertEquals(gameover, False)
        service.move(1, 1, "X")
        service.set_next("computer")
        service.move(3, 1, "O")
        service.set_next("player")
        service.move(2, 3, "X")
        service.set_next("computer")
        gameover = False
        try:
            service.gameover_check()
        except GameOver:
            gameover = True
        self.assertEquals(gameover, True)
        self.assertEquals(service.winner, "player")

        service = Service(3)

        service.move(1, 1, "X")
        service.set_next("computer")
        service.move(3, 1, "O")
        service.set_next("player")
        service.move(3, 3, "X")
        service.set_next("computer")
        service.move(1, 3, "O")
        service.set_next("player")
        next = service.next()
        self.assertEquals(next, "player")
        gameover = False
        try:
            service.gameover_check()
        except GameOver:
            gameover = True
        self.assertEquals(gameover, True)
        self.assertEquals(service.winner, "computer")

    def test_players(self):
        service = Service(3)
        player = Player(service)
        stupid = ComputerStupid(service)
        minimax = ComputerMiniMax(service)

        invalid = False
        try:
            player.move(1, 21)
        except InvalidMove:
            invalid = True

        self.assertEquals(invalid, True)

        player.move(1, 1)

        compare_service = Service(3)
        compare_service.move(1, 1, "X")

        self.assertEquals(service.repo.get_board().__str__(), compare_service.repo.get_board().__str__())

        stupid.move()

        o_count = 0

        for row in range(1, service.size + 1, 1):
            for column in range(1, service.size + 1, 1):
                if service.repo.get_board()[row][column] == "O":
                    o_count += 1

        self.assertEqual(o_count, 1)

        service = Service(3)
        player = Player(service)
        stupid = ComputerStupid(service)
        minimax = ComputerMiniMax(service)
        player.move(1, 1)
        best_move = minimax.find_best_move()
        self.assertNotEqual(best_move, (None, None))