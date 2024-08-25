<<<<<<< HEAD
function factorial(a){
    if (a === 0) return 1
    let factorial = a * factorial(a - 1)
    return factorial;

}

let a = parseInt(prompt("Enter the number = " + "!"));
console.log(factorial(a));
=======
function factorial(a) {

        if(a === 0){ // verify if a is strictment equal at 0 
            return 1 ;  
        }
    console.log("Factorielle : "+ a + " !"); // display the factorial number, x, x2, x3... x^n
    return a * factorial(a - 1); // traitement 
    
}


let a = parseInt(prompt("Enter the factorial : " + " !")); // ask to user to choose a factorial 

console.log("Factorielle  : "+ factorial(a));
>>>>>>> 1f084b683c8266d0be87a8008e62f1645cf1529e
