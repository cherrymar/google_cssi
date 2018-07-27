#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licens es/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

choice = ""

print("Welcome to the shopping list app!")

shopping_list = []

while choice.lower() != "e":
    print("Please choose your action from the following list:")
    print("a. Add an item to the list")
    print("b. Remove an item from the list")
    print("c. Check to see if an item is on the list")
    print("d. Show all items on the list")
    print("e. exit")

    choice = raw_input("Enter your choice [a|b|c|d|e]: ")
    if choice == "a":
        item = raw_input( "What do you wish to add? " ).lower()
        if item not in shopping_list:
            shopping_list.append(item)
        else:
            print( "This item is already in the list.")
    elif choice == "b":
        item = raw_input( "What do you wish to remove? " )
        if item in shopping_list:
            ans = raw_input( "Are you sure you want to remove %s? [Y|N] " % item ).lower()
            if ans == "y":
                shopping_list.remove( item )
            else:
                print( item + " was removed." )
        else:
            print( item + " was NOT in list.")
    elif choice == "c":
        item = raw_input( "What item are you looking for? " )
        if item in shopping_list:
            print( item + " is in the list" )
            if raw_input( "Would you like to remove this item?[Y|N] ").lower() == "y":
                shopping_list.remove( item )
        else:
            print( item + " is NOT in the list" )
            if raw_input( "Would you like to add this item?[Y|N] ").lower() == "y":
                shopping_list.append(item)
    elif choice == "d":
        print( shopping_list )
