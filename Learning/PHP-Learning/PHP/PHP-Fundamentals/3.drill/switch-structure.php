<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<h1>Notation de l'élève</h1>
    <form action="#" method="POST">
        <label for="note">Note :</label>
        <input type="number" id="note" name="note" min="0" max="20" required><br><br>
        
        <input type="submit" value="Soumettre">
    </form>
    <?php
if (isset($_POST['note'])) {
    $note = intval($_POST['note']); // S'assurer que la note est un entier

    $message = "Note invalide.";

    switch (true) {
        case ($note < 4):
            $message = "This work is really bad. What a dumb kid!";
            break;
        case ($note >= 5 && $note <= 9):
            $message = "This is not sufficient. More studying is required.";
            break;
        case ($note == 10):
            $message = "Barely enough!";
            break;
        case ($note >= 11 && $note <= 14):
            $message = "Not bad!";
            break;
        case ($note >= 15 && $note <= 18):
            $message = "Bravo, bravissimo!";
            break;
        case ($note == 19 || $note == 20):
            $message = "Too good to be true: confront the cheater!";
            break;
    }

    echo $message;
}
?>

</body>
</html>