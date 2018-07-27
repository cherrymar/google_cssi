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

# Replace "pass" with your code
import time
class BankAccount(object):
    def __init__( self, label, balance ):
        self.label = label
        self.balance = balance
        self.transactions = []

    def __str__( self ):
        return "Label: %s, Balance: %s" % (self.label, self.balance)

    def withdraw( self, amount ):
        if amount < 0:
            print( "You have attempted to withdraw a negative amount.")
        elif amount > self.balance:
            print( "You do not have enough money." )
        else:
            self.balance -= amount
            self.transactions.append( Transaction( "Withdrawal", amount, "self" ) )
            print( "You have withdrawn %s. Your current balance is %s." % (amount, self.balance) )

    def deposit( self, amount ):
        if amount > 0:
            self.balance += amount
            self.transactions.append( Transaction( "Deposit", amount, "self" ) )
            print( "Your current balance is %s." % self.balance )
        else:
            print( "You have attempted to deposit an negative amount." )

    def rename( self, name ):
        if name == "":
            print( "That is an invalid name." )
        else:
            self.label = name
            print( "Your new label is: " + self.label )

    def print_transactions( self ):
        print( self )
        for i in self.transactions:
            print( i )



#LEVEL 2
    def transfer( self, dest_account, amount ):
        if amount > 0 and self.balance > amount:
            self.withdraw( amount )
            dest_account.deposit( amount )
            self.transactions.append( Transaction( "Transfer", amount, dest_account ) )
        else:
            print( "Transfer is invalid." )

#LEVEL 3
class Transaction( object ):
    def __init__( self, type, amount, dest_account ):
        self.time = time.time()
        self.type = type
        self.amount = amount
        self.dest_account = dest_account

    def __str__( self ):
        return "Time: %s, Type: %s, Amount: %s, Dest Account: %s" % ( self.time, self.type, self.amount, self.dest_account )


acc1 = BankAccount("Carrie", 1000)
acc2 = BankAccount("Selena", 500)

acc1.deposit( 200 )
acc1.deposit( -1 )
acc1.withdraw( 500 )
acc1.withdraw( 10000 )

# acc2.deposit( 300 )
# acc2.deposit( -1 )
# acc2.withdraw( 600 )
# acc2.withdraw( 10000 )

acc1.transfer( acc2, 100 )
# acc2.transfer( acc1, 300 )

acc1.print_transactions()
# acc2.print_transactions()
