def greetAgent():
    print( "Bond, James Bond." )

# for i in range( 5 ):
#     greetAgent()

#MUST CALL METHODS AFTER THEY ARE DECLARED!!!!

def greeting( first_name, last_name ):
    return str( "%s, %s %s" % (last_name, first_name, last_name )  )

# print(greeting( "Cher", "Ma" ))
# print(greeting( "Elizabeth", "Zietz" ))
# agent1 = greeting( "Hana", "Tadesse" )
# print( agent1 )


agents = [greeting("Damon", "Hines"),
            greeting( "Hana", "Tadesse" ),
            greeting( "Lina", "Park" )
            ]

# print( agents )


agents[0] = "See-mong"
agents.append( "Damon")
agents.append( "Maireen" )
agents.append( "Miguel" )

print( agents )
print( len( agents ) )

#print all objects in list
for i in range( len( agents) ):
    print( agents[i] )
#print all objects in list
for i in agents:
    print( i )
#print all objects backwards in list
for a in reversed( agents ):
    print( a )
#print all objects backwards in list
agents.reverse()
for a in agents:
    print( a )

if "Damon" in agents:
    print( "Congratulations for making it back to being an agent!" )

agents.remove( "See-mong" )
print( agents )
