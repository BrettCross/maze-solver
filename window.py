from tkinter import Tk, BOTH, Canvas
from line import Line


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze Solver")

        self.canvas = Canvas(self.root, bg="white", width=self.width, height=self.height)
        self.canvas.pack()
        self.is_window_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.is_window_running = True
        while self.is_window_running:
            self.redraw()

    def close(self):
        self.is_window_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)