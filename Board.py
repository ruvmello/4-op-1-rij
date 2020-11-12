import Kolom


class Board:

    def __init__(self, lengte, breedte):
        self.board = []
        self.lengte = lengte
        self.breedte = breedte
        self.huidige_speler = "R"
        self.winaar = None

        for i in range(breedte):
            self.board.append(Kolom.Column(lengte, i))

    def __str__(self):
        eind_string = ""
        for i in range(self.lengte):
            for j in range(self.breedte):
                eind_string += self.board[j].get(i).get_kleur() + "\t"
            eind_string += "\n"

        return eind_string

    def get_winnaar(self):
        return self.winaar

    def zet(self, kolom):
        if self.winaar is not None:
            return self

        munt = self.board[kolom].zet(self.huidige_speler)

        if self.check(munt).get_winnaar() is not None:
            if self.winaar == "D":
                print("DRAW")
            else:
                print("\nDe winaar is " + str(self.winaar) + "\n")

        self.huidige_speler = "G" if self.huidige_speler == "R" else "R"

        return munt

    def is_draw(self):
        for i in self.board:
            if i.is_free():
                return False
        self.winaar = "D"
        return True

    def check(self, munt):
        if self.is_draw():
            return self

        rij = munt.get_positie()[0]
        kolom = munt.get_positie()[1]
        aantal_verticaal = 0
        for i in range(1, self.lengte):
            if self.board[kolom].get(i).get_kleur() == self.huidige_speler and self.board[kolom].get(i).get_kleur() == self.board[kolom].get(i - 1).get_kleur():
                aantal_verticaal += 1
                if aantal_verticaal == 3: # Teken is op papier en je snapt het :)
                    self.winaar = self.huidige_speler
                    return self
            else:
                aantal_verticaal = 0

        aantal_horizontaal = 0
        for i in range(1, self.breedte):
            if self.board[i].get(rij).get_kleur() == self.huidige_speler and self.board[i].get(rij).get_kleur() == self.board[i - 1].get(rij).get_kleur():
                aantal_horizontaal += 1
                if aantal_horizontaal == 3:
                    self.winaar = self.huidige_speler
                    return self
            else:
                aantal_horizontaal = 0

        # Check Schuin, we gaan naar de meest links bovenste positie ten opzichte van de zet
        # en gaan zo schuin naar beneden
        start_rij = rij
        start_kolom = kolom
        while start_rij > 0 and start_kolom > 0:
            start_rij -= 1
            start_kolom -= 1

        # Anders wordt er gekeken naar de verkeerde index in de loop de eerste keer
        start_kolom += 1
        start_rij += 1

        aantal_schuin = 0
        while start_rij < self.lengte and start_kolom < self.breedte:
            if self.board[start_kolom].get(start_rij).get_kleur() == self.huidige_speler \
                    and self.board[start_kolom].get(start_rij).get_kleur() == self.board[start_kolom - 1].get(start_rij - 1).get_kleur():
                aantal_schuin += 1
                if aantal_schuin == 3:
                    self.winaar = self.huidige_speler
                    return self
            else:
                aantal_schuin = 0

            start_rij += 1
            start_kolom += 1

        return self

    def get_lengte(self):
        return self.lengte

    def get_board(self):
        return self.board