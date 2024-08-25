
// let Write = ['K','e','l','l','e','r']; // let write = 'keller'  =>  alternative for letter of write  => récupère chaque string 
// exercice 1 

let Write = 'keller';
let index = 0;




let mainElement = document.querySelector('main');
let divElement  = document.createElement('div');
let divH2 = document.createElement('h2');
let divElementTimer =  document.createElement('div');
let divH2Timer = document.createElement('h2');


divH2.textContent = "mot : ";


divElementTimer.appendChild(divH2Timer)
mainElement.appendChild(divElementTimer);
divElement.appendChild(divH2);
mainElement.appendChild(divElement);

function typeWriter() {

    if(index < Write.length){
        divH2.textContent += Write.charAt(index);
        index++;
    } else {

    }
    return divH2.textContent;

}


let typing = setInterval(typeWriter, 500);

let currentString = typeWriter();



//exercice 2 : 
function updateTimeElapsed() {
    var now = new Date();
    var secondsPassed = Math.floor((now - startTime) / 1000); // Calculate elapsed seconds
    var minutesPassed = Math.floor(secondsPassed / 60); // Calculate elapsed minutes

    if (secondsPassed < 60) {
        // Display seconds passed
        document.getElementById('timeElapsed').innerText = secondsPassed + " second(s) have passed";
    } else {
        // Display minutes passed
        document.getElementById('timeElapsed').innerText = minutesPassed + " minute(s) have passed";
    }
}

var startTime = new Date(); // Record the time when the page was opened
updateTimeElapsed(); // Display initial time elapsed

// Refresh the display every second
setInterval(updateTimeElapsed, 1000);

















window.addEventListener('load',OnPageLoad);

