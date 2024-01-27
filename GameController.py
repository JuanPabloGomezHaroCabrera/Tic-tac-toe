from Board import Board
from Player import Player
import os, sys, time

class GameController:
    def __init__(self):
        self.players = [Player('X'), Player('O')]
        self.p1starts = 0
        self._board = Board()

    def Start(self):
        while True:
            while True:
                os.system('clear')
                print('Player X: ', str(self.players[0].wins), '   Player O: ', str(self.players[1].wins), '   0 para salir')
                self._board.PrintBoard()
                throw = self.players[self.p1starts].Play()
                if throw == '0':
                    self.Exit()
                result = self._board.Check(throw)
                if result == "DONE":
                    self.players[self.p1starts].SetMessage("")
                    self._board.Log(throw, self.players[self.p1starts].mark)
                    if self._board.IsVictory(self.players[self.p1starts].mark):
                        self.Victory(self.players[self.p1starts].mark)
                    break
                self.players[self.p1starts].SetMessage(result)
            os.system('clear')
            print('Player X: ', str(self.players[0].wins), '   Player O: ', str(self.players[1].wins), '   0 para salir')
            self._board.PrintBoard()
            if self._board.IsGameOver():
                self.GameOver()
            if self.p1starts == 1:
                self.p1starts = 0
            else:
                self.p1starts = 1


    def GameOver(self):
        print("\nGAME OVER")
        time.sleep(5)
        self._board.Reset()

    def Victory(self, mark):
        print("\n" + mark + " WINS")
        time.sleep(5)
        if mark == 'X':
            self.players[0].Winner()
        else:
            self.players[1].Winner()
        self._board.Reset()

    def Exit(self):
        sys.exit()