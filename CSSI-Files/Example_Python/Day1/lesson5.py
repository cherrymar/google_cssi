#dictionaries

states = {
    "NJ" : "New Jersey",
    "VT" : "Vermont",
    "WA" : "Washington",
    "TX" : ["Texas", "TEXASISGREAT"]
}

# print( states )

# print( states["VT"] ) #get value
# print( states["TX"])
# print( states["TX"][1])  #get index of the list
# print( states["NJ"][1])  #get letter at index one

states["NJ"] = states["NJ"][1].upper()
# print( states )

for i in states:
    if states[i] == "Washington":
        print( "We found it!" )
        print( "The key is: " + i )

    else:
        print( "Not here" )
