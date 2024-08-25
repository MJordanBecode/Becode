<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>test PHP</title>
</head>

<body>
<?php 
    $name = 'Jordan';
    $age = 23;
    $eyes_color = 'brown';
    $family = array('moi','moi2');

    ?>
    <p>Bonjour, <?php echo $name; ?> !</p>
    <p>age :  <?php echo $age; ?> !</p>
    <p>eyes :  <?php echo $eyes_color; ?> !</p>
    <ul>
        <?php foreach ($family as $member) { ?>
            <li><?php echo $member; ?></li>
        <?php } ?>
    </ul>
    <?php

?>

       
</body>

</html>
