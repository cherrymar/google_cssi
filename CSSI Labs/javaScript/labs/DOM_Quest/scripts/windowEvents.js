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

console.log("Running Window Events Script");
window.addEventListener("keypress", e=> {
console.log(e.keyCode);
})

let box6 = document.querySelector("#box6");
//*****Row 3 space bar --> color change (change shape and size)
window.addEventListener("keypress", e=> {
  console.log( "This is running." );
  if( e.keyCode == 32 )
  {
    let canvas = document.getElementById( "box6" );
    centert = canvas.getContext( "2d" );
    centerx = canvas.width/2;
    centerY = canvas.height / 2;

    // box6.style.arc = "red";
    // console.log.
    //Change size
    // document.querySelector("#box6").style.height = document.querySelector("#box6").style.height / 2;
    // document.querySelector("#box6").style.width = document.querySelector("#box6").style.width / 2;
    //document.getElementById('cercle1').style.height = "10px";
    // let box = document.querySelectorAll( "#box6" );
    // evt.target.style.backgroundColor = "yellow";
  }

})



window.addEventListener("keypress", e=> {
  // console.log( "This is running." );
  if( e.keyCode == 99 ) //letter "c"
  {
    document.querySelector("#box6").style.backgroundColor = "red";
    // let box = document.querySelectorAll( "#box6" );
    // evt.target.style.backgroundColor = "yellow";
  }
  if( e.keyCode ==  115)
  {
    document.querySelector("#box6").style.backgroundColor = "purple";
  }

})
