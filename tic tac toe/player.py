class Player:
    def __init__(self) :
        self.name=''
        self.symbol=''
    def chooseName(self):
        while true:
            name=input('enter your name')
            if name.isalpha():
                self.name=name
                break
            else print('name can contain only letters')
    def chooseSymbol(self):
        while true:
            symbol=input('enter your symbol')
            if symbol.isalpha() and len(symbol)==1:
                self.symbol==symbol.upper()
                break
            print("symbol must be only one letter")


