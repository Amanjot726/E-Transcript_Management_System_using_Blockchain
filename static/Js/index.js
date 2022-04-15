$(document).ready(function (e) {
  $(document).bind('contextmenu', function (e) {
    return false
  })
})
document.onkeydown = function (e) {
  if (
    e.ctrlKey &&
    (e.keyCode === 67 ||
      e.keyCode === 88 ||
      e.keyCode === 85 ||
      e.keyCode === 73 ||
      e.keyCode === 83 ||
      e.keyCode === 117)
  ) {
    return false
  } else {
    if (e.keyCode === 123) {
      return false
    } else {
      return true
    }
  }
}

function FidC(idv) {
  if (document.getElementById(idv) === null) {
    throw "Error:\n  Unable to find element with id '" + idv + "'"
  } else {
    document.getElementById(idv).click()
  }
}
function Fid(idv) {
  if (document.getElementById(idv) === null) {
    throw "Error:\n  Unable to find element with id '" + idv + "'"
  } else {
    return document.getElementById(idv)
  }
}
function Fcns(cnv) {
  if (document.getElementsByClassName(cnv) === null) {
    throw "Error:\n  Unable to find elements with className '" + cnv + "'"
  } else {
    return document.getElementsByClassName(cnv)
  }
}

// SHOW_HIDE_Password

var x = document.getElementById('pass')
document.getElementById('show-pass').addEventListener('input', function () {
  if (x.type === 'password') {
    x.type = 'text'
  } else {
    x.type = 'password'
  }
})

var un = document.getElementById('uname')
var pass = document.getElementById('pass')
var btn = document.getElementById('login')

un.onkeyup = function () {
  if (un.value.length > 0 && pass.value.length >= 6) {
    btn.removeAttribute('disabled')
  } else {
    btn.disabled = 'true'
  }
}
pass.onkeyup = function () {
  if (un.value.length > 0 && pass.value.length >= 6) {
    btn.removeAttribute('disabled')
  } else {
    btn.disabled = 'true'
  }
}

function validate() {
  var un = document.getElementById('uname')
  var pass = document.getElementById('pass')
  if (un.value.length > 0 && pass.value.length >= 8) {
    document.getElementById('login_form').submit()
  }
}
// window.onload=function(){
//   document.getElementById("ch-auth-su").onclick = function(){document.getElementById('login-f').style.display = "none";document.getElementById('signup-f').style.display = "block";}
//   document.getElementById("ch-auth-li").onclick = function(){document.getElementById('login-f').style.display = "block";document.getElementById('signup-f').style.display = "none";}}

//  myInput.onkeyup = function() {
//   if(myInput.value.length > 0) {
//   document.getElementById("message").style.display = "block";}
