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
                    <li><a href="home.php">Produtos</a></li>
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
            <h1>Sobre a Empresa</h1>
            
            <h2>Nossa História</h2>
            <p>A nossa empresa, Minha Loja, é uma loja online especializada em produtos de tecnologia e entretenimento. Fundada em 2015, nossa missão é fornecer aos nossos clientes os melhores produtos e serviços de alta qualidade, ao mesmo tempo em que oferecemos uma experiência de compra única e personalizada.</p>
            
            <h2>Nossa Missão</h2>
            <p>Nossa missão é ser a loja online mais confiável e respeitada do mercado, oferecendo aos nossos clientes uma experiência de compra segura, fácil e personalizada. Estamos comprometidos em fornecer os melhores produtos e serviços, ao mesmo tempo em que nos esforçamos para melhorar constantemente.</p>
            
            <h2>Nossa Equipe</h2>
            <p>Nossa equipe é formada por profissionais experientes e comprometidos, que trabalham arduamente para garantir que nossos clientes tenham a melhor experiência possível. Desde a seleção de produtos até a entrega, nossa equipe está sempre pronta para atender às necessidades dos nossos clientes.</p>
            
            <h2>Nossos Valores</h2>
            <p>Nossos valores são simples: qualidade, confiança, respeito e inovação. Estamos comprometidos em fornecer produtos e serviços de alta qualidade, ao mesmo tempo em que nos esforçamos para inovar e melhorar constantemente. Nossa equipe trabalha com respeito e dedicação para garantir que nossos clientes sejam satisfeitos.</p>
            <p><br><br><br><br><br><br><br></p>
    
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
