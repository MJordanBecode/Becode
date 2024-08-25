class Circle {

  constructor(xPos, yPos, radius) {
    this.xPos = xPos;
    this.yPos = yPos;
    this.radius = radius;
  }

  move(xOffset, yOffset){
    this.xPos += xOffset; // Ajuster la position x
    this.yPos += yOffset; // Ajuster la position y
  }

  get surface() {
    return (((this.radius)*2)*  Math.PI); //calculer la surface
  }
}

// Demande à l'utilisateur de saisir le rayon 
let radius = parseInt(prompt("Enter the radius: "));
let circle = new Circle(0, 0, radius);

// Affiche la surface du cercle
console.log("Surface = " + circle.surface);
