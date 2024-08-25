<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    // 1.1 Clean your room Exercise 

    $room_is_filthy = false;

    // Définition de la fonction cleanup_room()
    function cleanup_room()
    {
        // Code pour nettoyer la chambre (peut être vide pour cet exemple)
        echo "Cleaning the room...";
    }

    if ($room_is_filthy) {
        echo "Yuk, Room is dirty : let's clean it up !<br>";
        cleanup_room(); // Appel de la fonction cleanup_room()
        echo "<br>Room is now clean!";
        $room_is_filthy = false;
    } else {
        echo "<br>Nothing to do, room is neat.";
    }
    ?>
    <br>
    <?php
    // 1.2 Clean your room Exercise, improved

    // Create the array of possible states
    $possible_states = ["health hazard", "filthy", "dirty", "clean", "immaculate"];

    // When testing, change the index value to navigate to the possible array values
    $room_filthiness = $possible_states[1];

    if ($room_filthiness == $possible_states[0]) {
        echo "Yuk, Room is Disgusting! Let's clean it up !";
    } else if ($room_filthiness == $possible_states[1]) {
        echo "Yuk, Room is dirty : let's clean it up !";
        // ...
    } else {
        echo "<br>Nothing to do, room is neat.";
    }

    ?>
    <br>
    <?php 
    // 2. "Different greetings according to time" Exercise

    $timestamp = time();
    $now = date("H:i:s", $timestamp);
    echo "L'heure (méthode date()) est : " . $now . "<br>";
    
    if("05:00:00" <= $now && $now < "09:00:00"){
        echo("Good morning ! ");
    } elseif("09:00:00" <= $now && $now < "12:00:00"){
        echo("Good day !");
    } elseif("12:00:00" <= $now && $now < "16:00:00"){
        echo("Good afternoon !");
    } else {
        echo("Good evening !");
    }  
    ?>
    <br>
    <?php 
// 3. "Different greetings according to age, gender and mothertongue" Exercise

if (isset($_GET['age']) && isset($_GET['gender']) && isset($_GET['english'])) {
    $age = (int)$_GET['age'];
    $gender = $_GET['gender'];
    $english = $_GET['english'];
    
    // Choisir la salutation en fonction de la langue
    $greeting = ($english == 'yes') ? 'Hello' : 'Aloha';

    if ($age < 12) {
        if ($gender == 'woman') {
            echo "$greeting Girl!";
        } else {
            echo "$greeting Boy!";
        }
    } elseif ($age >= 12 && $age < 18) {
        if ($gender == 'woman') {
            echo "$greeting Miss Teen!";
        } else {
            echo "$greeting Mister Teen!";
        }
    } elseif ($age >= 18 && $age < 115) {
        if ($gender == 'woman') {
            echo "$greeting Miss!";
        } else {
            echo "$greeting Mister!";
        }
    } elseif ($age >= 115) {
        if ($gender == 'woman') {
            echo "Wow! Still alive? Are you a robot, like me? Can I hug you, madam?";
        } else {
            echo "Wow! Still alive? Are you a robot, like me? Can I hug you, sir?";
        }
    }
}
?>



<form method="GET" action="#">
        <label for="age">Entrez votre âge :</label>
        <input type="number" name="age" id="age" required>
        <br>
        <label>Genre :</label>
        <input type="radio" name="gender" value="man" id="man" required>
        <label for="man">Homme</label>
        <input type="radio" name="gender" value="woman" id="woman" required>
        <label for="woman">Femme</label>
        <br>
        <label>Parlez-vous anglais ?</label>
        <input type="radio" name="english" value="yes" id="yes" required>
        <label for="yes">Oui</label>
        <input type="radio" name="english" value="no" id="no" required>
        <label for="no">Non</label>
        <br>
        <input type="submit" value="Envoyer">
    </form>

    <?php
// if (isset($_POST['name']) && isset($_POST['age']) && isset($_POST['gender'])) {
//     $name = $_POST['name'];
//     $age = $_POST['age'];
//     $gender = $_POST['gender'];

//     if ($age >= 21 && $age <= 40 && $gender == 'female') {
//         echo "Welcome to the team, $name!";
//     } else {
//         echo "Sorry, $name, you don't fit the criteria.";
//     }
// }
if (isset($_POST['name']) && isset($_POST['age']) && isset($_POST['gender'])) {
    $name = $_POST['name'];
    $age = $_POST['age'];
    $gender = $_POST['gender'];}

    $message = "Sorry, $name, you don't fit the criteria.";
    if ($age >= 21 && $age <= 40 && $gender == 'female') {
                $message =  "Welcome to the team, $name!";
            } 
                echo $message;
            
?>

    <h1>Register for the Girls' Soccer Team</h1>
    <form action="#" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="age">Age:</label>
        <input type="number" id="age2" name="age" required><br><br>
        
        <label for="gender">Gender:</label>
        <select id="gender" name="gender" required>
            <option value="female">Female</option>
            <option value="male">Male</option>
            <option value="other">Other</option>
        </select><br><br>
        
        <input type="submit" value="Submit">
    </form>

    <h1>Notation de l'élève</h1>
    <form action="#" method="POST">
        <label for="note">Note :</label>
        <input type="number" id="note" name="note" min="0" max="20" required><br><br>
        
        <input type="submit" value="Soumettre">
    </form>
    <?php
if (isset($_POST['note'])) {
    $note = intval($_POST['note']); // S'assurer que la note est un entier

    $Message2 = "Note invalide.";

    if ($note < 4) {
        $Message2 = "This work is really bad. What a dumb kid!";
    } elseif ($note >= 5 && $note <= 9) {
        $Message2 = "This is not sufficient. More studying is required.";
    } elseif ($note == 10) {
        $Message2 = "Barely enough!";
    } elseif ($note >= 11 && $note <= 14) {
        $Message2 = "Not bad!";
    } elseif ($note >= 15 && $note <= 18) {
        $Message2 = "Bravo, bravissimo!";
    } elseif ($note == 19 || $note == 20) {
        $Message2 = "Too good to be true: confront the cheater!";
    }

    echo $Message2;
}
?>

</body>

</html>