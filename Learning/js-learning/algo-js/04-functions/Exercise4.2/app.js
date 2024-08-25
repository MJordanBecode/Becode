function rand10(a){ // ask to user to add a number at " a ". a = max of the random number. Default = 0, a = user number
    Math.floor(Math.random()*a);
    return Math.random()*a;
}

let a = prompt("Choose a number : "); // ask the number of max random 

console.log("Random number : "+ parseInt(rand10(a)));