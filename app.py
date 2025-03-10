import shutil
import datetime
import sqlite3
import os

# Caminho do banco no OneDrive
db_path = r"C:\Users\luiza.ribas\OneDrive - UNIVESP\Capivara Tech\capivara.db"

# Criar conexão com o SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Criar uma tabela de exemplo
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL
    )
''')

conn.commit()
conn.close()

def fazer_backup():
    # Caminho do banco e da pasta de backup
    db_origem = r"C:\Users\luiza.ribas\OneDrive - UNIVESP\Capivara Tech\capivara.db"
    pasta_backup = r"C:\Users\luiza.ribas\OneDrive - UNIVESP\Backup Capivara Tech"

    # Criar pasta de backup se não existir
    if not os.path.exists(pasta_backup):
        os.makedirs(pasta_backup)

    # Criar o nome do arquivo de backup com data e hora
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_destino = f"{pasta_backup}\\backup_{data_hora}.db"

    # Copiar o banco de dados para a pasta de backup
    shutil.copy(db_origem, backup_destino)
    print(f"Backup feito: {backup_destino}")

# Executar backup
fazer_backup()

# Dicionário com os usuários e seus níveis de acesso
usuarios = {
    "chefe1": {"senha": "capivara_de_chanel", "acesso": "total"},
    "chefe2": {"senha": "joaninha_cowboy", "acesso": "total"},
    "funcionario1": {"senha": "senhaa123", "acesso": "visualizar"},
    "joao123": {"senha": "joaninha_barbuda", "acesso": "total"},
}

def verificar_acesso(usuario, senha):
    if usuario in usuarios and usuarios[usuario]["senha"] == senha:
        return usuarios[usuario]["acesso"]
    else:
        return "negado"

# Teste de acesso
usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

nivel_acesso = verificar_acesso(usuario, senha)

if nivel_acesso == "total":
    print("Acesso total concedido! Você pode modificar os dados.")
elif nivel_acesso == "visualizar":
    print("Acesso restrito! Você pode apenas visualizar os dados.")
else:
    print("Acesso negado! Verifique seu usuário e senha.")

# Criar tabela de sugestões
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sugestoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        sugestao TEXT NOT NULL,
        data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()

def sugerir_alteracao(usuario, sugestao):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO sugestoes (usuario, sugestao) VALUES (?, ?)", (usuario, sugestao))
    conn.commit()
    conn.close()
    print("Sugestão enviada com sucesso!")

# Exemplo de uso
usuario = input("Seu nome: ")
sugestao = input("Digite sua sugestão: ")

sugerir_alteracao(usuario, sugestao)


