<?php

$host = 'localhost';
$db = 'museum_db';
$user = 'root';
$password = '';


$conn = new mysqli($host, $user, $password, $db);


if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


$name = $_POST['name'];
$reservation = $_POST['reservation'];


$sql = "INSERT INTO winner (name, reservation) VALUES (?, ?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ss", $name, $reservation);


if ($stmt->execute()) {
    echo "<h1>Thank you, $name!</h1><p>Thank you</p>";
} else {
    echo "<h1>Error!</h1><p>Could not save your details. Please try again later.</p>";
}


$stmt->close();
$conn->close();
?>
