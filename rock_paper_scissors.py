import random

def play():
    user_input = input("What do you choose? r for rock, p for paper and s for scissors ")
    computer = random.choice(['r','p','s'])
    print( computer)
    print(players(user_input,computer))

def players(x,y): 

    if x == y:
        tie = "it's a tie"
        return tie

    elif ((x == 'r' and y == 's') or (x == 's' and y == 'p') or (
            x == 'p' and y == 'r')):
        return 'you won'

    else:
        return 'you lost!'


play()
