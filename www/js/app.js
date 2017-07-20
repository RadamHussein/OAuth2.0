function handleClick(){
  console.log("click");
  var request = new XMLHttpRequest();
  request.open("GET", "http://localhost:8080/next", true);
  request.send(null);
  console.log(request.responseText);
}

document.addEventListener('DOMContentLoaded', function(){
  var button = document.getElementById("button");
  button.addEventListener("click", handleClick);
});
