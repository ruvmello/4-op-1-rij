import MuntStuk as m


class Column:

    def __init__(self, lengte, kolom_nr):
        self.kolom = []
        self.kolom_nr = kolom_nr
        for i in range(lengte):
            self.kolom.append(m.Munt("O", i, kolom_nr))

    def zet(self, speler):
        for i in range(1, len(self.kolom)):
            if self.kolom[-i].get_kleur() == "O":
                self.kolom[-i].set_kleur(speler)
                return self.kolom[-i]
        self.kolom[0].set_kleur(speler)
        return self.kolom[0]

    def undo(self):
        for i in range(0, len(self.kolom)):
            if self.kolom[i].get_kleur() != "O":
                self.kolom[i].set_kleur("O")
                return len(self.kolom) - i
        return 0

    def is_free(self):
        for i in range(0, len(self.kolom)):
            if self.kolom[i].get_kleur() == "O":
                return True
        return False

    def __len__(self):
        return len(self.kolom)

    def get(self, j):
        return self.kolom[j]

    def get_kolom(self):
        return self.kolom_nr

    def __str__(self):
        eind = ""
        for i in range(len(self.kolom)):
            eind += self.kolom[i].get_kleur() + "\n"
        return eind
