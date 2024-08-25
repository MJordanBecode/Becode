<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ternary exercises</title>
</head>
<body>
<h1>Formulaire de Salutation</h1>
    <form action="ternary.php" method="POST">
        <label for="gender">Genre :</label>
        <select id="gender" name="gender" required>
            <option value="M">Masculin</option>
            <option value="F">Féminin</option>
        </select><br><br>
        <input type="submit" value="Soumettre">
    </form>

 
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['gender'])) {
        // Récupération de la valeur du genre
        $gender = $_POST['gender'];

            $hello = ($gender == "M") ? "Bonjour Monsieur!" : "Bonjour Madame!"; // si = vrai alors premier message 

        echo "<p>$hello</p>";
    }
    ?>

</body>
</html>