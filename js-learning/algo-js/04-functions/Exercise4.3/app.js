function rand10(a){ // ask to user to add a number at " a ". a = max of the random number. Default = 0, a = user number
    Math.floor(Math.random()*a)+1;
    return Math.random()*a;
}

function multiRand(n) {
    let array = [];
    for (let i = 0; i < n; i++) {
        array[i] = parseInt(rand10(a)+1); // Use the function rand 10 to generate random numbers between 1 and a 
    }
    return array; // Return the completed array with random numbers
}

let a = parseInt(prompt("Choose a number : ")); // ask the number of max random 


console.log("the random number = " + a);
console.log("There is your Array = "+ multiRand(a));

