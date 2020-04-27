cartas = ['1', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']
palos = ['o', 'e', 'c', 'b']


for palo in palos:
    for carta in cartas:
        naipe = carta + palo
        baraja.append(naipe)

print(baraja)
