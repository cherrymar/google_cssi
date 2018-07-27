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

console.log("script is running...");

function Basic_Alarm( alarmMessage ) {
  return alarmMessage;
}

console.log( Basic_Alarm( "My alarm!" ) );

function My_Alarm( time )
{
  console.log( "Hey, CHER, wake up! It's " + time );
}

function Mom_Alarm( time )
{
  console.log( "Hey, Mom, wake up! It's " + time );
}

function Family_Alarm( name, time )
{
  console.log( "Hey, " + name + ", wake up! It's " + time );
}

function Important_Alarm( message )
{
  console.log( message.toUpperCase() );
}

function Snooze_Alarm( time )
{
  console.log( "The alarm for " + time + " has been changed to " + (time+1) );
}

function multip_WakeUp( numPpl )
{
  return "Wake up!".repeat( numPpl );
}
