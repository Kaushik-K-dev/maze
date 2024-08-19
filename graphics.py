from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze"
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__status = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__status = True
        while self.__status:
            self.redraw()
        print("window closed...")
    
    def close(self):
        self.__status = False

    def draw_line(self, line, fill_color='black'):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = Point(point1.x, point1.y)
        self.point2 = Point(point2.x, point2.y)
    
    def draw(self, canvas, fill_color='black'):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, win):
        self.left = True
        self.right = True
        self.top = True
        self.bottom = True
        self.__tlx = None
        self.__tly = None
        self.__brx = None
        self.__bry = None
        self.__win = win
        self.visited = False

    def draw(self, tlx, tly, brx, bry):
        self.__tlx = tlx
        self.__tly = tly
        self.__brx = brx
        self.__bry = bry
        self.__win.draw_line(Line(Point(self.__tlx, self.__tly), Point(self.__tlx, self.__bry)), 'black' if self.left else 'white')
        self.__win.draw_line(Line(Point(self.__brx, self.__tly), Point(self.__brx, self.__bry)), 'black' if self.right else 'white')
        self.__win.draw_line(Line(Point(self.__tlx, self.__tly), Point(self.__brx, self.__tly)), 'black' if self.top else 'white')
        self.__win.draw_line(Line(Point(self.__tlx, self.__bry), Point(self.__brx, self.__bry)), 'black' if self.bottom else 'white')

    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color = 'gray'
        else:
            fill_color = 'red'
        self.__win.draw_line(Line(Point((self.__tlx+self.__brx)/2,(self.__tly+self.__bry)/2), Point((to_cell.__tlx+to_cell.__brx)/2,(to_cell.__tly+to_cell.__bry)/2)), fill_color)