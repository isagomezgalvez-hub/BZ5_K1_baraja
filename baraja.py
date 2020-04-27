import random

cartas = ('1', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R')
palos = ('o', 'e', 'c', 'b')


def crea_baraja():
    baraja = []

    for palo in palos:
        for carta in cartas:
            naipe = carta + palo
            baraja.append(naipe)

    return(baraja)


def mezclar(b):
    br = []
    i = 0
    while i < 40:
        n = random.randint(0, 39)
        while b[n] in br:
            n = random.randint(0, 39)
        br.append(b[n])
        i += 1

    b = br

    return b


def repartir(b, players, cards):

    res = []
    for p in range(players):
        res.append([])

    for ic in range(cards):
        for ij in range(players):
            carta = b.pop(0)
            res[ic].append(carta)

        return res
