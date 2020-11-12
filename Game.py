import Board as b
import PerfecteSpeler as p
import InputPlayer as ip
import time as t


class Game:

    def __init__(self, lengte, breedte):
        self.board = b.Board(lengte, breedte)
        self.speler1 = p.PerfecteSpeler(self.board, breedte, lengte, "R")
        self.speler2 = ip.InputPlayer(breedte, lengte, self.board)
        self.huidige = self.speler2

    def get_speler1(self):
        return self.speler1

    def get_speler2(self):
        return self.speler2

    def play(self):
        while self.board.get_winnaar() is None:
            start = t.time()
            if self.huidige == self.speler1:
                beste = [0, float("-inf")]
                alpha = float("-inf")
                beta = float("inf")
                for i in self.get_free():
                    muntstuk = i.zet(self.huidige)
                    zet = self.speler1.get_zet(muntstuk, 1, alpha, beta)
                    i.undo()

                    if zet[1] > beste[1]:
                        zet[0] = i.get_kolom()
                        beste = zet

                    alpha = max(alpha, beste[1])

                    if beta <= alpha:
                        break

                self.board.zet(beste[0])
            else:
                self.board.zet(self.speler2.get_zet())
            self.huidige = self.speler1 if self.huidige == self.speler2 else self.speler2
            print(self.board)
            print(t.time() - start)

    def get_free(self):
        eind = []
        for kolom in self.board.get_board():
            if kolom.is_free():
                eind.append(kolom)
        return eind