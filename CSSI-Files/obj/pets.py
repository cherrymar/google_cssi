import math
import datetime as dt

print( dt.date.today() )

petey = {
    "name" : "Petey",
    "animal" : "dog",
    "species" : "corgi",
    "age": 9,            #oxford comma
}

fezzik = {
    "name" : "Fezzik",
    "animal" : "giant",
    "species" : "huge",
    "age" : 30,
}


class Pet(object):
    def __init__(self, name, age ):
        self.name = name
        self.age = age
        self.is_hungry = True
        self.mood = "happy"

    def year_born( self ):
        today = dt.date.today()
        year = today.year
        return year - self.age

    def eat( self ):
        if self.is_hungry:
            self.is_hungry = False
            self.mood = "happy"
        else:
            # I am eating while full
            self.mood = "Bloated"

    def play( self ):
        if self.mood == "happy":
            self.mood = "excited"
        elif self.mood == "excited":
            self.mood = "tired"
        self.is_hungry = True

    def play_with(self, other_pet):
        self.play()
        other_pet.play()

    def __str__(self):
        return self.name + " is "+ str(self.age) + " years old"




class Cup( object ):
    def __init__( self, radius, thickness ):
        self.radius = radius
        self.thickness = thickness
    def info( self ):
        return "The cup has a radius of %s and a thickness of %s" % (self.radius, self.thickness )

wesley = Pet( "Wesley", 25 )
buttercup = Pet( "Buttercup", 72 )


tea_Cup = Cup( 10, 0.4 )
print( tea_Cup.info() )

# print( "Wesley mood: " + wesley.mood )
# print( "Wesley is hungry: " + str(wesley.is_hungry) )
# wesley.play()
# print( "Wesley mood: " + wesley.mood )
# print( "Wesley is hungry: " + str(wesley.is_hungry) )
# wesley.eat()
# print( "Wesley mood: " + wesley.mood )
# print( "Wesley is hungry: " + str(wesley.is_hungry) )
# wesley.eat()
# print( "Wesley mood: " + wesley.mood )
# print( "Wesley is hungry: " + str(wesley.is_hungry) )
# wesley.play()
# wesley.play()
# print( "Wesley mood: " + wesley.mood )
# print( "Wesley is hungry: " + str(wesley.is_hungry) )


fido = Pet( "Fido", 4 )
petey = Pet( "Petey", 7)
fido.play_with( petey )

# print( "fido mood: " + fido.mood )
# print( "fido is hungry: " + str(fido.is_hungry) )
# print( "petey mood: " + petey.mood )
# print( "petey is hungry: " + str(petey.is_hungry) )


print( wesley)
print( buttercup )





#--
