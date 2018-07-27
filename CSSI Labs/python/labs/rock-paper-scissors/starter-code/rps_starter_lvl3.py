#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random


def get_player_move():
    """Asks the user to enter a move as 'r', 'p', or 's', and return it"""
    # TODO
    return raw_input( "Make a move( r, p, s ): " ).lower()


def get_computer_move():
    """Randomly generates the computer's move and
    returns it in the form of 'r', 'p', or 's'"""
    # TODO
    num = random.randint( 1, 3 )
    if num == 1:
        return "r"
    elif num == 2:
        return "p"
    elif num == 3:
        return "s"


def determine_winner(player_move, comp_move):
    """Takes in a player move and computer move each as 'r', 'p', or 's',
    and returns the winner as 'player', 'computer', or 'tie'"""
    # TODO
    if player_move == get_computer_move:
        return "tie"
    if ( player_move == "r" and comp_move == "p" ) or (player_move == "p" and comp_move == "s" ) or (player_move == "s" and comp_move == "r" ):
        return "computer"
    else:
        return "player"


def print_scoreboard(player_wins, comp_wins, ties):
    """Prints out the scoreboard neatly.  Returns nothing."""
    # TODO
    print( "Player wins: " + str(player_wins) )
    print( "Computer wins: " + str(comp_wins) )
    print( "Ties:  " + str(ties) )


def get_move_name(short_move):
    """Takes in 'r', 'p', or 's', and returns 'Rock', 'Paper, or
    'Scissors' respectively. Use this to neatly print move choices"""
    # TODO
    if short_move == "r":
        return "Rock"
    elif short_move == "p":
        return "Paper"
    elif short_move == "s":
        return "Scissors"





def play():
    num = int(raw_input( "How many rounds do you want to play? " ))
    player_wins = 0
    comp_wins = 0
    ties = 0
    for i in range( num ):
        playerMove = get_player_move();
        compMove = get_computer_move();
        winner = determine_winner( playerMove, compMove );
        if winner == "computer":
            comp_wins += 1
        elif winner == "player":
            player_wins += 1
        else:
            ties += 1
        print_scoreboard( player_wins, comp_wins, ties )

    if player_wins > comp_wins:
        print( "You win!" )
    elif player_wins < comp_wins:
        print( "You lost. The computer wins." )
    else:
        print( "You tied!" )



cont = True
while( cont ):
    play()
    cont = raw_input( "Do you want to continue( Yes/No ) " ).lower() == "yes"
# Write your code below - make RPS happen using the functions above!
