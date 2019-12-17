#coding: utf-8
import math
import tkinter as tk
import time


#menu

from tkinter import *
rootMenu = Tk()
#commands нужно добавить другие
lifeScale = 50
lifeSpeed = 200
cellSize = 20
preset ="empty"

def cellSize10():
    global cellSize
    cellSize = 10

def cellSize15():
    global cellSize
    cellSize = 15

def cellSize20():
    global cellSize
    cellSize = 20


def Scale200():
    global lifeScale
    lifeScale = 200

def Scale100():
    global lifeScale
    lifeScale = 100

def Scale50():
    global lifeScale
    lifeScale = 50

def Speed1():
    global lifeSpeed
    lifeSpeed = 20

def Speed2():
    global lifeSpeed
    lifeSpeed = 100

def Speed3():
    global lifeSpeed
    lifeSpeed = 200

def Glider():
    global preset
    preset = "glider"

def Clock():
    global preset
    preset = "clock"
def Vline():
    global  preset
    preset = "vline"
def Hline():
    global preset
    preset = "hline"
def Universe():
    global preset
    preset ="universe"
n = 0
m = 0
mass1 = [[0 for j in range(m)] for i in range(n)]
mass2 = [[0 for j in range(m)] for i in range(n)]


def CellUpdate():
    global n,m,generationCounter,mass1,mass2
    for i in range(n):
        for j in range(m):


            #считаем живых соседей
            neidgboursAlive = 0

            k = (n + i - 1) % n
            if mass1[k][j] == 1:
                neidgboursAlive+=1

            k = (n + i + 1) % n
            if mass1[k][j] == 1:
                neidgboursAlive += 1

            k = (n + i - 1) % n
            l = (m + j - 1) % m
            if mass1[k][l] == 1:
                neidgboursAlive += 1

            k = (n + i - 1) % n
            l = (m + j + 1) % m
            if mass1[k][l] == 1:
                neidgboursAlive += 1

            k = (n + i + 1) % n
            l = (m + j - 1) % m
            if mass1[k][l] == 1:
                neidgboursAlive += 1

            k = (n + i + 1) % n
            l = (m + j + 1) % m
            if mass1[k][l] == 1:
                neidgboursAlive += 1

            l = (m + j - 1) % m
            if mass1[i][l] == 1:
                neidgboursAlive += 1

            l = (m + j + 1) % m
            if mass1[i][l] == 1:
                neidgboursAlive += 1


            #считаем следующее поколение в соответствии с правилами
            if mass1[i][j] == 1:
                if neidgboursAlive == 2 or neidgboursAlive == 3 :
                    mass2[i][j] = 1
                else:
                    mass2[i][j] = 0
            else:
                if neidgboursAlive == 3:
                    mass2[i][j] = 1
                else:
                    mass2[i][j] = 0

    generationCounter += 1

def Filling(gen):
    global cellSize
    for j in range(0, m):
        for i in range(0, n):
            if(mass1[i][j]!=mass2[i][j] or gen ==0):
                if mass2[i][j] == 0:
                    canv.create_rectangle(i * cellSize, j * cellSize, (i + 1) * cellSize, (j + 1) * cellSize, fill='Black', outline='Pink')
                else:
                    canv.create_rectangle(i * cellSize, j * cellSize, (i + 1) * cellSize, (j + 1) * cellSize, fill='White', outline='Pink')

#перекрашиваем клетку на которую тыкнули
def MouceClick(event):
    global mass2,cellSize
    x = math.floor(event.x / cellSize)
    y = math.floor(event.y / cellSize)
    print(x,y)
    mass2[x][y] = (mass2[x][y] + 1) % 2

def TimeShift(event):
    global ifTime
    ifTime = (ifTime + 1) % 2
    print(ifTime)

def CheckButtons():
    global root
    root.bind('<1>',MouceClick)
    root.bind('<space>',TimeShift)

def MassEqual():
    global mass1, mass2
    for i in range(n):
        for j in range(m):
            mass1[i][j] = mass2[i][j]

