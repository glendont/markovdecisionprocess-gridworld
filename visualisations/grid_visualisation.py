from tkinter import *
from model.constants import *
import numpy as np

def grid_visualisation(np_array,grid,type):
    class Cell():
        FILLED_COLOR_BG = "green"
        EMPTY_COLOR_BG = "white"
        WALL_COLOR="#808080"
        FILLED_COLOR_BORDER = "black"
        EMPTY_COLOR_BORDER = "black"
        BROWN="orange"

        def __init__(self, master, x, y, size, text):
            """ Constructor of the object called by Cell(...) """
            self.master = master
            self.abs = x
            self.ord = y
            self.size = size
            self.fill = False
            self.text = text

        def draw(self):
            """ order to the cell to draw its representation on the canvas """
            if self.master != None:
                if (self.text=="W"):
                    fill=Cell.WALL_COLOR
                elif(self.text=="G"):
                    fill=Cell.FILLED_COLOR_BG
                elif(self.text=="B"):
                    fill=Cell.BROWN
                else:
                    fill = Cell.EMPTY_COLOR_BG

                outline = Cell.EMPTY_COLOR_BORDER

                xmin = self.abs * self.size
                xmax = xmin + self.size
                ymin = self.ord * self.size
                ymax = ymin + self.size

                self.master.create_rectangle(xmin, ymin, xmax, ymax, fill=fill, outline=outline)
                self.master.create_text((xmax - self.size / 2, ymax - self.size / 2), text=self.text)

    class CellGrid(Canvas):
        def __init__(self, master, grid, cell_size, *args, **kwargs):

            np_array=grid
            row_number = len(np_array)
            column_number = len(np_array[0])
            Canvas.__init__(self,
                            master,
                            width=cell_size * column_number,
                            height=cell_size * row_number,
                            *args,
                            **kwargs)

            self.cell_size = cell_size

            self.grid = []
            for row in range(row_number):
                line = []
                for column in range(column_number):
                    line.append(Cell(self,
                                     column,
                                     row,
                                     cell_size,
                                     np_array[row][column],
                                     )
                                )
                self.grid.append(line)
            self.draw()

        def draw(self):
            for row in self.grid:
                for cell in row:
                    cell.draw()
    app = Tk("Grid")
    if (type=="policy"):
        for key in np_array:
            if (np_array[key]=="U"):
                grid[key[0]][key[1]]="↑"
            elif (np_array[key]=="L"):
                grid[key[0]][key[1]]="←"
            elif (np_array[key]=="R"):
                grid[key[0]][key[1]]="→"
            elif (np_array[key]=="D"):
                grid[key[0]][key[1]]="↓"
            else:
                grid[key[0]][key[1]] = np_array[key]
    elif (type=="utilities"):
        for key in np_array:
            grid[key[0]][key[1]] = format(round(np_array[key],2))

    grid = CellGrid(app, grid, 150)
    grid.pack()
    app.mainloop()