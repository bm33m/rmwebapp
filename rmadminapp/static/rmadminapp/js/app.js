//
// app.js
// @author: Brian
//

var txtname = document.getElementById("txtname");
var surname = document.getElementById("surname");
var email = document.getElementById("email");
var phone = document.getElementById("phone");
var message = document.getElementById("message");
var umessage = "Please send us more details or update your profile.";
var tmpmesage = "";

function userInfo(uname, usurname, uemail, uphone){
  message.value = "";
  tmpmesage = "";
  txtname.value = uname;
  surname.value = usurname;
  email.value = uemail;
  phone.value = uphone;
  tmpmessage = "Hello "+uname+", \n\n"+umessage;
  message.value = tmpmessage;
}
