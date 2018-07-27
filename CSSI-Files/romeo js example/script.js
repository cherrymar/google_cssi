//This is an example

// let hamlet = "To be or not to be";
// let macbeth = "Full of sound and fury";
//
// console.log( "Hello World" );
// console.log( hamlet + macbeth );
//
// let shake = hamlet + macbeth;
// console.log( shake.substr(0, shake.length / 2 ) );
// console.log( "Half length " + shake.substr(0, shake.length / 2 ).length );
// console.log( "Full length " + shake.length );
//
// let numbers = [42, 12, 21, 3, 9, 7, 5, 3.1415];
// console.log( numbers[1] );
//
// let poem = ["Shall I compare thee to a summers day",
//   "Thou art more temperate",
//   "Do you hear the people sing",
//   "Singing the songs of angry men"
// ];
//
// console.log( poem [3] + hamlet );
// console.log( "The length of poem is: " + poem.length );
//
// if( poem[0].length < 5 )
// {
//   console.log( "Yes it is more than 5" );
// }
// else
// {
//   alert("Danger Will Robinson");
// }
//
//
// let i = 10;
// while( i >= 0 )
// {
//   console.log( "The number is " + i );
//   i --;
// }
//
//
// for( let j = 0; j < 10; j ++ )
// {
//   console.log( "The number is " + j );
// }
//
//
//
// for( let i = 0; i < 4; i ++ )
// {
//   console.log( poem[i] );
// }
//
// for( let i = 3; i >= 0; i -- )
// {
//   console.log( poem[i] );
// }
//
// let backwards;
// for( let i = 0; i < 4; i ++ )
// {
//   backwards = "";
//   let line = poem[i];
//   for( let r = line.length - 1; r >= 0; r -- )
//   {
//     backwards += line.charAt( r );
//   }
//   console.log( backwards );
// }
//
// let temp = poem[0];
// for( let i = 1; i < 4; i ++ )
// {
//   if( poem[i].length > temp.length )
//   {
//     temp = poem[i];
//   }
// }
// console.log( temp );





let exPoem = [ "Grim visaged war hath smooth'd his wrinkled brow",
  "And now, instead of mounting barded steeds",
  "To fright the souls of fearful adversaries",
  "He capers nimbly in a lady's chamber",
  "To the lascivious pleasing of a lute"
];

let exTemp = exPoem[0];
for( let j = 0; j < exPoem.length; j ++ )
{
  if( exPoem[j].length > exTemp.length )
  {
    exTemp = exPoem[j];
  }
}


// console.log( "+".repeat( exTemp.length + 4) );
// for( let i = 0; i < exPoem.length; i ++ )
// {
//   let ans = "+ " + exPoem[i] + " ".repeat( exTemp.length - exPoem[i].length );
//   console.log( ans + " +");
// }
// console.log( "+".repeat( exTemp.length + 4) );



for( let i = 0; i < exPoem.length; i ++ )
{
  printLine( exTemp.length, exPoem[i], exPoem.length );
}

function printLine( lengthLine, line )
{
  console.log( "+ " + line + " ".repeat( lengthLine - line.length ) + " +" );
}