def DrawVerticalLine(i,j,mass2,l):
    for k in range(l):
        mass2[i][j+k]=(mass2[i][j+k]+1)%2

def DrawHorizontalLine(i,j,mass2,l):
    for k in range(l):
        mass2[i+k][j]=(mass2[i][j+k]+1)%2

def DrawSquare(i, j, mass2):
    mass2[i][j] = 1
    mass2[i+1][j] = 1
    mass2[i+1][j+1] = 1
    mass2[i][j+1] = 1

def DrawClocks(i,j,mass2):
    DrawHorizontalLine(i - 1, j - 2, mass2, 4)
    DrawHorizontalLine(i - 1, j + 3, mass2, 4)
    DrawVerticalLine(i - 2, j - 1, mass2, 4)
    DrawVerticalLine(i + 3, j - 1, mass2, 4)
    DrawSquare(i + 1, j - 5, mass2)
    DrawSquare(i - 1, j + 5, mass2)
    DrawSquare(i + 5, j + 1, mass2)
    DrawSquare(i - 5, j - 1, mass2)
    mass2[i-1][j] = (mass2[i-1][j]+1)%2
    mass2[i][j+1] = (mass2[i][j+1]+1)%2
    mass2[i+1][j + 1] = (mass2[i+1][j + 1] + 1) % 2


def DrawGlider(i,j,mass2):

        mass2[i-1][j-1] = 1
        mass2[i-1][j] = 1
        mass2[i][j-1] = 1
        mass2[i][j+1] = 1
        mass2[i+1][j-1]=1

def DrawUniverse(i,j,mass2):

    DrawSquare(i - 1, j - 2, mass2)
    DrawSquare(i + 1, j - 1, mass2)
    DrawSquare(i, j + 1, mass2)
    DrawSquare(i - 2, j, mass2)

    mass2[i - 1][j + 2] = (mass2[i - 1][j + 2] + 1) % 2
    mass2[i - 2][j - 1] = (mass2[i - 2][j - 1] + 1) % 2
    mass2[i + 2][j + 1] = (mass2[i + 2][j + 1] + 1) % 2
    mass2[i + 1][j - 2] = (mass2[i + 1][j - 2] + 1) % 2


    mass2[i - 1][j - 3] = (mass2[i - 1][j - 3] + 1) % 2
    mass2[i - 2][j - 4] = (mass2[i - 2][j - 4] + 1) % 2
    mass2[i - 3][j - 3] = (mass2[i - 3][j - 3] + 1) % 2
    mass2[i - 3][j - 2] = (mass2[i - 3][j - 2] + 1) % 2

    mass2[i + 3][j - 1] = (mass2[i + 3][j - 1] + 1) % 2
    mass2[i + 4][j - 2] = (mass2[i + 4][j - 2] + 1) % 2
    mass2[i + 3][j - 3] = (mass2[i + 3][j - 3] + 1) % 2
    mass2[i + 2][j - 3] = (mass2[i + 2][j - 3] + 1) % 2

    mass2[i - 3][j + 1] = (mass2[i - 3][j + 1] + 1) % 2
    mass2[i - 4][j + 2] = (mass2[i - 4][j + 2] + 1) % 2
    mass2[i - 3][j + 3] = (mass2[i - 3][j + 3] + 1) % 2
    mass2[i - 2][j + 3] = (mass2[i - 2][j + 3] + 1) % 2

    mass2[i + 1][j + 3] = (mass2[i + 1][j + 3] + 1) % 2
    mass2[i + 3][j + 2] = (mass2[i + 3][j + 2] + 1) % 2
    mass2[i + 3][j + 3] = (mass2[i + 3][j + 3] + 1) % 2
    mass2[i + 2][j + 4] = (mass2[i + 2][j + 4] + 1) % 2


    mass2[i - 5][j - 2] = (mass2[i - 5][j - 2] + 1) % 2
    mass2[i - 5][j - 1] = (mass2[i - 5][j - 1] + 1) % 2

    mass2[i + 5][j + 2] = (mass2[i + 5][j + 2] + 1) % 2
    mass2[i + 5][j + 1] = (mass2[i + 5][j + 1] + 1) % 2

    mass2[i + 1][j - 5] = (mass2[i + 1][j - 5] + 1) % 2
    mass2[i + 2][j - 5] = (mass2[i + 2][j - 5] + 1) % 2

    mass2[i - 1][j + 5] = (mass2[i - 1][j + 5] + 1) % 2
    mass2[i - 2][j + 5] = (mass2[i - 2][j + 5] + 1) % 2


