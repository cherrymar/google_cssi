"""
print( "Hello World" )
#I can write a comment after this pound sign
print( "bye bye" )

#variables
name = "Cher Ma"
print( "hi there: "  )
print( name )

#user input

user = raw_input("What's your name? " )
print( "Hi " + user )


num1 = int( raw_input( "Enter a number: " ) )
num2 = int( raw_input( "Enter another number: " ) )
total = num1 + num2
print( total )
"""

x = str(int("2"))
print x + str(1)


userYear = raw_input( "What year were you born in? " )
age = 2018 - int( userYear )
print( "You are " + str( age ) + " years old this year." )


userAge = raw_input( "How old are you this year? " )
year = 2018 - int( userAge )
print( "You were born in " + str( year ) )
