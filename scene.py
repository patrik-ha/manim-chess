from manim import *
from chess import get_board

class Chess(Scene):
    def construct(self):
        board = get_board((5, 4), "rqkr/pppp/4/PPPP/RQKR w - - 0 1")
        self.add(board)

