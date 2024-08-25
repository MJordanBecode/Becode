function pickLearner(inputAr, n){
    if (n <= 0 || n > inputAr.length) {
        alert("number can't be < 0 and > lenght");

        return[]; //ne retourne rien
    }
    let SelectedLearners = [];
    let copyArray = inputAr.slice();

    for (let i = 0; i < n; i++) { // je me suis aidé de chat gpt parce que je ne voyais pas trop comment le faire (maintenant j'ai compris comment)
        let randomIndex = Math.floor(Math.random()* copyArray.length)
        SelectedLearners.push(copyArray[randomIndex]);
        copyArray.splice(randomIndex, 1);
    }

    return SelectedLearners;
}

const inputAr = ["Adrien.C", "Adrien.B", "Angel","Arnaud VA","Denis.L","Dylan","Dzheylyan","Giovanni","Isabelle","Jessica","Julie","Justine.F","Justine.L","Lyne","Jordan","Manu","Maryam","Mohamed","Nataliia","Bahra","Caroline","Dorian","Iliess","Louis","Nathanael","Tom","Youri","Stacy",];
let n = prompt("Choose your number : ");
console.log(inputAr);



let selectedLearners = pickLearner(inputAr, n); // n = number of Learners to print
console.log(selectedLearners);



// 

