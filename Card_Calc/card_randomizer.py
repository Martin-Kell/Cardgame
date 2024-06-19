import random

def pull_card ():

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    randomcardnumber = random.randint(1,13)

    randomcardsuit = random.randint(0,3)
        
    if randomcardnumber == 13: print('King of', suits[randomcardsuit])
    elif randomcardnumber == 12: print('Queen of', suits[randomcardsuit])  
    elif randomcardnumber == 11: print('Jack of', suits[randomcardsuit])
    elif randomcardnumber == 1: print('Ace of', suits[randomcardsuit]) 
    else: print(randomcardnumber, 'of', suits[randomcardsuit]) 




