// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
function testMe(a){
  return a + 4;
}


var customer_name;
var balance;
var logged_in = false;
var password;

function openAccount(name, pass, deposit = 0 ){
  balance = 0 + deposit;
  customer_name = name;
  password = pass;
  return name + " has opened a new account with a balance of $" + deposit;
}

function logIn( name, pass )
{
  logged_in = customer_name == name && password == pass;
  return name + " has logged in.";
}

function logOut()
{
  logged_in = false;
  return name + " has logged out.";
}

function deposit(value){
  if( !logged_in )
  {
    return "User must log in";
  }
  else {
    balance += value;
    return customer_name + " has deposited $" + value + ". " + customer_name + "‘s total balance is $" + balance;
  }
}

function withdraw( value )
{
  if( !logged_in )
  {
    return "User must log in";
  }
  else
  {
    if( value > balance )
    {
      return "Sorry, " + customer_name + ", you do not have enough money in your account. You need $" + (value-balance) + " more dollars.";
    }

    else
    {
      balance -= value;//update the value of balance
      return customer_name + " has withdrawn $" + value + ". " + customer_name + "has $" + balance + " remaining.";
    }
  }

}

function customer()
{
  let ans = "";
  ans += openAccount( "Cher", 300 ) + "\n";
  ans += deposit( 50 ) + "\n";
  ans += withdraw( 500 ) + "\n";
  // ans += withdraw( 50 );
  console.log( ans );
}

// Write your script below
