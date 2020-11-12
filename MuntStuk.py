
class Munt:

    def __init__(self, kleur, rij, kolom):
        self.color = kleur
        self.pos = (rij, kolom)

    def get_kleur(self):
        return self.color

    def set_kleur(self, kleur):
        self.color = kleur

    def get_positie(self):
        return self.pos