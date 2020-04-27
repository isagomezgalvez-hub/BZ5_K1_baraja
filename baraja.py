cartas = ('1', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R')
palos = ('o', 'e', 'c', 'b')


def crea_baraja():
    baraja = []

    for palo in palos:
        for carta in cartas:
            naipe = carta + palo
            baraja.append(naipe)

    return(baraja)
