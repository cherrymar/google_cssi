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

console.log("Running Click Events Script");


window.onload = function() {
  let row1 = document.querySelectorAll( "#container1" );
  for( let i = 0; i < row1.length; i ++ )
    row1[i].onclick = onRow1Click;

  let row2 = document.querySelectorAll( "#container2" );
  for( let i = 0; i < row2.length; i ++ )
    row2[i].onclick = onRow2Click;
}




//*****Row 3




//*****Row 2
let r2CounterY = 0;
let r2CounterB = 1;

function onRow2Click( evt )
{

  if( evt.target.id == "box4" )
  {
    toggle( evt, r2CounterY );
    r2CounterY ++;
  }

  else if( evt.target.id == "box5" )
  {
    toggle( evt, r2CounterB );
    r2CounterB ++;
  }
}

function toggle( evt, counter )
{
  if( counter % 2 == 0 )
    evt.target.style.backgroundColor = "yellow";
  else
    evt.target.style.backgroundColor = "blue";
}





//*****Row 1
function onRow1Click( evt ) {

  let clickedParent = evt.target.parentElement;
  let siblings = clickedParent.querySelectorAll(".box");

  if( evt.target.id == "box1" )
  {
    siblings[1].style.backgroundColor = "red";
    siblings[2].style.backgroundColor = "red";
  }

  else if( evt.target.id == "box2" )
  {
    siblings[0].style.backgroundColor = "pink";
    siblings[2].style.backgroundColor = "pink";
  }

  else if( evt.target.id == "box3" )
  {
    siblings[0].style.backgroundColor = "orange";
    siblings[1].style.backgroundColor = "orange";
  }



//Carlos info
// elements = containerOne.querySelectorAll( "div" );
// info.target.style.backgroundColor = getCssBackgroundColor( document.getElementById( info.target.id) );
// for( let i = o, i < elements.length; i ++ )
// {
//   elements[i].style.backgroundColor = info.target.style.backgroundColor;
// }
//
// function getCssBackgroundColor( element ) {
//   let style = window.getComputedStyle( element, "" );
//   console.log( style.getPropertyValue( "background-color" ) );
//   return style.getPropertyValue( "background-color" );
// }
