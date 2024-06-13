<?php
// Credenciais do banco de dados
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "mydatabase";

// Criar conexão
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexão
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $token = $_POST['token'];
    $new_password = password_hash($_POST['new_password'], PASSWORD_DEFAULT);

    // Verificar o token e sua validade
    $sql = "SELECT id FROM usuarios WHERE reset_token = ? AND reset_token_expiration > NOW()";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $token);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        // Token válido, atualizar a senha
        $sql = "UPDATE usuarios SET pass = ?, reset_token = NULL, reset_token_expiration = NULL WHERE reset_token = ?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("ss", $new_password, $token);
        $stmt->execute();

        //echo "Senha redefinida com sucesso!";
        ?>
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Redefinir Senha</title>
            <link rel="stylesheet" type="text/css" href="css/style.css">
            <script>
                // Redireciona para o index.html após 10 segundos
                setTimeout(function(){
                    window.location.href = "login.html";
                }, 10000);
            </script>
        </head>
        <body>
            <div class="form-container">
                <h1>Parabéns!</h1>
                <p>Sua senha foi redefinida.</p>
                <p>Você será redirecionado para a página de login em 10 segundos.</p>
            </div>
        </body>
        </html>

        <?php


    } else {
        //echo "Token inválido ou expirado.";
        ?>
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Redefinir Senha</title>
            <link rel="stylesheet" type="text/css" href="css/style.css">
            <script>
                // Redireciona para o index.html após 10 segundos
                setTimeout(function(){
                    window.location.href = "login.html";
                }, 10000);
            </script>
        </head>
        <body>
            <div class="form-container">
                <h1>Solicitação recusada!</h1>
                <p>Token inválido ou expirado.</p>
                <p>Você será redirecionado para a página de redefinição de senha em 10 segundos.</p>
            </div>
        </body>
        </html>

        <?php

    }
} else if (isset($_GET['token'])) {
    $token = $_GET['token'];
    ?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Redefinir Senha</title>
        <link rel="stylesheet" type="text/css" href="css/style.css">
    </head>
    <body>
        <div class="form-container">
            <h2>Redefinir Senha</h2>
            <form action="reset_password.php" method="post">
                <input type="hidden" name="token" value="<?php echo htmlspecialchars($token); ?>">
                <label for="new_password">Nova Senha:</label>
                <input type="password" id="new_password" name="new_password" placeholder="Nova Senha" required>
                <input type="submit" value="Redefinir Senha">
            </form>
        </div>
    </body>
    </html>
    <?php
}

$conn->close();
?>
