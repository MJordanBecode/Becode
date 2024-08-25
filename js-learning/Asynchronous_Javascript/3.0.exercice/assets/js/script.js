let mainelement = document.querySelector('main'); //slec the main element on the page

let divContainer = document.createElement('div');
let divImg = document.createElement('div');
let divText = document.createElement('div');
let divQuote = document.createElement('div');
let divAuthor = document.createElement('div');

let quote = document.createElement('p');
let hAutor = document.createElement('h1');
let img = document.createElement('img');
let p = document.createElement('p');


divQuote.classList.add('divQuote');
divAuthor.classList.add('divAuthor');
divText.classList.add('divText');
divImg.classList.add('divImg');
divContainer.classList.add('divContainer');

divContainer.appendChild(divImg);
divContainer.appendChild(divAuthor);
divQuote.appendChild(quote);
divContainer.appendChild(divQuote);
divContainer.appendChild(divText);
divAuthor.appendChild(hAutor);
divText.appendChild(p);
divImg.appendChild(img);
mainelement.appendChild(divContainer);
let urlApi = 'https://thatsthespir.it/api';


fetch(urlApi)
    .then(response => {
        // Vérification si la réponse est OK
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // Récupération des données JSON à partir de la réponse
        return response.json();
    })
    .then(data => {
        // Utilisation des données JSON récupérées
        img.setAttribute("src",""+ data.photo);
        hAutor.innerText = '' + data.author;
        quote.innerText = '' + data.total_quotes;
        p.innerText = '' + data.quote;

        // data.quote
        // data.author
        // data.photo
        // data.total_quotes
    })
    .catch(error => {
        // Gestion des erreurs
        console.error('Erreur lors de la récupération des données:', error);
    });