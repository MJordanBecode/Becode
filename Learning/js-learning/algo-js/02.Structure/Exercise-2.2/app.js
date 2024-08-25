let minNbre=0 ; maxNbre=0; currentNbre=0;

minNbre=prompt("Choose a number ",minNbre);

maxNbre=prompt("Choose a number 2 : ",maxNbre);

currentNbre=prompt("Choose a number between 2 last : ",currentNbre);


if((currentNbre > maxNbre) || (currentNbre < minNbre)){
    alert("Error the Current isn't betwen "+minNbre+" and "+maxNbre);
} else{
    alert("Good job");
}


