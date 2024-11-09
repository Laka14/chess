# main driver file.
"""
Class:
Handle user input and current game state
"""
import pygame as p
from ChessEngine import Gamestate

w = h = 512 # width and height 
dim = 8 # dimension 8x8
square_size = h//dim
Images = {}
maxfps = 30 # animation

'''
Initialize a global dictionary of imgs. will be called exactly once
'''

def loadimages():
    pcs = ['wp', 'wR', 'wN', "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
    for pc in pcs:
        #Images[pc] = p.image.load("images/"+pc+".png")
        Images[pc] = p.transform.scale(p.image.load("chess/images/"+pc+".png"), (square_size, square_size))

    #acces an img by 'Images['..']'

'''
the main driver 
handle user input and keep upodating the graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((w, h))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = Gamestate()
    loadimages()
    running = True
    
    sq_select = () #no square is selected, kepp track of the last click of the user(tuple: (row, col))
    player_clicks=[] #keep track of player clicks (two tuples: [(6,4)])
    
    while running:
        for e in p.event.get():
            if e.type== p.QUIT:
                running= False
            
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #(x,y)
                col = location[0]//square_size
                row = location[1]//square_size
                
        
        drawGameState(screen, gs)
        clock.tick(maxfps)
        p.display.flip()

def drawGameState(screen, gs):
    drawboard(screen)
    drawpieces(screen, gs.board)

'''
draw squares
'''

def drawboard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(dim):
        for col in range(dim):
            color  = colors[((row+col)%2)]
            p.draw.rect(screen, color, p.Rect(col*square_size, row*square_size, square_size, square_size))


'''
draw pieces
'''

def drawpieces(screen, board):
    # pass
    for row in range(dim):
        for col in range(dim):
            pc = board[row][col]
            if pc != "--":#empty, leave blank
                screen.blit(Images[pc], p.Rect(col*square_size, row*square_size, square_size, square_size)) 
            

if __name__ == "__main__":
    main()