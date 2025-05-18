from point import Point
from line import Line


class Cell:
    def __init__(self, win):
        self._win = win
        self._x1 = -1
        self._x2 = -1
        self._y1 = -1
        self._y2 = -1
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            point1 = Point(x1, y1)
            point2 = Point(x1, y2)
            line = Line(point1, point2)
            self._win.draw_line(line)
        if self.has_top_wall:
            point1 = Point(x1, y1)
            point2 = Point(x2, y1)
            line = Line(point1, point2)
            self._win.draw_line(line)
        if self.has_right_wall:
            point1 = Point(x2, y1)
            point2 = Point(x2, y2)
            line = Line(point1, point2)
            self._win.draw_line(line)
        if self.has_bottom_wall:
            point1 = Point(x1, y2)
            point2 = Point(x2, y2)
            line = Line(point1, point2)
            self._win.draw_line(line)