<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
<h1>Veuillez saisir votre nom</h1>
    <form action="functions.php" method="post">
        <label for="name">Nom:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="name">Chiffre :</label>
        <input type="text" id="number" name="number" required>
        <br><br>
        <input type="submit" value="Envoyer">
    </form>
<?php

if(isset($_POST['name'])){
    $name = $_POST['name'];
}

// echo($name);
// $str = 'This is going to be shuffled !';
// $str = str_shuffle($str);
// echo $str;

//creation of functions : 

//function Capitalizes : 

function Capitalizes($name){ //fonctionne :)
    $capitalizes = ucfirst($name);
    // echo($capitalizes);

    return $capitalizes;
}

function dateTime(){

    $date_now = date('Y-m-d H:i:s');

    return $date_now;
}
echo("il est ".dateTime());

// echo("Le nom changé = ".Capitalizes($name));

function sum($a, $b){

    $sum = $a + $b;

    return $sum;
}

echo('<br>'.'resultat ='.sum(5,4));
/* Fonction à retravailler */
if (isset($_POST['number'])) {
    $number = $_POST['number'];}
function checkNumber($number) {
   
        
        // Vérifier si le numéro est un entier
        if (filter_var($number, FILTER_VALIDATE_INT) === false) {
            echo "Isn't a number, try again";
        } else {
            echo "It's a valid number";
        }
    
}

?>
</body>
</html>