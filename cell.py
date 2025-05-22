from point import Point
from line import Line


class Cell:
    def __init__(self, win=None):
        self.__win = win
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
            return
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        left_line = Line(Point(x1, y1), Point(x1, y2))
        top_line = Line(Point(x1, y1), Point(x2, y1))
        right_line = Line(Point(x2, y1), Point(x2, y2))
        bottom_line = Line(Point(x1, y2), Point(x2, y2))

        if self.has_left_wall:
            self.__win.draw_line(left_line)
        else:
            self.__win.draw_line(left_line, "white")

        if self.has_top_wall:
            self.__win.draw_line(top_line)
        else:
            self.__win.draw_line(top_line, "white")

        if self.has_right_wall:
            self.__win.draw_line(right_line)
        else:
            self.__win.draw_line(right_line, "white")
        
        if self.has_bottom_wall:
            self.__win.draw_line(bottom_line)
        else:
            self.__win.draw_line(bottom_line, "white")

    def draw_move(self, to_cell, undo=False):
        fill = "red"
        if undo:
            fill= "gray"

        # from_cell [x=(x1+x2)/2, y=(y1+y2)/2] to_cell [x=(x1+x2)/2, y=(y1+y2)/2]
        x = (self._x1 + self._x2)/2
        y = (self._y1 + self._y2)/2
        point1 = Point(x, y)

        t_x = (to_cell._x1 + to_cell._x2)/2
        t_y = (to_cell._y1 + to_cell._y2)/2
        point2 = Point(t_x, t_y)

        line = Line(point1, point2)
        self.__win.draw_line(line, fill_color=fill)
