class MyCat:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def miaucz(self):
        print(f"{self.imie} miauczy")

    def baw_sie(self):
        print(f"{self.imie} bawi się")

    def śpij(self):
        print(f"{self.imie} śpi")

mruczek = MyCat("Mruczek", 2)
filemon = MyCat("Filemon", 3)

mruczek.miaucz()
filemon.baw_sie()
filemon.śpij()

