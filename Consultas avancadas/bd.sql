-- Criação do banco de dados
CREATE DATABASE empresa;

-- Seleciona o banco de dados que será utilizado
USE empresa;

-- Criação da tabela 'funcionarios'
CREATE TABLE funcionarios (
    id INT PRIMARY KEY AUTO_INCREMENT, -- Chave primária e autoincremento
    nome VARCHAR(100), -- Nome do funcionário
    departamento VARCHAR(50), -- Departamento onde o funcionário trabalha
    salario DECIMAL(10, 2), -- Salário do funcionário com precisão de duas casas decimais
    data_admissao DATE -- Data de admissão do funcionário
);

-- Inserção dos dados na tabela 'funcionarios'
INSERT INTO funcionarios (nome, departamento, salario, data_admissao)
VALUES
('João Silva', 'TI', 55000.00, '2023-03-15'),
('Maria Costa', 'Financeiro', 45000.00, '2023-05-10'),
('José Almeida', 'Financeiro', 60000.00, '2023-10-01'),
('Júlia Souza', 'TI', 70000.00, '2023-07-18'),
('Carlos Mendes', 'RH', 48000.00, '2023-02-22'),
('Jessica Lima', 'TI', 53000.00, '2022-12-30');
