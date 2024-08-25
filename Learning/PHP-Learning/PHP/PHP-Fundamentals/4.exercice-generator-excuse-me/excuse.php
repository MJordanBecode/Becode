<!DOCTYPE html>
<html>

<head>
    <title>Excuse Generator</title>
</head>

<body>
    <h1>Excuse Note Generator</h1>
    <form method="post" action="">
        <label for="child_name">Name of the child:</label>
        <input type="text" id="child_name" name="child_name" required><br><br>

        <label for="gender">Gender of the child:</label>
        <input type="radio" id="boy" name="gender" value="boy" required>
        <label for="boy">Boy</label>
        <input type="radio" id="girl" name="gender" value="girl" required>
        <label for="girl">Girl</label><br><br>

        <label for="teacher_name">Name of the teacher:</label>
        <input type="text" id="teacher_name" name="teacher_name" required><br><br>

        <label for="reason">Reason for absence:</label><br>
        <input type="radio" id="illness" name="reason" value="illness" required>
        <label for="illness">Illness</label><br>
        <input type="radio" id="death_pet" name="reason" value="death_pet" required>
        <label for="death_pet">Death of a pet</label><br>
        <input type="radio" id="death_family" name="reason" value="death_family" required>
        <label for="death_family">Death of a family member</label><br>
        <input type="radio" id="activity" name="reason" value="activity" required>
        <label for="activity">Significant extra-curricular activity</label><br>
        <input type="radio" id="other" name="reason" value="other" required>
        <label for="other">Other</label><br><br>

        <button type="submit" name="generate">Generate Excuse Note</button>
    </form>

    <?php
    if(isset($_POST['child_name']) && isset($_POST['teacher_name']) && isset($_POST['reason']) && isset($_POST['gender'])){
        $child_name = $_POST['child_name'];
        $gender = $_POST['gender'];
        $teacher_name = $_POST['teacher_name'];
        $reason = $_POST['reason'];
    
        $pronoun = $gender == 'boy' ? 'He' : 'She';
        $note = "";

        switch ($reason) {
            case 'illness':
                $note = "$child_name was unable to attend school due to illness. $pronoun is now recovering and will be back in school shortly.";
                break;
            case 'death_pet':
                $note = "$child_name was absent from school due to the death of a beloved pet. $pronoun needed some time to cope with the loss.";
                break;
            case 'death_family':
                $note = "$child_name was unable to attend school due to the death of a family member. $pronoun needed time to be with the family during this difficult time.";
                break;
            case 'activity':
                $note = "$child_name was involved in a significant extra-curricular activity and could not attend school. $pronoun will make up for the missed work.";
                break;
            case 'other':
                $note = "$child_name was unable to attend school for personal reasons. Please feel free to contact me for more details.";
                break;
        }

        echo "<h2>Copy and Paste This Excuse Note</h2>";
        echo "<p>Dear $teacher_name,</p>";
        echo "<p>$note</p>";
        echo "<p>Thank you for your understanding.</p>";
        echo "<p>Sincerely,<br>Parent/Guardian</p>";
    }
    ?>
</body>

</html>