from window import Window
from line import Line
from point import Point


def main():
    win = Window(800, 600)
    pt_1 = Point(100, 100)
    pt_2 = Point(100, 250)
    pt_3 = Point(400, 500)
    pt_4 = Point(150, 400)
    win.draw_line(Line(pt_1, pt_2), "blue")
    win.draw_line(Line(pt_3, pt_2), "red")
    win.draw_line(Line(pt_1, pt_4), "green")
    win.draw_line(Line(pt_4, pt_3), "purple")
    win.wait_for_close()


if __name__ == "__main__":
    main()