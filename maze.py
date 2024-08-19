from graphics import Cell
import random
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__rows = num_rows
        self.__cols = num_cols
        self.__cell_sizex = cell_size_x
        self.__cell_sizey = cell_size_y
        self.__win = win
        self.__create_cells()
        self.__break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()

    def __create_cells(self):
        self._cells = [[Cell(self.__win) for i in range(self.__rows)] for i in range(self.__cols)]
        for i in range(self.__cols):
            for j in range(self.__rows):
                self.draw_cell(i,j)

    def draw_cell(self, i, j):
        if self.__win is None:
            return
        self._cells[i][j].draw(self.__x1+(i*self.__cell_sizex), self.__y1+(j*self.__cell_sizey), self.__x1+((i+1)*self.__cell_sizex), self.__y1+((j+1)*self.__cell_sizey))
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.1)

    def __break_entrance_and_exit(self):
        self._cells[0][0].top = False
        self._cells[self.__cols-1][self.__rows-1].bottom = False
        self.draw_cell(0,0)
        self.draw_cell(self.__cols-1, self.__rows-1)

    def __break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_visit_list = []
            if i-1>=0 and self._cells[i-1][j].visited != True:
                direction = 'left'
                next_visit_list.append((i-1,j, direction))
            if i+1<=self.__cols-1 and self._cells[i+1][j].visited != True:
                direction = 'right'
                next_visit_list.append((i+1,j, direction))
            if j-1>=0 and self._cells[i][j-1].visited != True:
                direction = 'top'
                next_visit_list.append((i,j-1, direction))
            if j+1<=self.__rows-1 and self._cells[i][j+1].visited != True:
                direction = 'bottom'
                next_visit_list.append((i,j+1, direction))
            if next_visit_list == []:
                self.draw_cell(i,j)
                return
            next = random.randrange(0, len(next_visit_list))
            if next_visit_list[next][2] == 'left':
                self._cells[i][j].left = False
                self._cells[i-1][j].right = False
            if next_visit_list[next][2] == 'right':
                self._cells[i][j].right = False
                self._cells[i+1][j].left = False
            if next_visit_list[next][2] == 'top':
                self._cells[i][j].top = False
                self._cells[i][j-1].bottom = False
            if next_visit_list[next][2] == 'bottom':
                self._cells[i][j].bottom = False
                self._cells[i][j+1].top = False
            self.__break_walls_r(next_visit_list[next][0],next_visit_list[next][1])
        
    def __reset_cells_visited(self):
        for i in range(self.__cols):
            for j in range(self.__rows):
                self._cells[i][j].visited = False
    
    def solve(self):
        return self.__solve_r(0,0)
            
    def __solve_r(self, i, j):
        self.__animate()
        self._cells[i][j].visited = True
        if i == self.__cols-1 and j == self.__rows-1:
            return True
        if i-1>=0 and self._cells[i][j].left == False and self._cells[i-1][j].visited == False:
            self._cells[i][j].draw_move(self._cells[i-1][j], undo=False)
            if self.__solve_r(i-1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
        if i+1<=self.__cols-1 and self._cells[i][j].right == False and self._cells[i+1][j].visited == False:
            self._cells[i][j].draw_move(self._cells[i+1][j], undo=False)
            if self.__solve_r(i+1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
        if j-1>=0 and self._cells[i][j].top == False and self._cells[i][j-1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j-1], undo=False)
            if self.__solve_r(i, j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)
        if j+1<=self.__rows-1 and self._cells[i][j].bottom == False and self._cells[i][j+1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j+1], undo=False)
            if self.__solve_r(i, j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
        return False