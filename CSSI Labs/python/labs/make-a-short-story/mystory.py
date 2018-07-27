'''
The (noun1) ran over a (adjective1) (noun2).  Then the (noun2) decided to stop being so (adjective2) and take up a hobby: (verb1-ing). However, suddenly many (noun3) came out from (noun4) and (verb2) the (noun5).
'''

noun1 = raw_input( "Please input a singular noun: " )
adj1 = raw_input( "Please input a singular adjective: " )
noun2 = raw_input( "Please input a singular noun: " )
adj2 = raw_input( "Please input a singular adjective: " )
noun3 = raw_input( "Please input a singular noun: " )
verb1_ing = raw_input( "Please input an 'ing' verb: " )
noun4 = raw_input( "Please input a singular noun: " )
verb2 = raw_input( "Please input a verb: " )
noun5 = raw_input( "Please input a plural noun: " )




print( "The %s ran over a %s %s.  Then the %s decided to stop being so %s and take up a hobby: %s. However, suddenly many %s came out from %s and %s the %s." % (noun1, adj1, noun2, noun2, adj2, verb1_ing, noun3, noun4, verb2, noun5 ) )
