<!-- #Código PHP + HTML para Exibir a Consulta: -->

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consulta de Funcionários</title>
    
    <!-- Estilos CSS para formatar a tabela -->
    <style>
        table {
            width: 100%; /* Tabela ocupa toda a largura da página */
            border-collapse: collapse; /* Remove espaços entre bordas das células */
            margin-top: 20px; /* Espaçamento superior */
        }
        th, td {
            padding: 10px; /* Espaçamento interno das células */
            border: 1px solid #ddd; /* Define borda fina ao redor das células */
            text-align: left; /* Alinhamento de texto à esquerda */
        }
        th {
            background-color: #f2f2f2; /* Cor de fundo para o cabeçalho */
        }
        tr:nth-child(even) {
            background-color: #f9f9f9; /* Cor de fundo para linhas pares */
        }
        tr:hover {
            background-color: #f1f1f1; /* Cor de fundo ao passar o mouse sobre a linha */
        }
    </style>
</head>
<body>

    <!-- Título da página -->
    <h1>Funcionários com Salário Acima de 50.000</h1>

    <?php
    // Informações de conexão ao banco de dados MySQL
    $servername = "localhost"; // Nome do servidor
    $username = "root"; // Usuário do banco de dados
    $password = ""; // Senha do banco de dados
    $dbname = "empresa"; // Nome do banco de dados

    // Criar conexão com o banco de dados MySQL
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Verificar se a conexão foi bem-sucedida
    if ($conn->connect_error) {
        die("Falha na conexão: " . $conn->connect_error); // Exibe mensagem de erro em caso de falha
    }

    // Consulta SQL para buscar os funcionários que atendem aos critérios
    $sql = "SELECT nome, departamento, salario, data_admissao
            FROM funcionarios
            WHERE salario > 50000
            AND departamento IN ('TI', 'Financeiro')
            AND data_admissao BETWEEN '2023-01-01' AND '2024-01-01'
            AND nome LIKE 'J%'
            ORDER BY salario DESC";

    // Executar a consulta SQL
    $result = $conn->query($sql);

    // Verificar se a consulta retornou resultados
    if ($result->num_rows > 0) {
        // Se houver resultados, exibe a tabela
        echo "<table>";
        echo "<thead><tr><th>Nome</th><th>Departamento</th><th>Salário</th><th>Data de Admissão</th></tr></thead>";
        echo "<tbody>";
        
        // Loop através dos resultados e exibe cada linha na tabela
        while($row = $result->fetch_assoc()) {
            echo "<tr>";
            echo "<td>" . $row["nome"] . "</td>"; // Exibe o nome do funcionário
            echo "<td>" . $row["departamento"] . "</td>"; // Exibe o departamento
            echo "<td>R$ " . number_format($row["salario"], 2, ',', '.') . "</td>"; // Exibe o salário formatado
            echo "<td>" . date("d/m/Y", strtotime($row["data_admissao"])) . "</td>"; // Exibe a data de admissão formatada
            echo "</tr>";
        }

        echo "</tbody></table>"; // Fecha a tabela
    } else {
        // Caso não haja resultados, exibe uma mensagem
        echo "Nenhum resultado encontrado.";
    }

    // Fechar a conexão com o banco de dados
    $conn->close();
    ?>

</body>
</html>
