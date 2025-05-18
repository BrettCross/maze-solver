from window import Window
from cell import Cell
from line import Line
from point import Point


def main():
    win = Window(800, 600)
    
    a = Cell(win)
    a.has_left_wall = False
    a.draw(50, 50, 100, 100)

    b = Cell(win)
    b.has_right_wall = False
    b.draw(125, 50, 175, 100)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(200, 50, 250, 100)

    d = Cell(win)
    d.has_top_wall = False
    d.draw(200, 125, 250, 175)
    
    a.draw_move(b)
    b.draw_move(c, undo=True)
    b.draw_move(d)
    win.wait_for_close()


if __name__ == "__main__":
    main()