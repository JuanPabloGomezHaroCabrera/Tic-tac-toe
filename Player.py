class Player:
    def __init__(self, mark):
        self.mark = mark
        self.wins = 0
        self.message = ""
    
    def Winner(self) -> None:
        self.wins += 1

    def SetMessage(self, message: str) -> None:
        self.message = message
    
    #* Give feedback if it is neccessary to the player and waits for its move
    def Play(self) -> str:
        print(self.message)
        throw = input(self.mark + " turn player: ")
        return throw        