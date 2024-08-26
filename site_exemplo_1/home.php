<?php
session_start();

// Verifica se o usuário está logado
if (!isset($_SESSION['user_id'])) {
    // Redireciona para a página de login se não estiver logado
    header("Location: login.html");
    exit();
}
?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minha Loja</title>
    <link rel="stylesheet" href="css/style_home.css">
</head>
<body>
    <header>
        <div class="container">
            <h1><a href="home.php">Minha Loja</a></h1>
            <nav>
                <ul>
                    <li><a href="#">Produtos</a></li>
                    <li><a href="company.php">Sobre a Empresa</a></li>
                </ul>
            </nav>
            <div class="header-buttons">
                <span id="account">
                    <button onclick="toggleAccount()">Conta</button>
                    <div id="account-options" class="hidden">
                        <ul>
                            <li><a href="#">Minhas compras</a></li>
                            <li><a href="config.php">Configurações</a></li>
                            <li><a href="logout.php">Sair</a></li>
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
            <h2>Produtos</h2>
            <div id="product-list"></div>
        </div>
    </main>
    <script src="script.js"></script> 
</body>
<footer>
    <div class="container">
      <p>&copy; 2024 Minha Loja. Todos os direitos reservados.</p>
    </div>
  </footer>
</html>
