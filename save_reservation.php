<?php
$host = "localhost";
$username = "root";
$password = "";
$database = "museum_db";

$conn = new mysqli($host, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $dayofvisit = $_POST['dayofvisit'];
    $country = $_POST['country'];
    $reservation_code = $_POST['reservation-code'];

    $hashed_code = password_hash($reservation_code, PASSWORD_DEFAULT);

    $sql = "INSERT INTO visitors (name, email, dayofvisit, country, reservation_code) 
            VALUES ('$name', '$email', '$dayofvisit', '$country', '$hashed_code')";

    if ($conn->query($sql) === TRUE) {
        echo "success";
    } else {
        echo "Error: " . $conn->error;
    }
}

$conn->close();
?>
