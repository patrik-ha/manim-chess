from manim import *

def piece_to_icon(c, fill=True):
    color = RED if c.isupper() else BLACK
    prefix = r"\Black" if c.isupper() else r"\Black"
    prefix = prefix if not c.isspace() else ""
    lookup = {
        'k': "King",
        'q': "Queen",
        'r': "Rook",
        'b': "Bishop",
        'n': "Knight",
        'p': "Pawn",
        ' ': ""
    }

    suffix = "OnWhite" if c.isupper() else "OnWhite"
    suffix = suffix if not c.isspace() else ""

    template = TexTemplate()
    template.add_to_preamble(r"\usepackage{skak}")
    tex = Tex(
        prefix + lookup[c.lower()] + suffix,
        tex_template=template,
        color=color,
    )

    tex.set_fill(color)
    tex.scale(1)
    return tex

def clean_fen(fen):
    # Only care about the position
    # Also assume that the fen is valid or whatever
    if " " in fen:
        fen = fen.split(" ")[0]
    
    rows = fen.split("/")

    for i, row in enumerate(rows):
        new_row = ""
        for c in row:
            if c in "12345678":
                new_row += " " * int(c)
            else:
                new_row += c
        rows[i] = new_row
    print(rows)
    return rows


def get_board(dims, fen):
    fen = clean_fen(fen)
    template = TexTemplate()
    template.add_to_preamble(r"\usepackage{skak}")
    board = []
    for i in range(dims[0]):
        for j in range(dims[1]):
            color = WHITE if ((i + j) % 2) == 0 else BLUE
            square = Square(1, stroke_color=BLACK, stroke_width=DEFAULT_STROKE_WIDTH * 0.3)
            square.set_fill(color, 1)
            icon = piece_to_icon(fen[i][j])
            full_square = Group(square, icon)
            full_square.shift(i * DOWN + j * RIGHT)
            board.append(full_square)
    board = Group(*board)
    board.set_x(0)
    board.set_y(0)
    return board