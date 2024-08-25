function askTvSerie() { // create the function "AskTvSerie" to ask to user differents param of a serie  
    let serie = { // create an object
        serie_name: "",
        production_year: "",
        actor: []
    };
  
    serie.serie_name = prompt("Enter the name of serie : "); //ask to user the name serie
    serie.production_year = prompt("Enter the production year : "); // ask to user the production year of the serie
  
    let ActorCount = parseInt(prompt("How much actor do you like?")); // ask to user how much actor.s to have the actor.lenght
  
    for (let i = 0; i < ActorCount; i++) {
        let actorName = prompt("Name of the Actor " + (i + 1) + " :"); // ask to user names of actors to add it in the array
        serie.actor.push(actorName);
    }
  
    console.log(serie);
    return serie;
  }
  let tvSerie = askTvSerie();
  
  console.log(JSON.stringify(tvSerie)); // change display at JSON format 
 