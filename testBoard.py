import unittest
from tictactoe import Board

class TestBoardMarkBoard(unittest.TestCase):
    def test_markBoardLocationCheck(self):
        b = Board()
        b.mark_square(2, 1, "X")
        self.assertEqual(b.tictactoeBoard, ["-", "-", "-", "-", "-", "X", "-", "-", "-"])

    def test_markBoardOutOfBounds(self):
        b = Board()
        self.assertFalse(b.mark_square(3, 3, "X"))

    def test_markBoardBadInput(self):
        b = Board()
        self.assertFalse(b.mark_square(2, 2, 2))

    def test_markBoardSuccess(self):
        b = Board()
        self.assertTrue(b.mark_square(1, 1, "X"))

    def test_markBoardWrongCase(self):
        b = Board()
        self.assertTrue(b.mark_square(1, 1, "x"))


class TestBoardHasWinner(unittest.TestCase):
    def test_hasWinner(self):
        b = Board()
        b.mark_square(0,0,1)
        b.mark_square(1,0,1)
        b.mark_square(2,0,1)
        self.assertTrue(b.has_winner())

    def test_noWinner(self):
        b = Board()
        self.assertFalse(b.has_winner())


class TestBoardValidInput(unittest.TestCase):
    def test_invalidInput(self):
        b = Board()
        self.assertFalse(b.valid_input(3, 3))

    def test_validInput(self):
        b = Board()
        self.assertTrue(b.valid_input(1, 1))

if __name__ == '__main__':
    unittest.main()