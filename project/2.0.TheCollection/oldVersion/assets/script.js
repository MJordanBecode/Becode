
document.body.style.backgroundColor = '#000000';












// image.appendChild(nouvelArticle);
// nouveauDiv.appendChild(nouvelArticle);







const Anime = [
{
    image : "./assets/images/86.jpg",
    AnimeName : "Heighty-Six",
    author : "Author : Toshimasa Ishii",
    episode : "episode : 23",
    film : "film : 0",
    release : "10 avril 2021",
},

{
    image : "./assets/images/bleach.jpg",
    AnimeName : "Bleach",
    author : "Author : Tite Kubo",
    episode : "episode : 366" ,
    film : "film : 4",
    release : "27 mars 2012",
},

{
    image : "./assets/images/clannadAfterStory.jpg",
    AnimeName : "Clannad After Story",
    author : "Author : Tatsuya Ishihara",
    episode : "episode : 22",
    film : "film : 0",
    release : "03 octobre 2008",
},

{
    image : "./assets/images/frieren.jpg",
    AnimeName : "Frieren",
    author : "Author : Kanehito Yamada",
    episode : "episode : 28",
    film : "film : 0",
    release :"29 septembre 2023" ,
},

{
    image : "./assets/images/guiltycrown.jpg",
    AnimeName : "Guilty Crow",
    author : "Author : Hiroyuki Yoshino",
    episode : "episode : 22",
    film : "film : 0",
    release : "13 octobre 2011",
},

{
    image : "./assets/images/jjk.jpg",
    AnimeName : "Jujutsu no kaise",
    author : "Author : Gege Akutami",
    episode : "episode : 47",
    film : "film : 1",
    release : "3 ocotobre 2020",
},

{
    image : "./assets/images/Kimetsu_no_Yaiba_Hashira_Geiko-hen.jpg",
    AnimeName : "Kimetsu no Yaiba",
    author : "Author : Koyoharu Gotouge",
    episode : "episode : 55",
    film : "film : 3",
    release : "2019",
},

{
    image : "./assets/images/sao.jpg",
    AnimeName : "Sword Art Online",
    author : "Author : Reki Kawahara",
    episode : "episode : 25",
    film : "film : 4",
    release : "7 juillet 2012",
},

{
    image : "./assets/images/Snk.jpg",
    AnimeName : "Shingeki no Kyojin",
    author : "Author : Hajime Isayama",
    episode : "episode : 94",
    film : "film : 4",
    release : "7 avril 2013",
},
{
    image : "./assets/images/VioletEvergarden.jpg",
    AnimeName : "Violet Evergarden",
    author : "Author : Kana Akatsuki ",
    episode : "episode : 13",
    film : "film : 1",
    release : "11 janvier 2018",
},
]

// Voir en off pour comprendre le système et y ajouter des class, id... 
// function createDiv(){
//     const newDiv = document.createElement('div');

//     return newDiv;
// }

function card(){
    for(let i = 0; i<Anime.length; i++){
        const nouvelArticle = document.createElement('article'); // Création d'un nouvel élément <article>
        nouvelArticle.setAttribute("class", "border-article");
        const NewTitle = document.createElement('h2'); // Création d'un nouvel élément <p>
        const image = document.createElement('img');
        const globalDiv = document.createElement('div');
        globalDiv.setAttribute("class", "container-div")
        const newDiv = document.createElement('div');
        newDiv.setAttribute("class", "div-img")
        const secondDiv = document.createElement('div');
        const thirdDiv = document.createElement('div');
        thirdDiv.setAttribute("class", "container-info");
        const newAuthor = document.createElement('p');
        const newEpisode = document.createElement('p');
        const newFilm = document.createElement('p');
        const newRelease = document.createElement('p');
        image.setAttribute("src", ""+Anime[i].image) ;
        image.setAttribute("class", "redim-img");


        
        nouvelArticle.appendChild(globalDiv);
        // globalDiv.appendChild();
        // globalDiv.appendChild();
        
        nouvelArticle.appendChild(newDiv);
        nouvelArticle.appendChild(NewTitle); // Ajout du paragraphe à l'article
        nouvelArticle.appendChild(secondDiv);
        secondDiv.appendChild(NewTitle);
        nouvelArticle.appendChild(newDiv);
        nouvelArticle.appendChild(image);
        newDiv.appendChild(image);
        nouvelArticle.appendChild(thirdDiv);
        thirdDiv.appendChild(newAuthor); 
        thirdDiv.appendChild(newEpisode); 
        thirdDiv.appendChild(newFilm);
        thirdDiv.appendChild(newRelease);
        nouvelArticle.appendChild(globalDiv);
        globalDiv.appendChild(secondDiv);
        globalDiv.appendChild(newDiv);
        globalDiv.appendChild(thirdDiv);
        
        

        for(let j = 0; j<Anime.length ;j++){

            NewTitle.textContent = (""+Anime[i].AnimeName);
            newAuthor.textContent = (""+Anime[i].author);
            newEpisode.textContent = (""+Anime[i].episode);
            newFilm.textContent = (""+Anime[i].film);
            newRelease.textContent = (""+Anime[i].release);
             
        }

        // for(let k = 0 ;k < Anime.length;k++){

        // }

        // for(let l = 0; l < Anime.length;l++){

        // }
        const mainElement = document.querySelector('main'); // Sélection de la balise <main> en utilisant querySelector


        mainElement.appendChild(nouvelArticle);// Ajout de l'article à la fin du main

    }
    
}

card();