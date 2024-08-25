<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<h1>Your Identity GIF</h1>
    <form action="" method="GET">
        <label for="identity">Are you a human, a cat, or a unicorn?</label>
        <select id="identity" name="identity" required>
            <option value="human">Human</option>
            <option value="cat">Cat</option>
            <option value="unicorn">Unicorn</option>
        </select><br><br>
        <input type="submit" value="Submit">
    </form>
    <?php 
    if (isset($_GET['identity'])) {
        $identity = $_GET['identity'];
        $gif = "";
        $message = "";

        switch ($identity) {
            case 'human':
                $gif = "https://giphy.com/embed/3oEjI6SIIHBdRxXI40";
                $message = "Hello, human!";
                break;
            case 'cat':
                $gif = "https://giphy.com/embed/JIX9t2j0ZTN9S";
                $message = "Meow, cat!";
                break;
            case 'unicorn':
                $gif = "https://giphy.com/embed/BpNdGqBuK7JkZpT3wN";
                $message = "Greetings, majestic unicorn!";
                break;
            default:
                $message = "Unknown identity.";
        }

        if ($gif) {
            echo "<h2>$message</h2>";
            echo '<iframe src="' . $gif . '" width="480" height="480" frameborder="0" class="giphy-embed" allowfullscreen></iframe>';
            echo '<p><a href="' . $gif . '">via GIPHY</a></p>';
        } else {
            echo "<p>$message</p>";
        }
    }
    ?>
    
</body>
</html>