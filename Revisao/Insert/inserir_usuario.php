<?php
// Configurações do banco de dados
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "mydatabase";

// Conexão com o banco de dados
$conn = new mysqli($servername, $username, $password, $dbname);

// Verifica se a conexão foi bem-sucedida
if ($conn->connect_error) {
    die("Falha na conexão: " . $conn->connect_error);
}

// Verifica se o formulário foi submetido
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $firstname = $_POST['firstname'];
    $lastname = $_POST['lastname'];
    $email = $_POST['email'];
    $pass = password_hash($_POST['pass'], PASSWORD_BCRYPT);  // Hash da senha para maior segurança
    $birthdate = $_POST['birthdate'];
    $gender = $_POST['gender'];

    // Prepara a instrução SQL para evitar SQL Injection
    $stmt = $conn->prepare("INSERT INTO usuarios (firstname, lastname, email, pass, birthdate, gender) VALUES (?, ?, ?, ?, ?, ?)");
    $stmt->bind_param("ssssss", $firstname, $lastname, $email, $pass, $birthdate, $gender);

    // Executa a instrução SQL
    if ($stmt->execute()) {
        echo "Usuário cadastrado com sucesso! ID: " . $stmt->insert_id;
    } else {
        echo "Erro ao cadastrar usuário: " . $conn->error;
    }

    // Fecha a declaração e a conexão
    $stmt->close();
    $conn->close();
}
?>
