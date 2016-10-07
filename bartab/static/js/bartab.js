var username;
var drinkname;
var drinkprice;

function drinkSubmit()
{
  var request = new XMLHttpRequest();
  var str = "/bartab/submit?name=" + username + "&price=" + drinkprice;
  request.open("GET", str, true);
  request.send(null);
  clearSection();
//  return request.responseText;
  console.log("user: " + username + " drink: " + drinkname + " price: " + drinkprice);
}

function userSelect(user)
{
  clearSection();
  username = user;
  var str = user + " took a ";
  document.getElementById("name").innerHTML = str;
}

function drinkSelect(drink, price)
{
  drinkname = drink;
  drinkprice = price;
  var str = document.getElementById("name").innerHTML;
  str += drink + " for $" + price;
  document.getElementById("name").innerHTML = str;
  document.getElementById("submitButton").style.display = "initial";
}

function clearSection()
{
  document.getElementById("name").innerHTML = null;
  document.getElementById("submitButton").style.display = "none";
}
