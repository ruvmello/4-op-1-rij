class InputPlayer:

    def __init__(self, breedte, lengte, board):
        self.board = board
        self.breedte = breedte
        self.lengte = lengte

    def get_zet(self):
        inp = int(input("Geef de volgende zet:"))
        while inp > self.breedte - 1 or inp < 0 or not self.board.get_board()[inp].is_free():
            inp = int(input("Geen geldige zet, geef een geldige zet:"))
        return inp