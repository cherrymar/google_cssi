window.onload = function() {
  let wordClick = document.querySelectorAll( "span" );
  for( let i = 0; i < wordClick.length; i ++)
  {
    wordClick[i].onclick = onWordClick;
  }

  let inputClick = document.querySelectorAll( "input" );
  for( let i = 0; i < inputClick.length; i ++)
  {
    inputClick[i].onclick = onInputClick;
  }
}

newRed = rgb(178, 7, 29);
function onWordClick(evt)
{
  if( evt.target.style.color == "rgb(178, 7, 29)")
  {
    evt.target.style.color = "green";
  }

  else {
    evt.target.style.color = "rgb(178, 7, 29)";
  }
}


function onInputClick(evt)
{
  evt.target.value = "";
}
