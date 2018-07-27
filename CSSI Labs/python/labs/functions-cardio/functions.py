def longest_word( word1, word2, word3 ):
    temp = word1
    if len(word2) > len(temp):
        temp = word2
    if len(word3) > len(temp):
        temp = word3
    return temp;

# print( longest_word( "hi", "bye", "hello" ) ) # => hello
# print( longest_word( "Carlos", "Cher", "Harry" ) ) # => Carlos



def reverse_string( word ):
    ans = "";
    for i in range( len(word), -1, -1 ):
        ans += word[i:1+i]
    return ans
    #word[::-1] GET REVERSE ORDER

# print( reverse_string( "hello" ) ) # => !olleh
# print( reverse_string( "human" ) ) # => namuh



def sum_to_n(num):
    ans = 0;
    for i in range( num + 1 ):
        ans += i;
    return ans

# print( sum_to_n( 4 ) ) # => 10
# print( sum_to_n( 7 ) ) # => 28



def is_triangle( s1, s2, s3 ):
    if s1 + s2 > s3 and s2 + s3 > s1 and s3 + s1 > s2:
        return True
    return False

# print( is_triangle( 1, 2, 3 ) ) # => false
# print( is_triangle( 2, 2, 3 ) ) # => false

import random
def roll_dice( num ):
    temp = 0;
    for i in range( num ):
        temp += random.randint( 1, 6 )
    return temp

# print( roll_dice(2) );
# print( roll_dice(5) );



def isPrime( num ):
    if num in range( 1, 4):
        return True
    for i in range( 2, int( (num) / 2 ) + 1 ):
        # print( i )
        if num % i == 0:
            return False
    return True

# print( isPrime(1) ); # => true
# print( isPrime(2) ); # => true
# print( isPrime(3) ); # => true
# print( isPrime(4) ); # => false
# print( isPrime(5) ); # => true
# print( isPrime(9) ); # => false


def snake_case( word ):
    ans = ""
    for c in word:
        if c.isupper():
            ans += "-" + c.lower()
        else:
            ans += c
    return ans

# print( snake_case( "helloWorld" ) ) # => hello-world
# print( snake_case( "camelCase" ) ) # => camel-case



def get_number_input( string ):
    ans = 0
    while raw_input( string ) IS NOT A NUMBER:
        
