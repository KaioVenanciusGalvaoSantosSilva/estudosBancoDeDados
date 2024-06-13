<?php
// Verifica se os campos foram submetidos
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Credenciais de conexão com o banco de dados
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "mydatabase";

    // Estabelece a conexão com o banco de dados
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Verifica se houve erro na conexão
    if ($conn->connect_error) {
        die("Erro na conexão com o banco de dados: " . $conn->connect_error);
    }

    // Obtém os dados enviados via POST
    $email = $_POST["email"];
    $pass = $_POST["pass"];

    // Prepara a consulta SQL para obter as credenciais do usuário
    $sql = "SELECT pass FROM usuarios WHERE email = '$email'";
    $result = $conn->query($sql);

    // Verifica se a consulta retornou algum resultado
    if ($result->num_rows > 0) {
        // Obtém o hash da senha do banco de dados
        $row = $result->fetch_assoc();
        $pass_hash = $row["pass"];

        // Verifica se a senha fornecida pelo usuário corresponde ao hash armazenado
        if (password_verify($pass, $pass_hash)) {
            // Senha correta, redireciona para a página de sucesso
            $sql = "SELECT id,firstname,lastname,email,birthdate,gender FROM usuarios WHERE email = '$email'";
            $result = $conn->query($sql);
            $user = $result->fetch_assoc();

            session_start();
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['user_firstname'] = $user['firstname'];
            $_SESSION['user_lastname'] = $user['lastname'];
            $_SESSION['user_email'] = $user['email'];
            $_SESSION['user_birthdate'] = $user['birthdate'];
            $_SESSION['user_gender'] = $user['gender'];
            header("Location: home.html");
            exit();
        } else {
            // Senha incorreta, redireciona para a página de erro
            header("Location: erro.html");
            exit();
        }
    } else {
        // Usuário não encontrado, redireciona para a página de erro
        header("Location: erro.html");
        exit();
    }

    // Fecha a conexão com o banco de dados
    $conn->close();
    
}
?>
