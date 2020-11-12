

class PerfecteSpeler:

    def __init__(self, bord, breedte, lengte, kleur):
        self.positions = breedte * lengte
        self.board = bord
        self.breedte = breedte
        self.lengte = lengte
        self.kleur = kleur
        self.oponent = "R" if self.kleur == "G" else "G"

    def get_kleur(self):
        return self.kleur

    def get_zet(self, muntstuk, diepte, alpha, beta):
        free = self.get_free()

        check = self.check(muntstuk)
        if check == 1:
            return [0, (self.positions - diepte)] if muntstuk.get_kleur() != self.kleur else [0, -(self.positions - diepte)]

        if len(free) == 0:
            if diepte % 2 == 0:
                return [0, -(self.positions - diepte)]
            else:
                return [0, self.positions - diepte]

        if diepte % 2 == 0:
            beste = [0, float("-inf")]
            for i in free:
                muntstuk_gezet = i.zet(self.kleur)
                zet = self.get_zet(muntstuk_gezet, diepte + 1, alpha, beta)
                i.undo()

                if zet[1] > beste[1]:
                    zet[0] = i.get_kolom()
                    beste = zet

                alpha = max(alpha, beste[1])

                if beta <= alpha:  # Pruning
                    break

            return beste
        else:
            beste = [0, float("inf")]
            for i in free:
                muntstuk_gezet = i.zet(self.oponent)
                zet = self.get_zet(muntstuk_gezet, diepte + 1, alpha, beta)
                i.undo()

                if zet[1] < beste[1]:
                    zet[0] = i.get_kolom()
                    beste = zet

                beta = min(beta, beste[1])

                if beta <= alpha:  # Pruning
                    break

            return beste

    def get_free(self):
        eind = []
        for kolom in self.board.get_board():
            if kolom.is_free():
                eind.append(kolom)
        return eind

    def check(self, muntstuk):
        aantal_verticaal = 0
        kolom = muntstuk.get_positie()[1]
        rij = muntstuk.get_positie()[0]
        speler = muntstuk.get_kleur()
        for i in range(1, self.board.get_lengte()):
            if self.board.get_board()[kolom].get(i).get_kleur() == speler and self.board.get_board()[kolom].get(i).get_kleur() == self.board.get_board()[kolom].get(i - 1).get_kleur():
                aantal_verticaal += 1
                if aantal_verticaal == 3: # Teken is op papier en je snapt het :)
                    return 1
            else:
                aantal_verticaal = 0

        aantal_horizontaal = 0
        for i in range(1, self.breedte):
            if self.board.get_board()[i].get(rij).get_kleur() == speler and self.board.get_board()[i].get(rij).get_kleur() == self.board.get_board()[i - 1].get(rij).get_kleur():
                aantal_horizontaal += 1
                if aantal_horizontaal == 3:
                    return 1
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
            if self.board.get_board()[start_kolom].get(start_rij).get_kleur() == speler \
                    and self.board.get_board()[start_kolom].get(start_rij).get_kleur() == self.board.get_board()[start_kolom - 1].get(start_rij - 1).get_kleur():
                aantal_schuin += 1
                if aantal_schuin == 3:
                    return 1
            else:
                aantal_schuin = 0

            start_rij += 1
            start_kolom += 1

        return 0