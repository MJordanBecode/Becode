let mainElement = document.querySelector('main');
let buttonElement = document.querySelector("button");
console.log(buttonElement);

function printJsonFile() {
    buttonElement.addEventListener('click', event => {
        // console.log('test zebi');
 
        fetch('./human.json')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(json => {
                console.log("JSON content:", json);

                const selecUl = document.querySelector('ul');
                
                // Effacer le contenu précédent de la liste avant d'ajouter de nouveaux éléments
                selecUl.innerHTML = '';

                // Créer un nouvel élément li pour chaque élément du tableau JSON
                json.forEach(element => {
                    const li = document.createElement('li');
                    li.textContent = ""+ element.nom + " "+element.age;
                    selecUl.appendChild(li);
                });
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    });
}


printJsonFile();
