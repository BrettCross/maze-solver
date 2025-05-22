from cell import Cell
import time
import random


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []

        if seed is not None:
            random.seed(seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()

    def __create_cells(self):
        # populate cells
        for i in range(self.__num_cols):
            col_cells = []
            for j in range(self.__num_rows):
                cell = Cell(self.__win)
                col_cells.append(cell)
            self.__cells.append(col_cells)

        for i in range(self.__num_cols):
                for j in range(self.__num_rows):
                    self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        # calculate x/y pos base on i/j pos and cell size
        if self.__win is None:
            return 
        
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0,0)
        self.__cells[self.__num_cols-1][self.__num_rows-1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols-1, self.__num_rows-1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            to_visit = []
            # up j-1, right i+1, down j+1 or left i-1? 
            # left
            if i > 0 and not self.__cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            # right
            if i < self.__num_cols -1 and not self.__cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            # up
            if j > 0 and not self.__cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            # down
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            if len(to_visit) == 0:
                self.__draw_cell(i, j)
                return
            
            # choose random direction
            direction = random.randrange(len(to_visit))
            next_index = to_visit[direction]

            # right
            if next_index[0] == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i - 1][j].has_right_wall = False
            # up
            if next_index[1] == j - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j - 1].has_bottom_wall = False
            # down
            if next_index[1] == j + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j + 1].has_top_wall = False

            self.__break_walls_r(next_index[0], next_index[1])

    def __reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                if self.__cells[i][j].visited:
                    self.__cells[i][j].visited = False

    def solve(self):
        return self.__solve_r(0, 0)
    
    # depth-first solution
    def __solve_r(self, i, j):
        self.__animate()

        self.__cells[i][j].visited = True

        # if end cell, we are done!
        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True

        
        # left
        if (
            i > 0 
            and not self.__cells[i - 1][j].visited 
            and not self.__cells[i][j].has_left_wall
            ):
            self.__cells[i][j].draw_move(self.__cells[i - 1][j])
            if self.__solve_r(i - 1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i - 1][j], True)

        # right
        if (
            i < self.__num_cols - 1 
            and not self.__cells[i + 1][j].visited 
            and not self.__cells[i][j].has_right_wall
            ):
            self.__cells[i][j].draw_move(self.__cells[i + 1][j])
            if self.__solve_r(i + 1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i + 1][j], True)

        # up
        if (
            j > 0 
            and not self.__cells[i][j - 1].visited 
            and not self.__cells[i][j].has_top_wall
            ):
            self.__cells[i][j].draw_move(self.__cells[i][j - 1])
            if self.__solve_r(i, j - 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j - 1], True)

        # down
        if (
            j < self.__num_rows - 1 
            and not self.__cells[i][j + 1].visited 
            and not self.__cells[i][j].has_bottom_wall
            ):
            self.__cells[i][j].draw_move(self.__cells[i][j + 1])
            if self.__solve_r(i, j + 1):
                return True
            else: 
                self.__cells[i][j].draw_move(self.__cells[i][j + 1], True)
        
        return False