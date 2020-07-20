var cemail = document.getElementById('cemail');
var password= document.getElementById('password');

// storing input from register-form
function store() {
    localStorage.setItem('cemail', cemail.value);
    localStorage.setItem('password', password.value);
}

// check if stored data from register-form is equal to entered data in the   login-form
function check() {

    // stored data from the register-form
    var storedcemail = localStorage.getItem('cemail');
    var storedpassword = localStorage.getItem('password');

    // entered data from the login-form
    var userName = document.getElementById('userName');
    var userPw = document.getElementById('userPw');

    // check if stored data from register-form is equal to data from login form
  if(userName.value == storedcemail && userPw.value == storedpassword) {
        alert('You are loged in.');
    }else {s
        alert('ERROR.');
    }
}