name1 = "Joe"
name2 = "Carlos"
name3 = "Lauren"
name4 = "Min"


print( "Hi %s, %s, %s, and %s" % #you can line break w/in a "()"
    (name1, name2, name3, name4 ) ) #only need parenthesis around names if there are multiple

print( "My favorite number is %s" % 7 )


#conditionals
num = int( raw_input( "Enter a number: "))

if num > 0:
    print( "This is a positive number." )
    if num % 2 == 0:
        print( "This is an even number")
    else:
        print( "This is an odd number" )
elif num < 0:
    print( "This is a negative number." )
else:
    print( "This number is zero" )
