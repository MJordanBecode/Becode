let age: number = 20;
let text: string = "test";

if (age < 50) {
  age += 10;
}

console.log(age);

let sales: number = 123_456_789;
let course: string = "TypeScript";
let is_published: boolean = true;
let level;

// Any

function render(document: any) {
  console.log(document);
}

//Array

let user: [number, string, boolean, number] = [1, "Mosh", true, 0];

//const

const small = 1;
const medium = 2;
const large = 3;

const enum Size {
  Small = 1,
  Medium,
  Large,
}
let mySize: Size = Size.Medium;
console.log(mySize);

//functions

function calculateTax(income: number, taxYear=2022): number {
    if(taxYear< 2022)
    return income * 1.2;
  return income * 1.3;
}

calculateTax(10_000);


//objects 

let employee2 : {
    readonly id: number,
    name: string,
    retire:(date: Date) => void
} = {id: 1, 
    name:'Mosh',
    retire:(date: Date) => {
        console.log(date);
    }
}

    ; // ou {id: 1? name: 'Mosh};

    // Allias 

    type Employee = {
        readonly id: number,
        name: string,
        retire:(date: Date) => void
    }

    let employee: Employee = {
        id :1,
        name: 'Mosh',
        retire: (date: Date)=>{
            console.log(date);
        }
    }