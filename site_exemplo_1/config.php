<?php
session_start();
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Configuração da Conta</title>
    <link rel="stylesheet" href="css/style_home.css">
</head>
<body>
    <header>
        <div class="container">
            <h1><a href="home.html">Minha Loja</a></h1>
            <nav>
                <ul>
                    <li><a href="home.html">Produtos</a></li>
                    <li><a href="company.html">Sobre a Empresa</a></li>
                </ul>
            </nav>
            <div class="header-buttons">
                <span id="account">
                    <button onclick="toggleAccount()">Conta</button>
                    <div id="account-options" class="hidden">
                        <ul>
                            <li><a href="#">Minhas compras</a></li>
                            <li><a href="#">Configurações</a></li>
                            <li><a href="login.html">Sair</a></li>
                        </ul>
                    </div>
                </span>
                <span id="cart">
                    <button onclick="toggleCart()">Carrinho (<span id="cart-count">0</span>)</button>
                    <div id="cart-items" class="hidden">
                        <h2>Itens no Carrinho</h2>
                        <ul id="cart-list"></ul>
                        <button onclick="checkout()">Finalizar Compra</button>
                    </div>
                </span>
            </div>
        </div>
    </header>
    <main>
        <div class="container">
            <h2>Configuração da Conta</h2>
            <form id="configuracao-form" action="atualizar_usuario.php" method="post">
                <div class="form-group">
                    <label for="firstname">Nome:</label>
                    <input type="text" id="firstname" name="firstname" value="<?php echo $_SESSION['user_firstname']; ?>" required>
                </div>
                <div class="form-group">
                    <label for="lastname">Sobrenome:</label>
                    <input type="text" id="lastname" name="lastname" value="<?php echo $_SESSION['user_lastname']; ?>" required>
                </div>
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" value="<?php echo $_SESSION['user_email']; ?>" required>
                </div>
                <div class="form-group">
                    <label for="password">Senha:</label>
                    <input type="password" id="password" name="password">
                </div>
                <div class="form-group">
                    <label for="birthdate">Data de Nascimento:</label>
                    <input type="date" id="birthdate" name="birthdate" value="<?php echo $_SESSION['user_birthdate']; ?>" required>
                </div>
                <div class="form-group">
                    <label for="gender">Gênero:</label>
                    <select id="gender" name="gender" required>
                        <option value="male" <?php if($_SESSION['user_gender'] == 'male') echo 'selected'; ?>>Masculino</option>
                        <option value="female" <?php if($_SESSION['user_gender'] == 'female') echo 'selected'; ?>>Feminino</option>
                        <option value="other" <?php if($_SESSION['user_gender'] == 'other') echo 'selected'; ?>>Outro</option>
                    </select>
                </div>
                <div class="form-buttons">
                    <button type="submit">Salvar Dados</button>
                    <button type="button" onclick="deleteAccount()">Excluir Conta</button>
                </div>
            </form>
        </div>
    </main>
    <script src="script.js"></script>
</body>
<br><br><br><br>
<footer>
    <div class="container">
        <p>&copy; 2024 Minha Loja. Todos os direitos reservados.</p>
    </div>
</footer>
</html>
