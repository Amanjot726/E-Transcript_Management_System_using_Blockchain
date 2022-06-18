
  // SHOW_HIDE_Password
  
  var x = document.getElementById('pass')
  document.getElementById('show-pass').addEventListener('input', function () {
    if (x.type === 'password') {
      x.type = 'text'
    } else {
      x.type = 'password'
    }
  })
  
  // create Element
  function create__element(Id, Class, InnerHTML, Type='div', Parent=document.body) {
    var element = document.createElement(Type);
    if (Id != undefined) element.id = Id;
    if (Class != undefined) element.className = Class;
    if (InnerHTML != undefined) element.innerHTML = InnerHTML;
    Parent.appendChild(element);
  }
  function snackbar(Notification) {if(document.getElementById("snackbar") == undefined){create__element('snackbar')};var x = document.getElementById("snackbar");x.innerHTML=Notification;x.className = "show";setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);}


  var login_form = document.getElementById('login_form');
  var login_btn = document.getElementById('login');
  var informed = false;

  window.onload = function(){
    login_form.reset();
    setTimeout(()=>{login_form.reset();}, 10);
    if (login_form.dataset.login_status == "False" && !informed) {
      try{
        setTimeout(()=>{$('#LoginStatus').modal('show');}, 300);
      }catch(e){
        alert("Login Failed");
      }
      informed = true;
    }
  }
  
  // login_btn.addEventListener('click', function () {
  //   login_form.submit();
  // });


// var login_form = document.getElementById("my-form");
// var s_form_check = 0;
async function handleLogin(event) {
  login_btn.innerHTML = '<div class="spinner-border text-success" role="status"></div>';
  event.preventDefault();
  login_btn.style.transition = 'none';
  login_btn.style.backgroundColor = 'transparent';

  var data = new FormData(event.target);
  if (data.get("username") == ""){
    document.querySelector('#uname').setAttribute('required', '');
    snackbar("Please fill the Username");
    return;
  }
  else{
    if (data.get("password") == ""){
      document.querySelector('#pass').setAttribute('required', '');
      snackbar("Please fill the Username");
      return;
    }
    else{
      data.set('js_status', 'Enabled');
      fetch(event.target.action, {
        method: login_form.method,
        body: data,
        headers: {
            'Accept': 'application/json'
        }
      }).then(async response => {
        setTimeout(()=>{login_btn.innerHTML = 'Login';login_btn.removeAttribute('style');},300);
        if (response.ok) {
          await response.json().then((result) => {
            if (result.login_success == true) {
              window.location.href = result.redirect;
            }
            else{
              try{
                $('#LoginStatus').modal('show');
              }catch(e){
                alert("Login Failed");
              }
            }
          });
          login_form.reset();
        } 
        else {
          try{
            snackbar("Oops! Facing some issues<br>Please try again later");
          }catch(e){
            alert("Oops! Facing some issues\nPlease try again later");
          }
        }
      }).catch(error => {
        // console.log(error);
        try{
          snackbar("Oops! Facing some issues<br>Please try again later");
        }catch(e){
          alert("Oops! Facing some issues\nPlease try again later");
        }
        setTimeout(()=>{login_btn.innerHTML = 'Login';login_btn.removeAttribute('style');},500);
      });
    }
  }
}
login_form.addEventListener("submit", function(event){
  login_btn.innerHTML = '<div class="spinner-border text-success" role="status"></div>';
  login_btn.style.transition = 'none';
  login_btn.style.backgroundColor = 'transparent';
  event.preventDefault();
  handleLogin(event);
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