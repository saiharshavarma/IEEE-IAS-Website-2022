const firebaseConfig = {
apiKey: "AIzaSyBkP6GOGzorF-7kYYTwxUWtxjfqTikEx7M",
authDomain: "ieee-ias-website.firebaseapp.com",
databaseURL: "https://automated-billing-management-default-rtdb.firebaseio.com/",
projectId: "ieee-ias-website",
storageBucket: "ieee-ias-website.appspot.com",
messagingSenderId: "934099392871",
appId: "1:934099392871:web:88cc27ad1a7d04b71cb7c2",
measurementId: "${config.measurementId}"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();


// Listen for form submit

var messageRef = firebase.database().ref('messages');

document.getElementById("contactForm").addEventListener('submit', submitForm);


//Submit Form
function submitForm(e) {
    e.preventDefault();

    // Get values
    var fname = getInputVal("fname-5a14");
    var lname = getInputVal("lname-5a14");
    var name = fname + ' ' + lname;
    var mobile_number = getInputVal("mobile-5a14");
    var email = getInputVal("email-5a14");
    var message = getInputVal("message-5a14");

    saveMessage(name, email, mobile_number, message);

    // show alert
    document.querySelector('.alert').style.display = 'block';

    

    // Hide after 3 sec
    setTimeout(function(){
        document.querySelector('.alert').style.display = 'none';
    }, 2000);

    document.getElementById('contactForm').reset();
}

// Function to get Form values

function getInputVal(id) {
    return document.getElementById(id).value;
}

// Save messages

function saveMessage(name, email, mobile_number, message){
    var newmessageRef = messageRef.push();
    newmessageRef.set({
        name: name,
        email: email,
        mobile_number: mobile_number,
        message: message
    });
}

//Authentication