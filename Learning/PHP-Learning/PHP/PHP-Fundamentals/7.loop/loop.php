<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!-- <?php
    // $names= array('john', 'jeanne', 'joan', 'émile');
    // foreach ($names as $name){
    //     echo ucfirst($name); // permet de mettre la première lettre du mot en maj 
    // }
    ?> -->


<?php

// $names= array('John', 'jeanne', 'Joan', 'émile');
// var_dump($names);

// foreach ($names as $key => $value){ // permet de savoir ou son stocker les données 
// 	$names[$key] = ucfirst($value);
// }
// var_dump($names);

?>

<?php 
//exercice : pronouns 

$pronouns = array ('I', 'You', 'He/She','We', 'You', 'They');


foreach($pronouns as $pronouns){
    echo($pronouns." code"."<br> \n");
}

$a = 0;
while($a <= 120){
    echo($a ."<br>");
    $a++;
}

// for($i = 0; $i <=120 ;$i++){
//     echo($i ."<br>");
// }
?>

<form action="#" method="post">
        <label for="country-select">Choose a country:</label>
        <select id="country-select" name="country">
            <option value="">--Please choose an option--</option>
            <?php
            // Associative array of countries
            $countries = array(
                "US" => "United States",
                "CA" => "Canada",
                "MX" => "Mexico",
                "UK" => "United Kingdom",
                "DE" => "Germany",
                "FR" => "France",
                "IT" => "Italy",
                "ES" => "Spain",
                "AU" => "Australia",
                "JP" => "Japan"
            );

            // Define the default selected country
            $selectedCountry = "US";

            // Loop through the countries array and create option elements
            foreach ($countries as $code => $country) {
                $selected = ($code == $selectedCountry) ? 'selected' : '';
                echo "<option value=\"$code\" $selected>$country</option>";
            }
            ?>
        </select>
    </form>
</body>
</html>