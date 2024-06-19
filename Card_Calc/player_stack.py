import numpy as np
import card_randomizer as card

def player_count():

    numberofplayers = input('How many players?\n-> ')

    table = np.zeros((int(numberofplayers) + 1, 5), dtype=str)
    table[0,0] ='Dealer'

    print(table)

    titles = 0

    #for titles in range(numberofplayers):




player_count()

for i in range(2):
    card.pull_card()
    i += 1


