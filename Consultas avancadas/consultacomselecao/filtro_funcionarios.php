<?php
// Informações de conexão com o banco de dados
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "empresa";

// Criar conexão
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar a conexão
if ($conn->connect_error) {
    die("Conexão falhou: " . $conn->connect_error);
}

// Construir a consulta SQL dinamicamente com base nos filtros selecionados
$sql = "SELECT nome, departamento, salario, data_admissao FROM funcionarios WHERE 1=1";

// Filtro por departamento
if (isset($_POST['departamento'])) {
    $departamentos = implode("','", $_POST['departamento']);
    $sql .= " AND departamento IN ('$departamentos')";
}

// Filtro por salário
if (!empty($_POST['salario'])) {
    $salario = $_POST['salario'];
    $sql .= " AND salario > $salario";
}

// Filtro por data de admissão
if (!empty($_POST['data_inicio']) && !empty($_POST['data_fim'])) {
    $data_inicio = $_POST['data_inicio'];
    $data_fim = $_POST['data_fim'];
    $sql .= " AND data_admissao BETWEEN '$data_inicio' AND '$data_fim'";
}

// Filtro por nome personalizado
if (!empty($_POST['nome'])) {
    $nome = $_POST['nome'];
    $sql .= " AND nome LIKE '$nome%'";
}

// Ordenar por salário em ordem decrescente
$sql .= " ORDER BY salario DESC";

// Executar a consulta
$result = $conn->query($sql);

// Exibir os resultados
if ($result->num_rows > 0) {
    echo "<table border='1'>
            <tr>
                <th>Nome</th>
                <th>Departamento</th>
                <th>Salário</th>
                <th>Data de Admissão</th>
            </tr>";

    // Loop através dos resultados
    while ($row = $result->fetch_assoc()) {
        echo "<tr>
                <td>" . $row['nome'] . "</td>
                <td>" . $row['departamento'] . "</td>
                <td>R$ " . number_format($row['salario'], 2, ',', '.') . "</td>
                <td>" . date("d/m/Y", strtotime($row['data_admissao'])) . "</td>
              </tr>";
    }

    echo "</table>";
} else {
    echo "Nenhum resultado encontrado.";
}

// Fechar a conexão
$conn->close();
?>
