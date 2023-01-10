console.log("Hello Students")
let uname = document.getElementById("name");
let rno = document.getElementById("rno");
let sec = document.getElementById("sec");
let m1 = document.getElementById("m1");
let m2 = document.getElementById("m2");
let m3 = document.getElementById("m3");
let m4 = document.getElementById("m4");
let m5 = document.getElementById("m5");
let m6 = document.getElementById("m6");





function send_data(){
    let url = "http://127.0.0.1:8000/student";
    
    // console.log(data);
    let marks = [parseInt(m1.value),parseInt(m2.value),parseInt(m3.value),parseInt(m4.value),parseInt(m5.value),parseInt(m6.value)];
    
    
    // main.js

// POST request using fetch()
fetch(url, {
	
// Adding method type
method: "POST",

// Adding body or contents to send
body: JSON.stringify({
        name : uname.value,
        rno : rno.value,
        section:sec.value,
        marks : marks
}),

// Adding headers to the request
headers: {
    "Content-type": "application/json; charset=UTF-8"
}
})

// Converting to JSON
.then(response => response.json())

// Displaying results to console
.then(json => console.log(json));

}

function get_students(){
    let url = "http://127.0.0.1:8000/all";
    fetch(url)
.then(data => {
	console.log(data);
})
.catch(err => {
	// Catch and display errors
    console.log("error");
})

}