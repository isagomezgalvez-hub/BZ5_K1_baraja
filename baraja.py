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

    while len(br) != len(b):
        n = random.randint(0, len(b)-1)
        while b[n] in br:
            n = random.randint(0, len(b)-1)
        br.append(b[n])

    b[:] = bbr

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


def invertir(b):
    for i in range(len(b)//2):
        aux = b[i]
        b[i] = b[-1-i]
        b[-1-i] = aux
