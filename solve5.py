""" Giorgio, grande esperto di previsioni meteo riconosciuto mondialmente, ha di nuovo bisogno del tuo aiuto
per decidere se pioverà oppure no, basandosi sui valori di pressione registrati dai suoi sofisticatissimi
apparecchi.
Giorgio deve stabilire una soglia di pressione oltre la quale decretare che pioverà. Per ogni giorno, il
verdetto è pioggia se e solo se il valore di pressione (che varia tra 0 e 100) è maggiore o uguale della soglia
(che anch’essa può variare tra 0 e 100).

"""


def solve(parks, actions):

    free = []

    for i in range(0, len(parks)):
        free.append(0)

    for command in actions:
        splitted = str(command).split(" ")
        if splitted[0] is "P":
            amount = int(splitted[1])
            index = int(splitted[2])

            clean_up(free, amount, index, parks)

        elif splitted[0] is "M":

            index = int(splitted[1])
            print(free[index])

        else:
            print("Wrong command syntax")

    return -1


def clean_up(free, amount, index, trail):

    if index > len(free)-1:
        return

    max_value = trail[index]

    if amount > max_value:
        left = amount - (max_value - free[index])
        free[index] = max_value
        clean_up(free, left, index+1, trail)
    else:
        usable = max_value-free[index]
        if amount <= usable:
            free[index] = free[index]+amount
        else:
            free[index] = max_value
            clean_up(free, amount-(max_value-free[index]), index+1, trail)


solve((3, 3, 1, 1), [
    "P 4 0",
    "P 3 0",
    "M 2"
])
