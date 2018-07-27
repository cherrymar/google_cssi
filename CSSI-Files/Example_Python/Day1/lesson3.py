
# again = 'y'

while raw_input( "Try again? (y/n)" ) != 'n':
    num = int( raw_input( "Give me a numbah: ") )
    word = raw_input( "Give me a noun: " )

    listY = [ "ay", "oy", "uy", "ey" ]
    listCS = [ "sh", "ch" ]

    if word == "deer":
        print( "There are %s %s" % (num, word) )
    else:
        if num == 1:
            print( "There is 1 " + word )
        elif num == 0 or num > 1:
            if word[-3:] == "ife":
                print( "There are %s %sives" % (num, word) )
            elif word[-2:] in listCS:
                print( "There are %s %ses" % (num, word) )
            elif word.endswith("us"):
                print( "There are %s %si" % (num, word[:-2]) )
            elif word[-1:] == "y" and word[-2:] not in listY:
                print( "There are %s %sies" % (num, word[:-1]) )
            elif word == "ox":
                print( "There are %s %sen" % (num, word) )
            elif word == "goose":
                print( "There are %s geese" % num )
            elif word == "mouse":
                print( "There are %s mice" % num )
            else:
                print( "There are %s %ss" % (num, word) )
        # again = raw_input(
        #     "Wouly you like to tray another number? " +
        #     "(y/n)" )


word = "bunnies are cute"
for letter in word:
    print( letter.upper() )



for i in range( 100, 90, -2 ):
    print( i )
