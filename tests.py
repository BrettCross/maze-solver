import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_wide(self):
        num_cols = 30
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows
        )

    def test_maze_break_entrance_and_exit(self):
        maze = Maze(0, 0, 10, 10, 20, 20)
        maze._Maze__break_entrance_and_exit()
        self.assertEqual(
            maze._Maze__cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            maze._Maze__cells[9][9].has_bottom_wall,
            False
        )


if __name__ == "__main__":
    unittest.main()