class Player:
    def __init__(self, mark):
        self.mark = mark
        self.wins = 0
        self.message = ""
    
    def Winner(self):
        self.wins += 1

    def SetMessage(self, message):
        self.message = message

    def Play(self):
        print(self.message)
        throw = input(self.mark + " turn player: ")
        return throw
        