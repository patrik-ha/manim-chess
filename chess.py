from manim import *

def piece_to_icon(c):
    color = RED if c.isupper() else BLACK
    lookup = {
        'k': r"\symking",
        'q': r"\symqueen",
        'r': r"\symrook",
        'b': r"\symbishop",
        'n': r"\symknight",
        'p': r"\sympawn",
    }
    template = TexTemplate()
    template.add_to_preamble(r"\usepackage{skak}")
    tex = Tex(
        lookup[c.lower()],
        tex_template=template,
        color=color
    )
    tex.scale(1.9)
    return tex

def get_board(dims, fen):
    template = TexTemplate()
    template.add_to_preamble(r"\usepackage{skak}")

    board = []
    for i in range(dims[0]):
        for j in range(dims[1]):
            color = WHITE if ((i + j) % 2) == 0 else BLUE
            square = Square(1, stroke_color=BLACK, stroke_width=DEFAULT_STROKE_WIDTH * 0.3)
            square.set_fill(color, 1)
            icon = piece_to_icon("Q")
            full_square = Group(square, icon)
            full_square.shift(i * DOWN + j * RIGHT)
            board.append(full_square)
    board = Group(*board)
    board.set_x(0)
    board.set_y(0)
    return board