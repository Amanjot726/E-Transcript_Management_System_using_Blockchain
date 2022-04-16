
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