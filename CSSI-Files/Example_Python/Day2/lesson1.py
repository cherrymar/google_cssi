def factorial( number ):
    ans = 1
    for i in range( 2, number + 1 ):
        ans *= i
    return ans

def recurseF( num, total ):
    if num == 1:
        return total
    else:
        return recurseF( num - 1, total * num )


# print(factorial(5)) #120
# print(factorial(3)) #6
# print(recurseF(8, 1)) #40320
# print(recurseF(2, 1)) #2


ceri = {
    "species" : "dog",
    "name" : "ceri",
    "sound" : "yip",
    "food" : [ "tuna", "vanilla ice cream" ],
    "age": 8
}

petey = {
    "species" : "dog",
    "name" : "petey",
    "sound" : "woooooof",
    "food" : ["peanut butter", "steak", "tuna"],
    "age" : 9
}

for i in range( len(petey["food"]) ):
    print( "my dog's favorite food is " + petey["food"][i] )











import math
math.sin( 30 )


import datetime
today = datetime.date.today()
today.year
