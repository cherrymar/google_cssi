function greet( name1, name2 )
{
  console.log( "Hello, " + name1 );
  console.log( "Hello, " + name2 );
}

function greetTwice( name )
{
  greet(name);
  greet(name);
}


function makeReturnValue() {
  return "Android";
}


function messageBars( message )
{
  console.log( "+".repeat( 40 ) );
  console.log( message );
  console.log( "+".repeat(40) );
}
