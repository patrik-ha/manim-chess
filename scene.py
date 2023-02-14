from manim import *
from chess import get_board

class Chess(Scene):
    def construct(self):
        board = get_board((5, 4), "")
        self.add(board)

