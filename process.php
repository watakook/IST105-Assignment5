<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    $number = escapeshellarg($_POST["number"]);
    $text = escapeshellarg($_POST["text"]);

    $command = "python3 process.py $number $text";
    $output = shell_exec($command);

    echo "<h2>結果:</h2>";
    echo "<pre>$output</pre>";
}
?>