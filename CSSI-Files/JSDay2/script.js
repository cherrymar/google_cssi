
window.onload = function() {
  let myButton = document.querySelector( "button" );
  myButton.onclick = onButtonClick;
  let myTitle = document.querySelector( "h1" );
  myTitle.onclick = onElementClick;
  let divs = document.querySelectorAll( "div" );
  for( let i = 0; i < divs.length; i ++ )
    divs[i].onclick = onElementClick;
  // myButton.onmouseover = onMouseHover;
}


function divClick( evt ) {
  //console.log( "div element" );
  // if( evt.target.id == "a" )
  //   evt.target.innerText = "Changed a";
  // else {
  //   evt.target.innerText = "Changed b";
  // }

  let myNewElement = document.createElement( "p" );
  if( evt.target.id == "a" )
    myNewElement.innerText = "7";
  else if ( evt.target.id == "b" )
    myNewElement.innerText = "8";
  else if( evt.target.id == "c" )
    myNewElement.innerText = "11";
  evt.target.appendChild( myNewElement );


  // console.log( evt.target );


  // if( evt.target.id = "a" )
  // {
  //   evt.target.innerText = "This is the first div"
  // }
  // else {
  //   evt.target.innerText = "This is the second div"
  // }
  //
  // evt.target.innerText = "New Text";

}

// function onMouseHover() {
//   console.log( "hover" );
//   let myTitle = document.querySelector("h1");
//   // myTitle.style.pointer;
//   myTitle.innerText = "My New Title";
// }
//
// function onMouseOut()
// {
//
// }



function onButtonClick()
{
  let userName = document.querySelector( "#name" );
  let userAddress = document.querySelector( "#address" );
  let userColor = document.querySelector( "#color" );

  let greeting = document.createElement( "p" );
  greeting.innerText = "hello " + userName.value + ", who lives at " + userAddress.value + " and who likes " + userColor.value;
  document.querySelector("div").appendChild( greeting );

  // let myInput = document.querySelector( "input" );
  // console.log( myInput.value );
}

function onElementClick(evt) {
  let clicked = evt.target;
  let clickedParent = evt.target.parentElement;
  console.log( clickedParent);
  let siblings = clickedParent.querySelectorAll("p");
  console.log(siblings);
}




//
// function onElementClick(evt) {
//   let title = document.querySelector( "h1" );
//   title.innerText = "My New Title";
//   console.log( "I was clicked" );
//   changeLines();
// }

function changeLines()
{
  let lines = document.querySelectorAll( ".lines" );

  for( let i = 0; i < lines.length; i ++ )
  {
    lines[i].textContent = "It's BaNaNAs";
    lines[i].style.backgroundColor = "lime";
    lines[i].style.left = "50px";

    if( i == 0 )
    {
      lines[i].style.display = "none";
    }
  }
}









//morning notes
// console.log( "running..." );
//
// let myArray = [
//   "Wrath sing, o goddess, the wrath of Peleus' son Achilles",
//   "the very destructive wrath, that sent many pains to the Acheans",
//   true,
//   4
// ];
//
//
// let achillesMood = "wrathful";
// let achillesNumberOfShips = 50;
// let achillesIsAlive = true;
//
// let achilles = {
//   mood: "wrathful",
//   numberOfShips: 50,
//   isAlive: true,
//   buddies: ["Agemenon", "Petroclus:" ],
//   attack: function () {
//     console.log[ "Yargh!" ];
//   }
// };
//
//
//
// console.log( window );
