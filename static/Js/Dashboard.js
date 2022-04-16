document.querySelectorAll('.option').forEach(element => {
    element.addEventListener('click', function () {
      element.classList.add('active');
      document.querySelectorAll('.option').forEach(element => {
        if (element.classList.contains('active') && element !== this) {
          element.classList.remove('active');
        }
      });
    });
  });
  
const now = new Date();
const date_option = {day: 'numeric',month: 'long',year: 'numeric'}
const day_option = {weekday: 'long'}
const local = navigator.language
var date = `${new Intl.DateTimeFormat(local,date_option).format(now)}`.replace('/',' ')+', '+`${new Intl.DateTimeFormat(local,day_option).format(now)}`;
document.getElementById('date').innerHTML = date;


var animateButton = function(e) {

    e.preventDefault;
    //reset animation
    e.target.classList.remove('animate');
    
    e.target.classList.add('animate');
    setTimeout(function(){
      e.target.classList.remove('animate');
    },700);
  };
  



var bubblyButtons = document.querySelectorAll(".bubbly-button");

for (var i = 0; i < bubblyButtons.length; i++) {
bubblyButtons[i].addEventListener('click', animateButton, false);
}



var copy_btn = document.querySelector('.copy-button');
copy_btn.addEventListener('click', function() {
    var copyText = document.querySelector(".hash-text");
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(copyText.value)
    var tooltip = document.querySelector(".my-tooltiptext");
    tooltip.innerHTML = "Copied!";
    setTimeout(function(){
        copyText.focus();
        copyText.selectionEnd = copyText.selectionStart;
    },1000);
});
  
copy_btn.addEventListener('mouseout', function() {
    var tooltip = document.querySelector(".my-tooltiptext");
    tooltip.innerHTML = "Copy to clipboard";
});

// function myFunctionORIGINAL() {
//     var copyText = document.getElementById("myInput");
//     copyText.select();
//     navigator.clipboard.writeText(copyText.value)
//     var tooltip = document.getElementById("myTooltip");
//     tooltip.innerHTML = "Copied: " + copyText.value;
// }
  