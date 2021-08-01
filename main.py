import tkinter
from tkinter import *
from random import randint
import random as rnd
from playsound import playsound
import os

debug = 0
cell_size = 20          #pixels
ms = 30                 #rows and columns
pacman_size=20
agent_turns = 8         #number of blocks agent gets to try for ever one block of cyberpac move

visited_cells = []
walls = []
revisited_cells = []

# creates a list with 50 x 50 "w" items
map = [['w' for _ in range(ms)] for _ in range(ms)]

#array of tuples to keep track of how many times
#the agent has been stuck at this position
stuck_log = []

#one pair for each enemy agent
global xa, ya, xb, yb

xa = randint(1, ms) + cell_size
ya = randint(1, ms) + cell_size
xb = randint(1, ms) + cell_size
yb = randint(1, ms) + cell_size

def draw_pac(row,col,color):
    print("placing pac: x:y",row,col)
    x = col * cell_size
    y = row * cell_size
    ffs.create_oval(x,y,x+10,y+10,fill=color)

def create():
    "Create a rectangle with draw function (below) with random color"
    for row in range(ms):
        for col in range(ms):
            if map[row][col] == 'P':
                color = 'Green'
            elif map[row][col] == 'w':
                color = 'black'
            draw(row, col, color)

#place the pac points
def place_pacs():
    for row in range(ms):
        for col in range(ms):
            if map[row][col] == 'P':
                color = 'Green'
                if row%2 == 0 and col%2 == 0:
                    draw_pac(row, col,"blue")

#play various beeping noises
def beep(soundFile):
    playsound(soundFile)

def draw(row, col, color):
    x1 = col * cell_size
    y1 = row * cell_size
    x2 = x1 + cell_size
    y2 = y1 + cell_size
    ffs.create_rectangle(x1, y1, x2, y2, fill=color)

def check_agent_neighbours(ccr, ccc):
    neighbours = [[
        ccr,
        ccc - 1,
        ccr - 1,
        ccc - 2,
        ccr,
        ccc - 2,
        ccr + 1,
        ccc - 2,
        ccr - 1,
        ccc - 1,
        ccr + 1,
        ccc - 1
    ],

# left
                [ccr, ccc + 1, ccr - 1, ccc + 2, ccr, ccc + 2, ccr + 1, ccc + 2, ccr - 1, ccc + 1, ccr + 1, ccc + 1], #right
                [ccr - 1, ccc, ccr - 2, ccc - 1, ccr - 2, ccc, ccr - 2, ccc + 1, ccr - 1, ccc - 1, ccr - 1, ccc + 1], #top
                [ccr + 1, ccc, ccr + 2, ccc - 1, ccr + 2, ccc, ccr + 2, ccc + 1, ccr + 1, ccc-1, ccr + 1, ccc + 1]] #bottom
    visitable_agent_neighbours = []
    for i in neighbours:                                                                        #find neighbours to visit
        if i[0] > 0 and i[0] < (ms-1) and i[1] > 0 and i[1] < (ms-1):
            if map[i[2]][i[3]] == 'P' or map[i[4]][i[5]] == 'P' or map[i[6]][i[7]] == 'P' or map[i[8]][i[9]] == 'P' or map[i[10]][i[11]] == 'P':
                walls.append(i[0:2])
            else:
                visitable_neighbours.append(i[0:2])
    return visitable_agent_neighbours

def check_neighbours(ccr, ccc):
    neighbours = [[
        ccr,
        ccc - 1,
        ccr - 1,
        ccc - 2,
        ccr,
        ccc - 2,
        ccr + 1,
        ccc - 2,
        ccr - 1,
        ccc - 1,
        ccr + 1,
        ccc - 1
    ],

# left
                [ccr, ccc + 1, ccr - 1, ccc + 2, ccr, ccc + 2, ccr + 1, ccc + 2, ccr - 1, ccc + 1, ccr + 1, ccc + 1], #right
                [ccr - 1, ccc, ccr - 2, ccc - 1, ccr - 2, ccc, ccr - 2, ccc + 1, ccr - 1, ccc - 1, ccr - 1, ccc + 1], #top
                [ccr + 1, ccc, ccr + 2, ccc - 1, ccr + 2, ccc, ccr + 2, ccc + 1, ccr + 1, ccc-1, ccr + 1, ccc + 1]] #bottom
    visitable_neighbours = []
    for i in neighbours:                                                                        #find neighbours to visit
        if i[0] > 0 and i[0] < (ms-1) and i[1] > 0 and i[1] < (ms-1):
            if map[i[2]][i[3]] == 'P' or map[i[4]][i[5]] == 'P' or map[i[6]][i[7]] == 'P' or map[i[8]][i[9]] == 'P' or map[i[10]][i[11]] == 'P':
                walls.append(i[0:2])
            else:
                visitable_neighbours.append(i[0:2])
    return visitable_neighbours

#StartingPoint

# starting color of row
scr = randint(1, ms)

# starting random column
scc = randint(1, ms)
start_color = 'Green'

# memorize row and column of the starting rectangle
# current color row and current color column
ccr, ccc = scr, scc

x1 = ccr * 12
y1 = ccc * 12

print(scr, scc)
print(ccr, ccc)

xa = scr + randint(1, ms) * cell_size
ya = scc + randint(1, ms) * cell_size

map[ccr][ccc] = 'P'

loop = 1

