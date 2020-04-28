import random


class Baraja():
    cartas = ('1', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R')
    palos = ('o', 'e', 'c', 'b')

    def __init__(self):
        self.__creaBaraja()

    def __creaBaraja(self):
        self.naipes = []
        self.mano = []
        for palo in self.palos:
            for carta in self.cartas:
                naipe = carta + palo
                self.naipes.append(naipe)

    def num_naipes(self):
        return len(self.naipes)

    def mezclar(self):
        br = []
        while len(br) != len(self.naipes):
            n = random.randint(0, len(self.naipes)-1)
            while self.naipes[n] in br:
                n = random.randint(0, len(self.naipes)-1)
            br.append(self.naipes[n])
        self.naipes[:] = br

    def repartir(self, players, cards):

        for p in range(players):
            self.mano.append([])

        for ic in range(cards):
            for ij in range(players):
                carta = self.naipes.pop(0)
                self.mano[ij].append(carta)


def recoger(self):
    self.__creaBaraja()
