import sqlite3

# Aqui conecta com o banco de dados - colocar o caminho da pasta
conexao2 = sqlite3.connect('c:/Users/livia/OneDrive/Área de Trabalho/banco_sqlite3/exe_BD')

# Criar um cursor
cursor = conexao2.cursor()

#Crie uma tabela chamada "alunos" com os seguintes campos: id
#(inteiro), nome (texto), idade (inteiro) e curso (texto).

cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

#2.Insira pelo menos 5 registros de alunos na tabela que você criou no
#exercício anterior.
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Pedro", 21, "Design")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Maria", 18, "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Cicero", 22, "Design")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Thais", 19, "Administração")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Beatriz", 23, "Enfermagem")')

cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(6, "João", 20, "Engenharia")')



#3.Consultas Básicas
#A) Selecionar toso os registros da tabela "alunos":
dados = cursor.execute('SELECT * FROM alunos')
for alunos in dados: 
 print(alunos)

#B.Selecionar todos os registros da tabela "alunos"
#dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
for alunos in dados: 
    print(alunos)

#C)Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
#dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome ASC')
for alunos in dados: 
    print(alunos)

#D)Contar o número total de alunos na tabela
dados = cursor.execute('SELECT COUNT(id) FROM alunos ')
for alunos in dados: 
    print(alunos)

#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade=24 WHERE nome ="Maria"')

#b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM alunos where id = 6')

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave
#primária), nome (texto), idade (inteiro) e saldo (float). 

cursor.execute('CREATE TABLE clientes(id INTEGER PRIMARY KEY, nome TEXT, idade INT, saldo FLOAT);')

#Insira algunsregistros de clientes na tabela.

cursor.execute('INSERT INTO clientes(id , nome, idade, saldo) VALUES(001, "José", 20, 114.50)')
cursor.execute('INSERT INTO clientes(id , nome, idade, saldo) VALUES(002, "Vanessa", 41, 300)')
cursor.execute('INSERT INTO clientes(id , nome, idade, saldo) VALUES(003, "Willian", 35, 1650.41)')
cursor.execute('INSERT INTO clientes(id , nome, idade, saldo) VALUES(004, "Renato", 30, 915.58)')
cursor.execute('INSERT INTO clientes(id , nome, idade, saldo) VALUES(005, "Messias", 29, 485.96)')
cursor.execute('INSERT INTO clientes(id , nome, idade, saldo) VALUES(006, "Mariana", 38, 188.49)')
cursor.execute('INSERT INTO clientes(id , nome, idade, saldo) VALUES(007, "Isabele", 45, 2500)')
cursor.execute('INSERT INTO clientes(id , nome, idade, saldo) VALUES(008, "Pedro", 50, 1367.88)')
cursor.execute('INSERT INTO clientes(id , nome, idade, saldo) VALUES(009, "Cristine", 25, 49.50)')
cursor.execute('INSERT INTO clientes(id , nome, idade, saldo) VALUES(010, "Leticia", 49, 19.90)')



#6. Consultas e Funções Agregadas
#a)Selecione  nome e a idade dos clientes com idade superior a 30 anos
cadastro = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
for clientes in cadastro: 
    print(clientes)

#b)Calcule o saldo médio do clientes
cadastro = cursor.execute('SELECT avg(saldo) as saldo_medio FROM clientes')
for clientes in cadastro: 
    print(clientes)

#c)Encntre o cliente com o saldo máximo
cadastro = cursor.execute('SELECT nome, max(saldo) as saldo_medio FROM clientes')
for clientes in cadastro: 
    print(clientes)


#d) Conte quantos clientes têm saldo acima de 1000.

cadastro = cursor.execute('SELECT count(nome) as qtd_clientes FROM clientes where saldo>1000')
for clientes in cadastro: 
    print(clientes)

#Atualize o saldo de um cliente específico
cursor.execute('UPDATE clientes SET saldo=3500 WHERE nome ="Leticia"')

#Remova um cliente pelo seu id
cursor.execute('DELETE FROM clientes where id = 6')

#Crie uma segunda tabela chamada compras com os campos: id(chave primaria), cliente_id(chave estrangeira)
#referenciando o id da tabelas clientes), produto(texto) e valor(real)
#cursor.execute('CREATE TABLE compras (id INTEGER PRIMARY KEY, cliente_id INTEGER, produto TEXT, valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes (id));')

cursor.execute('INSERT INTO compras(id , cliente_id, produto, valor) VALUES(202401, "1", "Cafeteira", 199.90)')
cursor.execute('INSERT INTO compras(id , cliente_id, produto, valor) VALUES(202402, "2", "Torradeira", 350)')
cursor.execute('INSERT INTO compras(id , cliente_id, produto, valor) VALUES(202403, "3", "TV LCD", 3000)')
cursor.execute('INSERT INTO compras(id , cliente_id, produto, valor) VALUES(202404, "4", "Lavadora a jato", 579.50)')
cursor.execute('INSERT INTO compras(id , cliente_id, produto, valor) VALUES(202405, "5", "Celular", 450)')
cursor.execute('INSERT INTO compras(id , cliente_id, produto, valor) VALUES(202406, "6", "Impressora", 685.90)')
cursor.execute('INSERT INTO compras(id , cliente_id, produto, valor) VALUES(202407, "7", "Cadeira de Praia", 199)')
cursor.execute('INSERT INTO compras(id , cliente_id, produto, valor) VALUES(202408, "8", "Caderno", 19.90)')
cursor.execute('INSERT INTO compras(id , cliente_id, produto, valor) VALUES(202409, "9", "Planta", 5.99)')
cursor.execute('INSERT INTO compras(id , cliente_id, produto, valor) VALUES(202410, "10", "Whey Protein", 430)')
cursor.execute('INSERT INTO compras(id , cliente_id, produto, valor) VALUES(202411, "11", "Tenis",850)')
cursor.execute('INSERT INTO compras(id , cliente_id, produto, valor) VALUES(202412, "12", "óculos de Sol", 259.94)')

#JOIN
cadastro_c = cursor.execute('SELECT a.nome, b.produto, b.valor  FROM clientes a INNER JOIN compras b ON a.id = b.cliente_id')
for compras in cadastro_c: 
    print(compras)

conexao2.commit()
conexao2.close()
