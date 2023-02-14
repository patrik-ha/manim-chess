from manim import *

def piece_to_icon(c, fill=True):
    prefix = "w" if c.isupper() else "b"
    prefix = prefix if not c.isspace() else ""
    icon = SVGMobject("pieces/{}.svg".format(prefix + c.upper()), should_center=False)
    scalings = {
        'p': 0.35,
        'r': 0.35,
        'k': 0.40,
        'n': 0.38,
        'b': 0.38,
        'q': 0.38
    }
    icon.set_x(0)
    icon.set_y(0)
    icon.scale(scalings[c.lower()])
    if c.lower() == "k":
        icon.shift(UP * 0.035)
    return icon

def read_fen(fen):
    if " " in fen:
        fen = fen.split(" ")[0]
    
    rows = fen.split("/")


    for i, row in enumerate(rows):
        new_row = ""
        for c in row:
            if c in "123456789":
                new_row += " " * int(c)
            else:
                new_row += c
        rows[i] = new_row
    dims = (len(rows), max([len(row) for row in rows]))
    return rows, dims


def get_board(fen):
    fen, dims = read_fen(fen)
    template = TexTemplate()
    template.add_to_preamble(r"\usepackage{skak}")
    board = []
    for i in range(dims[0]):
        for j in range(dims[1]):
            color = "#B58863" if ((i + j + 1) % 2) == 0 else "#F0D9B5"
            square = Square(0.999, stroke_color=BLACK, stroke_width=0)
            square.set_fill(color, 1)
            if not fen[i][j].isspace():
                icon = piece_to_icon(fen[i][j])
                square = Group(square, icon)
            square.shift(i * DOWN + j * RIGHT)
            board.append(square)
    board = Group(*board)
    board.set_x(0)
    board.set_y(0)
    return board