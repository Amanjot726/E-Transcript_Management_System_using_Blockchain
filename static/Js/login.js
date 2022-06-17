
  // SHOW_HIDE_Password
  
  var x = document.getElementById('pass')
  document.getElementById('show-pass').addEventListener('input', function () {
    if (x.type === 'password') {
      x.type = 'text'
    } else {
      x.type = 'password'
    }
  })
  
  
  var login_btn = document.getElementById('login');

  login_btn.addEventListener('click', function () {
    document.getElementById('login_form').submit();
  });

  
  // document.getElementById('login_form').submit()
  // var un = document.getElementById('uname');
  // var pass = document.getElementById('pass');
  // var btn = document.getElementById('login');
  
  // function validate() {
  //   console.log('called');
  //   if (un.value.length > 0 && pass.value.length >= 6) {
  //     btn.removeAttribute('disabled');
  //   } else {
  //     btn.disabled = 'true';
  //   }
  // }

  // // window.onload = function () {console.log('loaded');validate()};
  // form.onfocus = function () {validate()};
  // form.onmouseenter = function () {validate();un.focus();un.setAttribute('autocomplete', 'true');};
  // un.onkeyup = function () {validate()};
  // pass.onkeyup = function () {validate()};
  // un.onchange = function () {validate()};
  // pass.onchange = function () {validate()};