class Board:
    def __init__(self):
        self.board = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ',
                      '6': ' ', '7': ' ', '8': ' ', '9': ' '}
        self.guide = "\tGUIDE\n1 2 3\n4 5 6\n7 8 9\n"
        
    def Reset(self) -> None:
        for index in self.board:
            self.board[index] = ' '

    #* Check if the index exists in the board and if it is empty
    def Check(self, index: str) -> str:
        if index in self.board and self.board[index] == ' ':
            return "DONE"
        return "INVALID INPUT"

    def Log(self, index: str, mark: str) -> None:
        self.board[index] = mark

    def IsVictory(self, mark: str) -> bool:
        if ((self.board['1'] == mark and self.board['2'] == mark and self.board['3'] == mark) or 
        (self.board['4'] == mark and self.board['5'] == mark and self.board['6'] == mark) or 
        (self.board['7'] == mark and self.board['8'] == mark and self.board['9'] == mark) or 
        (self.board['1'] == mark and self.board['4'] == mark and self.board['7'] == mark) or 
        (self.board['2'] == mark and self.board['5'] == mark and self.board['8'] == mark) or 
        (self.board['3'] == mark and self.board['6'] == mark and self.board['9'] == mark) or 
        (self.board['1'] == mark and self.board['5'] == mark and self.board['9'] == mark) or 
        (self.board['3'] == mark and self.board['5'] == mark and self.board['7'] == mark)):
            return True
        return False

    def IsGameOver(self) -> bool:
        if ' ' not in self.board.values():
            return True
        return False

    def PrintBoard(self) -> None:
        print(self.guide)
        print(self.board['1'] + "|" + self.board['2'] + "|" + self.board['3'])
        print("-+-+-")
        print(self.board['4'] + "|" + self.board['5'] + "|" + self.board['6'])
        print("-+-+-")
        print(self.board['7'] + "|" + self.board['8'] + "|" + self.board['9'])