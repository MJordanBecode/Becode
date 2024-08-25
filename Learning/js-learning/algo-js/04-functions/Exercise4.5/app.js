function calcDistance(x1, y1, x2, y2){
    
     
     return Math.sqrt(Math.pow((x2 - x1), 2) + Math.pow((y2 - y1), 2));
}

let x1 = prompt("Enter the coordinate of x1 : ");
console.log(x1);
let y1 = prompt("Enter the coordinate of y1 : ");
console.log(y1);
let x2 = prompt("Enter the coordinate of x2 : ");
console.log(x2);
let y2 = prompt("Enter the coordinate of y2 : ");
console.log(y2);

console.log("Distance between point A and point B:" + calcDistance(x1, y1, x2, y2));
