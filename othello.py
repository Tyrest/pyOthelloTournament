#!/usr/bin/env python
"""
othello.py Humberto Henrique Campos Pinheiro
Game initialization and main loop
v2.0 includes edits by Cesar Cesarotti
"""

import pygame
import datetime
import ui
import player
import board
from config import BLACK, WHITE, DEFAULT_LEVEL
import sys
from importlib import import_module

# py2exe workaround
# import sys
# import os
# sys.stdout = open(os.devnull, 'w')
# sys.stderr = open(os.devnull, 'w')


class Othello:
    """
    Game main class.
    """

    def __init__(self, play1=None, play2=None):
        """ Show options screen and start game modules"""
        # start
        self.gui = ui.Gui()
        self.board = board.Board()
        self.logging = True
        self.get_options(play1,play2,DEFAULT_LEVEL)

    def get_options(self, player1, player2, level):
        # set up players
        if player1==None or player2==None:
            player1, player2, level = self.gui.show_options()

        if player1[-3:] == ".py":
            globals()["student1"] = import_module(player1[:-3])
            self.now_playing = student1.BotPlayer(self.gui, BLACK)
        elif player1 == "human":
            self.now_playing = player.Human(self.gui, BLACK)
            self.logging = False
        else:
            self.now_playing = player.Computer(BLACK, level + 3)

        if player2[-3:] == ".py":
            globals()["student2"] = import_module(player2[:-3])
            self.other_player = student2.BotPlayer(self.gui, WHITE)
        elif player2 == "human":
            self.other_player = player.Human(self.gui, WHITE)
            self.logging = False
        else:
            self.other_player = player.Computer(WHITE, level + 3)

        if self.logging:
            timestamp = str(datetime.datetime.today())
            timestamp = timestamp[:timestamp.rfind('.')]
            print(timestamp)
            self.logfile = open("logs/pyOthello game log " + timestamp, "w")
            self.logfile.write("Creating a game between " + str(player1) + "(Black) and " + str(player2) + "(White)\n")
        print("Creating a game between " + str(player1) + " and " + str(player2))

        self.gui.show_game()
        self.gui.update(self.board.board, 2, 2, self.now_playing.color)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            if self.board.game_ended():
                whites, blacks, empty = self.board.count_stones()
                if whites > blacks:
                    winner = WHITE
                    if self.logging:
                        self.logfile.write("The winner is Player 2")
                        print("The winner is Player 2")
                elif blacks > whites:
                    winner = BLACK
                    if self.logging:
                        self.logfile.write("The winner is Player 1")
                        print("The winner is Player 1")
                else:
                    winner = None
                if self.logging:
                    self.logfile.close()
                break
            self.now_playing.get_current_board(self.board)
            if self.board.get_valid_moves(self.now_playing.color) != []:
                score, self.board = self.now_playing.get_move()
                whites, blacks, empty = self.board.count_stones()
                self.gui.update(self.board.board, blacks, whites,
                                self.now_playing.color)
                if self.logging:
                    self.logfile.write(self.board.toString()+'\n')
            self.now_playing, self.other_player = self.other_player, self.now_playing
        self.gui.show_winner(winner)
        pygame.time.wait(1000)
        #self.restart()

    def restart(self):
        self.board = board.Board()
        self.get_options(play1,play2,DEFAULT_LEVEL)
        self.run()


def main():
    legalinputs = ['human','computer']
    if len(sys.argv) > 1:
        if len(sys.argv) == 3:
            player1 = sys.argv[1]
            player2 = sys.argv[2]
            if (player1[-3:] != '.py' and player1 not in legalinputs) or (
                player2[-3:] != '.py' and player2 not in legalinputs):
                print("Legal command line arguments are: human, computer, or the name of a python file with a BotPlayer class.")
            else:
                game = Othello(player1, player2)
                game.run()
        else:
            print("Legal command line arguments are: human, computer, or the name of a python file with a BotPlayer class.")
    else:
        game = Othello()
        game.run()

if __name__ == '__main__':
    main()
