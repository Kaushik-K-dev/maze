from graphics import Window, Point, Line, Cell
from maze import Maze

def main():
    # line = Line(Point(200, 100), Point(600,500))
    # win.draw_line(line)
    # cell1 = Cell(win)
    # cell1.right = False
    # cell1.draw(100,100,200,200)
    # cell2= Cell(win)
    # cell2.left = False
    # cell2.draw(200,100,300,200)
    # cell1.draw_move(cell2, False)

    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()