<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Excuse</title>
</head>
<body>
<h1>Absence Form</h1>
<!--  -->
    <form action="excuse.php" method="post">
        <label for="child-name">Name of the child:</label><br>
        <input type="text" id="child-name" name="child-name" required><br><br> <!-- child-name -->

        <label for="gender">Gender of the child:</label><br>
        <input type="radio" id="girl" name="gender" value="girl" required><!-- gender -->
        <label for="girl">Girl</label><br>
        <input type="radio" id="boy" name="gender" value="boy" required><!-- gender -->
        <label for="boy">Boy</label><br><br>

        <label for="teacher-name">Name of the teacher:</label><br>
        <input type="text" id="teacher-name" name="teacher-name" required><br><br><!-- teacher-name -->

        <label for="reason">Reason for the absence:</label><br>
        <input type="radio" id="illness" name="reason" value="illness" required><!-- reason -->
        <label for="illness">Illness</label><br>
        <input type="radio" id="death" name="reason" value="death" required><!--reason-->
        <label for="death">Death of a pet or family member</label><br>
        <input type="radio" id="activity" name="reason" value="activity" required><!-- reason -->
        <label for="activity">Significant extra-curricular activity</label><br>
        <input type="radio" id="other" name="reason" value="other" required><!-- reason -->
        <label for="other">Any other excuse of your choice</label><br><br>

        <input type="submit" value="Submit">
    </form>

    <?php 
    if(isset($_GET['gender']) && isset($_GET['teacher-name']) && isset($_GET['reason']) && $_GET['child-name']){ // on vérifie si tous les éléments sont vides 
        $gender = $_GET['gender'];
        $reason = $_GET['reason'];
        $teacherName = $_GET['teacher-name'];
        $childName = $_GET['child-name'];
    }
    
   
        echo($childName);
    


    ?>
</body>
</html>