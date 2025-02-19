import os

grid = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

spritesx = [0,0,0,0,0]
spritesy = [0,0,0,0,0]
sprites_display = [0,0,0,0,0]
sprites_Bdisplay = [0,0,0,0,0]

def render_grid():
    for row in grid:
        for index in row:
            print(index,end = " ")
        print("")

def add_pixel(x,y,output):
    if not output == 0:
        grid[y][x] = output

def clear_grid():
    os.system('clear')

def get_input():
    inp = input()
    return inp

def create_spr(x,y,display,sprNUM):
    sprites_Bdisplay[sprNUM] = grid[y][x]
    spritesx[sprNUM] = x
    spritesy[sprNUM] = y;
    sprites_display[sprNUM] = display;

def show_spr(sprNUM):
    add_pixel(spritesx[sprNUM],spritesy[sprNUM],sprites_display[sprNUM])

def move_spr(x,y,sprNUM):
    add_pixel(spritesx[sprNUM],spritesx[sprNUM],sprites_Bdisplay[sprNUM])
    spritesx[sprNUM] = x
    spritesy[sprNUM] = y;

def set_bkg_image(image):
    file = open(image,"r")
    content = file.read()
    index = 0
    yindex = 1
    grid[0][0] = content[0]
    grid[0][1] = content[1]
    grid[0][2] = content[2]
    grid[0][3] = content[3]
    grid[0][4] = content[4]
    grid[1][0] = content[6]
    grid[1][1] = content[7]
    grid[1][2] = content[8]
    grid[1][3] = content[9]
    grid[1][4] = content[10]
    grid[2][0] = content[12]
    grid[2][1] = content[13]
    grid[2][2] = content[14]
    grid[2][3] = content[15]
    grid[2][4] = content[16]
    grid[3][0] = content[18]
    grid[3][1] = content[19]
    grid[3][2] = content[20]
    grid[3][3] = content[21]
    grid[3][4] = content[22]
    grid[4][0] = content[24]
    grid[4][1] = content[25]
    grid[4][2] = content[26]
    grid[4][3] = content[27]
    grid[4][4] = content[28]

def get_grid_spot(x,y):
    spot = grid[y][x]
    return spot

def collide_spr(sprNUM1,sprNUM2):
    output = False
    if spritesx[sprNUM1] == spritesx[sprNUM2]:
        if spritesy[sprNUM2] == spritesy[sprNUM1]:
            output = True
    return output

def check_spr_pos(spr,x,y):
    spr_x = spritesx[spr]
    spr_y = spritesy[spr]
    output = False
    if x == spr_x:
        if y == spr_y:
            output = True
    return output

clear_grid()