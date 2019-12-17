from random import randrange as rnd, choice
import tkinter as tk
import math
import time


global root,canv,lifeScale,lifeSpeed,ifTime,generationCounter
root = tk.Tk()
#fr = tk.Frame(root)
lifeScale = 100
s = str(lifeScale * 10) + "x" + str(lifeScale * 10)
root.geometry(s)
canv = tk.Canvas(root, bg='pink')
canv.pack(fill=tk.BOTH, expand=1)
#масштаб
lifeSpeed = 1 #скорость

ifTime = 0 #остановка времени 0-если время стоит
generationCounter = 0

canv.create_rectangle(0, 0, 100, 100,fill='Black', outline='Pink')
canv.create_rectangle(100, 0, 200, 100,fill='Black', outline='Pink')

def filling():

    for j in range (0, lifeScale)
        for i in range(0, lifeScale):
        if mass2[i][j]== 0:
            canv.create_rectangle (i*10, j*10, (i+1)*10, (j+1)*10, fill='Black', outline='Pink')
        else:
            canv.create_rectangle(i * 10, j * 10, (i + 1) * 10, (j + 1) * 10, fill='Black', outline='Pink')

root.mainloop()
