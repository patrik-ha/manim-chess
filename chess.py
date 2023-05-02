from manim import *
import os

def piece_to_icon(c, fill=True):
    prefix = "w" if c.isupper() else "b"
    prefix = prefix if not c.isspace() else ""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    piece_path = os.path.join(dir_path, "pieces/{}.svg".format(prefix + c.upper()))
    icon = SVGMobject(piece_path, should_center=False)
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


def get_board(fen, arrows=None, piece_opacities=None, highlights=None):
    if arrows is None:
        arrows = []
    if highlights is None:
        highlights = []
    fen, dims = read_fen(fen)
    if piece_opacities is None:
        piece_opacities = np.ones(dims, dtype=np.float32)
    board = []
    for i in range(dims[0]):
        for j in range(dims[1]):
            color = "#B58863" if ((i + j + 1) % 2) == 0 else "#F0D9B5"
            square = Square(0.999, stroke_color=BLACK, stroke_width=0)
            square.set_fill(color, 1)
            if not fen[i][j].isspace():
                icon = piece_to_icon(fen[i][j])
                icon.fade((1 - piece_opacities[i, j])).set_z_index(square.get_z() + 1)
                square = Group(square, icon)
            square.shift(i * DOWN + j * RIGHT)
            board.append(square)
    highlights_to_add = []
    for (i, j, color) in highlights:
        highlight = Square(0.999, stroke_width=0, fill_color=color, fill_opacity=0.7).shift(i * DOWN + j * RIGHT)
        highlights_to_add.append(highlight.set_z_index(icon.get_z() + 0.5))  
    
    arrows_to_add = []
    for arrow in arrows:
        i, j, dx, dy = arrow
        graphical_arrow = Arrow((DOWN * i + RIGHT * j), (DOWN * (i + dx) + RIGHT * (j + dy)), color=BLUE, stroke_width=25, max_stroke_width_to_length_ratio=10, max_tip_length_to_length_ratio=0.5)
        circle = Circle(0.45, stroke_width=DEFAULT_STROKE_WIDTH*2).shift((DOWN * (i + dx) + RIGHT * (j + dy)))
        group = Group(circle, graphical_arrow)
        arrows_to_add.append(group)
        
    
    board = Group(*board, *arrows_to_add, *highlights_to_add)
    board.set_x(0)
    board.set_y(0)
    return board