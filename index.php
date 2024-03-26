<html>

<head>
    <title>RimWorld Art Generator</title>
</head>

<body>
    <?php
    // Execute the Python script and capture output
    $output = shell_exec("python app.py");

    // Check if there was any output or error
    if ($output !== null) {
        echo "<pre>$output</pre>";
    } else {
        echo "Error: Unable to execute Python script.";
    }
    ?>
</body>

</html>