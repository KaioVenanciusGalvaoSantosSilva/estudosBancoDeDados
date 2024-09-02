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
    $email = $_POST['email'];
    $nome = $_POST['nome'];

    // Prepara a instrução SQL para evitar SQL Injection
    $stmt = $conn->prepare("UPDATE usuarios SET firstname = ? WHERE email = ?");
    $stmt->bind_param("ss", $nome, $email);

    // Executa a instrução SQL
    if ($stmt->execute()) {
        echo "Nome atualizado com sucesso!";
    } else {
        echo "Erro ao atualizar o nome: " . $conn->error;
    }

    // Fecha a declaração e a conexão
    $stmt->close();
    $conn->close();
}
?>