<?php
<?php
$servername = "localhost";
$servername = "localhost";
$database = "databasename";
$database = "databasename";
$username = "username";
$username = "username";
$password = "password";
$password = "password";
// Create connection
// Create connection
$conn = mysqli_connect($servername, $username, $password, $database);
$conn = mysqli_connect($servername, $username, $password, $database);
// Check connection
// Check connection
if (!$conn) {
if (!$conn) {
die("Connection failed: " . mysqli_connect_error());
    die("Connection failed: " . mysqli_connect_error());
}
}
echo "Connected successfully";
echo "Connected successfully";
mysqli_close($conn);
mysqli_close($conn);
?>
?>