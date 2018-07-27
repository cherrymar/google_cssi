
//Grains of Rice
function square( num )
{
  return Math.pow( 2, num - 1);
}

function total( num )
{
  // let ans = 0;
  // for( let i = 1; i <= num; i ++  )
  // {
  //   ans += square( i );
  // }
  // return ans;
  return square( num + 1 ) - 1;
}


//Simple Elevator
// var elevatorLine = [];
//
//
// function pressFloorNumber( elevatorLine, floor )
// {
//   elevatorLine.push( floor );
//   return "Position " + elevatorLine.length;
// }
//
//
// function goToNextFloor()
// {
//   if( elevatorLine.length == 0 )
//   {
//     return "There are no more floors to go to";
//   }
//
//   else
//   {
//     let temp = elevatorLine[0];
//     elevatorLine.shift();
//     return "Floor " + temp;
//   }
// }
//
// function currentLine()
// {
//   if( elevatorLine.length == 0 )
//   {
//     return "The line is currently empty.";
//   }
//
//   else {
//     let ans = "The line is currently: ";
//     for( let i = 0; i < elevatorLine.length; i ++ )
//     {
//       ans += "Floor " + elevatorLine[i];
//       if( i != elevatorLine.length - 1 )
//       {
//         ans += ", ";
//       }
//     }
//     return ans;
//   }
//
// }


//Most Recent elevator
var elevatorLine = [];


function pressFloorNumber( elevatorLine, floor )
{
  elevatorLine.push( floor );
  return "Position 1";
}


function goToNextFloor()
{
  if( elevatorLine.length == 0 )
  {
    return "There are no more floors to go to";
  }

  else
  {
    return "Floor " + elevatorLine.pop();
  }
}

function currentLine()
{
  if( elevatorLine.length == 0 )
  {
    return "The line is currently empty.";
  }


  else
  {
    let ans = "The line is currently: ";
    for( let i = elevatorLine.length - 1; i >= 0; i -- )
    {
      ans += "Floor " + elevatorLine[i];
      if( i != 0 )
      {
        ans += ", ";
      }
    }
    return ans;
  }
}
