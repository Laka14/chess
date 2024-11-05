"""
class:
store all the info about the current state of a chess game.
determine the valid moves at the current state, keeping a move log..

"""  
class Gamestate():
    def __init__(self):
        # 8x8 2d list
        # b/w -> color
        # 2nd character piece type K -> king, Q-> queen, B-> bishop, ..... 
        self.board=[
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        
        self.whiteToMove = True
        self.movelog = []
