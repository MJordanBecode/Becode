class Rectangle{
    constructor(topLeftXPos,topLeftYPos, width, lenght){
        topLeftXPos = topLeftXPos;
        topLeftYPos = topLeftYPos;
        width = width;
        lenght = lenght;   
    }

    collides(otherRectangle) {
        // Check for collision along x-axis
        const xCollision = (this.topLeftXPos < otherRectangle.topLeftXPos + otherRectangle.width &&
                            this.topLeftXPos + this.width > otherRectangle.topLeftXPos);
        
        // Check for collision along y-axis
        const yCollision = (this.topLeftYPos < otherRectangle.topLeftYPos + otherRectangle.length &&
                            this.topLeftYPos + this.length > otherRectangle.topLeftYPos);
        
        // Return true if both x and y collisions occur
        return xCollision && yCollision;
    }
}
// Test cases
const rect1 = new Rectangle(0, 0, 4, 4);
const rect2 = new Rectangle(2, 5, 4, 4);
const rect3 = new Rectangle(5, 5, 2, 2);

console.log(rect1.collides(rect2)); // Should return true, as rect1 and rect2 overlap
console.log(rect1.collides(rect3)); // Should return false, as rect1 and rect3 do not overlap