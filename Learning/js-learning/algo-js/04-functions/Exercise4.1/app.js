function calcSurface(a,b){ // Surface of rectangle = L x l =>    a = lenght, b = width => a * b ;  
     return a * b;
}

let a = parseFloat (prompt("Enter the lenght of your rectangle : "));
console.log("c = "+a);
let b = parseFloat (prompt("Enter the width of your rectangle : "));
console.log("b = "+b);
alert("The surface of your rectangle = "+ calcSurface(a,b) +" m²");
