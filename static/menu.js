console.log('yahho')
function $(id) {return document.querySelector(id)}
$("#menu-switch")._b = false
$("#menu-switch").onclick = () =>{
  $("#menu-switch")._b = !$("#menu-switch")._b
  if ($("#menu-switch")._b) {
    $("#menu").style.display = "block"
  }else{
    $("#menu").style.display = "none"
  }
}
