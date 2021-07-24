from tkinter import *
from random import randint

cell_size = 30         #pixels
ms = 30                 #rows and columns
pacman_size=20

visited_cells = []
walls = []
revisited_cells = []

# creates a list with 50 x 50 "w" items
map = [['w' for _ in range(ms)] for _ in range(ms)]

global xa, ya
xa = randint(1, ms) + cell_size
ya = randint(1, ms) + cell_size

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
                color = 'White'
            elif map[row][col] == 'w':
                color = 'black'
            draw(row, col, color)

#place the pac points
def place_pacs():
    for row in range(ms):
        for col in range(ms):
            if map[row][col] == 'P':
                color = 'White'
                if row%2 == 0 and col%2 == 0:
                    draw_pac(row, col,"green")

def draw(row, col, color):
    x1 = col * cell_size
    y1 = row * cell_size
    x2 = x1 + cell_size
    y2 = y1 + cell_size
    ffs.create_rectangle(x1, y1, x2, y2, fill=color)

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
    ffs.create_rectangle((x1, y1, x1 + 12, y1 + 12), fill="green")

def del_rect():
    ffs.create_rectangle((x1, y1, x1 + cell_size, y1 + cell_size), fill="white")

def locate_agent(xa,ya):
    #global xa,ya
    col = w = xa//cell_size
    row = h = ya//cell_size
    print("agent is at: ", row, col)
    print("block color left: ",map[row][col-1])

    if map[row][col-1] == 'w':
        ffs.create_rectangle((xa, ya, xa + cell_size, ya + cell_size), fill="white")
        ya = row*cell_size - cell_size
        print("move agent to: ",xa,ya,map[row][col-1])
        cyberagent = ffs.create_oval(xa, ya, xa + pacman_size, ya + pacman_size, fill="red")
    elif map[row][col+1] == 'w':
        ffs.create_rectangle((xa, ya, xa + cell_size, ya + cell_size), fill="white")
        ya = row*cell_size + cell_size
        print("move agent to: ", xa, ya, map[row][col + 1])
        cyberagent = ffs.create_oval(xa, ya, xa + pacman_size, ya + pacman_size, fill="red")
    else:
        print("agent cannot go up or down")

    if map[row-1][col] == 'w':
        ffs.create_rectangle((xa, ya, xa + cell_size, ya + cell_size), fill="white")
        xa = col*cell_size - cell_size
        print("move agent to: ", xa, ya, map[row-1][col])
        cyberagent = ffs.create_oval(xa, ya, xa + pacman_size, ya + pacman_size, fill="red")
    elif map[row+1][col] == 'w':
        ffs.create_rectangle((xa, ya, xa + cell_size, ya + cell_size), fill="white")
        xa = col*cell_size + cell_size
        print("move agent to: ", xa, ya, map[row+1][col])
        cyberagent = ffs.create_oval(xa, ya, xa + pacman_size, ya + pacman_size, fill="red")
    else:
        print("agent cannot go left or right")
    return xa,ya

def move(event):
    global x1, y1
    global xa, ya
    print("keypress event: ",event.char)
    del_rect()
    col = w = x1//cell_size
    row = h = y1//cell_size
    #print("before", map[row][col])
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
    #print(w, h)
    #print("after", map[row][col])

    xa,ya = locate_agent(xa,ya)

window.bind("<Key>", move)
window.mainloop()