<?php
session_start();

// Destroi todas as variáveis de sessão
$_SESSION = [];

// Destroi a sessão
session_destroy();

// Redireciona para a página de login
header("Location: login.html");
exit();
?>