while loop:

    visitable_neighbours = check_neighbours(ccr, ccc)


    if len(visitable_neighbours) != 0:
        d = randint(1, len(visitable_neighbours))-1
        ncr, ncc = visitable_neighbours[d]
        map[ncr][ncc] = 'P'
        visited_cells.append([ncr, ncc])
        ccr, ccc = ncr, ncc

    if len(visitable_neighbours) == 0:
        try:
            ccr, ccc = visited_cells.pop()
            revisited_cells.append([ccr, ccc])

        except:
            loop = 0

window = Tk()
window.title('!! CYBER PAC !!')
canvas_side = ms*cell_size
ffs = Canvas(window, width = canvas_side, height = canvas_side, bg = 'grey')
ffs.pack(pady=20,padx=20)
create()
place_pacs()

y1 = scr * cell_size
x1 = scc * cell_size

draw(scr, scc, start_color)

#try to draw a little round pacman
cyberpac = ffs.create_oval(x1+10,y1+10,x1+30,y1+30)

e = randint(1, len(revisited_cells))-1

ecr = revisited_cells[e][0]
ecc = revisited_cells[e][1]

#colour of the prize pac
pac_color = 'red'

draw_pac(ecr, ecc, pac_color)

# print(revisited_cells)

def draw_rect():
    ffs.create_rectangle((x1, y1, x1 + 12, y1 + 12), fill="Green")

def del_rect():
    ffs.create_rectangle((x1, y1, x1 + cell_size, y1 + cell_size), fill="Green")

def move_agent(xn,yn):
    xnPrev=xn
    ynPrev=yn
    global stuck_log

    #rollover to prevent list out of range errors
    #and add a nice teleporting effect
    if xn < 0:
        xn = 5
        col = w = xn // cell_size
    if yn < 0:
        yn = 5
        row = h = yn // cell_size
    col = w = xn//cell_size
    row = h = yn//cell_size

    #get visitable neighbours for the agent
    #visitable_agent_neighbours = check_agent_neighbours(row, col)
    #print("visitable agent neighbours: ",visitable_agent_neighbours)

    if debug == 1:
        print("agent is at: ", xn, yn)
        print("cyberpac is at: ",x1,y1)

    if abs(xn - x1) < 40 and abs(yn - y1) < 20:
        print("AGENT COLLISION WITH CYBERPAC!!!")
        os.system('say "AGENT COLLISION WITH CYBERPAC!!!"')
    else:
        print("safe")
    #print("block color left: ",map[row][col-1])
    #enemy agent moves 4 times
    options = ['a','d','w','s']
    for turn in range(agent_turns):
        xnPrev=xn
        ynPrev=yn
        rand_index=rnd.randint(0, len(options) - 1)
        option=options[rand_index]
        print(f" DEBUG> row = {row} col {col}")

        stuck_log.append((row,col))

        row, col = rollover_check(row, col,stuck_log)
        if option == "a":
            if map[row][col - 1] == "P":
                xn -= cell_size
        elif option == "d":
            if map[row][col + 1] == "P":
                xn += cell_size
        elif option == "w":
            if map[row - 1][col] == "P":
                yn -= cell_size
        elif option == "s":
            if map[row + 1][col] == "P":
                yn += cell_size
        #erase previous location (visual trick)
        ffs.create_rectangle((xnPrev, ynPrev, xnPrev + cell_size, ynPrev + cell_size), fill="Green")
        #draw the agent
        cyberagent = ffs.create_oval(xn, yn, xn + pacman_size, yn + pacman_size, fill="red")
    stuck_teleportation(row, col)
    return xn,yn

#teleport the agents if they get stucks
def rollover_check(row, col,stuck_log):
    if col > ms - 1 or row > ms - 1:
        col = col - 3
        if map[row][col] == "P":
            return col,row
        if map[row][col + 1] == "P":
            return col,row
        if map[row - 1][col] == "P":
            return col,row
        if map[row + 1][col] == "P":
            return col,row
    return row, col

def stuck_teleportation(row,col):
    stuck = False
    lt = map[row][col - 1]
    rt = map[row][col + 1]
    up = map[row + 1][col]
    dn = map[row - 1][col]
    """if debug == 1:
        print(f"LEFT -> {lt}")
        print(f"RIGHT -> {rt}")
        print(f"UP -> {up}")
        print(f"DOWN -> {dn}")
    """
    #determine if agent is stuck
    if lt == 'w' and rt == 'w' and up == 'up' and down == 'dn':
        print("agent is stuck!")
    return stuck

def move(event):
    global x1, y1
    global xa, ya
    global xb, yb
    if debug == 1:
        print("keypress event: ",event.char)
    del_rect()
    col = w = x1//cell_size
    row = h = y1//cell_size

    if debug == 1:
        print("before", map[row][col])
    if event.char == "a":
        if map[row][col - 1] == "P":
            x1 -= cell_size
    elif event.char == "d":
        if map[row][col + 1] == "P":
            x1 += cell_size
    elif event.char == "w":
        if map[row - 1][col] == "P":
            y1 -= cell_size
    elif event.char == "s":
        if map[row + 1][col] == "P":
            y1 += cell_size
    # try to draw a little round pacman
    cyberpac = ffs.create_oval(x1, y1, x1 + pacman_size, y1 + pacman_size,fill="yellow")
    col = w = x1//cell_size
    row = h = y1//cell_size

    #print("after", map[row][col])

    xa,ya = move_agent(xa,ya)
    xb,yb = move_agent(xb,yb)

window.bind("<Key>", move)
window.mainloop()