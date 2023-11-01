var username = "ashish123", password = "1234";
let current = document.getElementById("loginpage");
function login() {
    let u = document.getElementById("UN").value;
    let p = document.getElementById("PW").value;
    if (u == username && p == password) {
        current.style.display = "none";
        current = document.getElementById("loginSpage");
        current.style.display = "flex";
    }
    else{
        alert("Entered Username or Password is incorrect.");
    }
}
function register() {
    current.style.display = "none";
    current = document.getElementById("signUpPage");
    current.style.display = "flex";
    document.getElementById("FN").value="";
    document.getElementById("LN").value="";
    document.getElementById("email").value="";
    document.getElementById("userN").value="";
    document.getElementById("passW").value="";
}
function loginpage() {
    current.style.display = "none";
    current = document.getElementById("loginpage");
    current.style.display = "flex";
    document.getElementById("UN").value = "";
    document.getElementById("PW").value = "";
}
function forgetpassword() {
    current.style.display = "none";
    current = document.getElementById("forgetPpage");
    current.style.display = "flex";
    document.getElementById("newpw").value="";
    document.getElementById("reEnterpw").value="";
}
function newpassword() {
    let newPW = document.getElementById("newpw").value;
    let reEPW = document.getElementById("reEnterpw").value;
    if(newPW.length<4)
    {
        alert("Minimun length of password should be 4.");
    }
    else if (newPW == reEPW) {
        password = newPW;
        loginpage();
    }
    else{
        alert("Re-entered password is incorret.");
    }
}
function submitData() {
    let f = document.getElementById("FN").value;
    let l = document.getElementById("LN").value;
    let e = document.getElementById("email").value;
    let u = document.getElementById("userN").value;
    let p = document.getElementById("passW").value;
    if (f != "" && l != "" && e != "" && u != "" && p != "") {
        if(p.length>=4){
            username = u;
            password = p;
            loginpage();
        }
        else{
            alert("Minimun length of password should be 4.");
        }
    }
    else{
        alert("Fill all the Entries.");
    }
}