def Update():
    global generationCounter, ifTime, mass2, mass1,lifeSpeed
#    print(generationCounter)
    CheckButtons()
    if ifTime:
        CellUpdate()
    Filling(generationCounter)
    MassEqual()
    generationCounter+=1
    root.after(lifeSpeed,Update)

def Start():
    global root, canv, lifeScale, ifTime, generationCounter, n, m, mass1, mass2, cellSize, preset
    rootMenu.destroy()
    root = tk.Tk()
    #fr = tk.Frame(root)
    n = math.floor(lifeScale)
    m = math.floor(lifeScale * 3 / 4)
    s = str(n * cellSize) + "x" + str(m * cellSize)
    root.geometry(s)
    canv = tk.Canvas(root, bg='pink')
    canv.pack(fill=tk.BOTH, expand=1)

    # заполняем 0-ми массивы

    mass1 = [[0 for j in range(m)] for i in range(n)]
    mass2 = [[0 for j in range(m)] for i in range(n)]
    if preset == "glider":
        DrawGlider(math.floor(n/2), math.floor(m/2), mass2)
    if preset == "clock":
        DrawClocks(math.floor(n/2), math.floor(m/2), mass2)
    if preset == "vline":
        DrawVerticalLine(math.floor(n / 2), math.floor(m / 2)-5, mass2, 10)
    if preset == "hline":
        DrawHorizontalLine(math.floor(n/2)-5, math.floor(m/2), mass2, 10)
    if preset == "universe":
        DrawUniverse(math.floor(n/2), math.floor(m/2), mass2)

    #print(lifeScale) #масштаб
    #print(lifeSpeed) #скорость
    ifTime = 0 #остановка времени 0-если время стоит
    generationCounter = 0
    Update()
    root.mainloop()


menubar = Menu(rootMenu)

#General
filemenu = Menu(menubar, tearoff=0)
#filemenu.add_command(label="Open", command=hello)
#filemenu.add_command(label="Save", command=hello)
#filemenu.add_separator()
filemenu.add_command(label="Exit", command=rootMenu.quit)
menubar.add_cascade(label="File", menu=filemenu)
#lifeScale
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="200", command=Scale200)
editmenu.add_command(label="100", command=Scale100)
editmenu.add_command(label="50", command=Scale50)
menubar.add_cascade(label="lifeScale", menu=editmenu)
#lifeSpeed
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="20", command=Speed1)
editmenu.add_command(label="100", command=Speed2)
editmenu.add_command(label="200", command=Speed3)
menubar.add_cascade(label="lifeSpeed", menu=editmenu)
#cellSize
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="10", command=cellSize10)
editmenu.add_command(label="15", command=cellSize15)
editmenu.add_command(label="20", command=cellSize20)
menubar.add_cascade(label="cellSize", menu=editmenu)
#preset
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="glider", command=Glider)
editmenu.add_command(label="clock", command=Clock)
editmenu.add_command(label="verticalLine", command=Vline)
editmenu.add_command(label="horizontalLine", command=Hline)
editmenu.add_command(label="universe", command=Universe)
menubar.add_cascade(label="presets", menu=editmenu)

#Play
editmenu = Menu(menubar, tearoff=0)
menubar.add_command(label="Play",command=Start)
# display the menu
rootMenu.config(menu=menubar)
rootMenu.mainloop()
