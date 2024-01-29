from Board import Board
from Player import Player
import os, sys, time

class GameController:
    def __init__(self):
        self.players = [Player('X'), Player('O')]
        self.p1starts = 0
        self._board = Board()

    def Start(self) -> None:
        self.UpdateBoard()
        # While game is running
        while True:
            # While a player is moving
            while True:
                throw = self.players[self.p1starts].Play()
                if throw == '0':
                    self.Exit()
                # Move must be accepted
                result = self._board.Check(throw)
                if result == "DONE":
                    self.players[self.p1starts].SetMessage("")
                    # Save move and update the board
                    self._board.Log(throw, self.players[self.p1starts].mark)
                    self.UpdateBoard()
                    if self._board.IsVictory(self.players[self.p1starts].mark):
                        self.Victory(self.players[self.p1starts].mark)
                    break
                # Give feedback to the player
                self.players[self.p1starts].SetMessage(result)
            if self._board.IsGameOver():
                self.GameOver()
            # Change player
            if self.p1starts == 1:
                self.p1starts = 0
            else:
                self.p1starts = 1

    def GameOver(self) -> None:
        print("\nGAME OVER")
        time.sleep(5)
        self._board.Reset()
        self.UpdateBoard()

    def Victory(self, mark) -> None:
        print("\n" + mark + " WINS")
        time.sleep(5)
        if mark == 'X':
            self.players[0].Winner()
        else:
            self.players[1].Winner()
        self._board.Reset()
        self.UpdateBoard()

    def Exit(self) -> None:
        sys.exit()

    #* Clear the screen and show the updated board
    def UpdateBoard(self) -> None:
        os.system('clear')
        print('Player X: ', str(self.players[0].wins), '   Player O: ', str(self.players[1].wins), '   0: Exit')
        self._board.PrintBoard()