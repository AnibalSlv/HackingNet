from engine.player import Player

class Core:
    def __init__(self):
        self.player = Player()

    def buy_item(self) -> None:
        self.player.money -= 10 