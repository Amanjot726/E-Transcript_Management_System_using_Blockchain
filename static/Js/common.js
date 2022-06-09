$(document).ready(function (e) {
  $(document).bind('contextmenu', function (e) {
    return false
  });
  try{
    $('[data-toggle="tooltip"]').tooltip();
  }
  catch(e){}
})
// document.onkeydown = function (e) {
//   if (
//     e.ctrlKey &&
//     (e.keyCode === 67 ||
//       e.keyCode === 88 ||
//       e.keyCode === 85 ||
//       e.keyCode === 73 ||
//       e.keyCode === 83 ||
//       e.keyCode === 117)
//   ) {
//     return false
//   } else {
//     if (e.keyCode === 123) {
//       return false
//     } else {
//       return true
//     }
//   }
// }

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
