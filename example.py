from manim import *
from chess import get_board

class Chess(Scene):
    def construct(self):
        board = get_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        small_board = get_board("rqkr/pppp/4/PPPP/RQKR w - - 0 1").next_to(board, RIGHT)
        self.add(Group(board, small_board).center())


