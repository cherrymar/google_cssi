import random

words = [
    "museum", "apple", "baby", "yellow",
    "human", "movies", "game", "crazy hot dog",
    "human centipede"
]

def printer( word, taken, wrong ):
    print( "+++++")
    print( "These are the spacings: ")

    string = ""
    for i in word:
        for dash in i:
            if dash in taken:
                string += dash
            else:
                string += "_"
        string += " "
    print( string )

    letters = ""
    for i in taken:
        letters += i + " "
    print( "Used letters: " + letters )
    print( "Lives left : " + str( 5 - wrong ) )
    return string


def makeGuess( taken ):
    flag = True
    guess = ""
    while( flag ):
        guess = raw_input( "Guess a letter: " )
        print( "+++++")
        print( " " )
        if guess not in taken:
            flag = False
    taken += guess
    return guess

def correctGuess( word, guess ):
    ans = 0
    for i in word:
        if guess == i:
            return 0
    return 1


def game():
    word = words[random.randint( 0, len( words )-1 ) ].split()
    taken = ""
    wrong = 0

    flag = True
    while flag:
        remaining = printer( word, taken, wrong )
        temp = makeGuess(taken)
        taken += temp
        wrong += correctGuess( word, temp )
        if wrong >= 5 or remaining + " " == word:
            flag = False



    if "_" in printer( word, taken, wrong ):
        print( "You FAILED!" )
    else:
        print( "WINNER WINNER WINNER!" )


#Actually calling on the game
temp = True
while temp:
    game()
    if raw_input( "Play again? (Y/N): " ).lower() == "n":
        temp = False
