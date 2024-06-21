import mysql.connector

# Classe Aluno
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

# Classe Turma
class Turma:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

# Classe SistemaEscolar para gerenciar interações com o banco de dados
class SistemaEscolar:
    def __init__(self):
        # Conexão com o banco de dados MySQL
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="he182555@",
            database="escola_db"
        )
        self.cursor = self.conexao.cursor()

    def adicionar_aluno(self, nome, matricula):
        # Cria um novo aluno
        aluno = Aluno(nome, matricula)
        query = "INSERT INTO alunos (nome, matricula) VALUES (%s, %s)"
        valores = (aluno.nome, aluno.matricula)
        self.cursor.execute(query, valores)
        self.conexao.commit()
        print(f"Aluno {aluno.nome} adicionado com sucesso!")

    def listar_turmas(self):
        # Lista todas as turmas disponíveis
        query = "SELECT id, nome FROM turmas"
        self.cursor.execute(query)
        turmas = self.cursor.fetchall()
        if not turmas:
            print("Nenhuma turma encontrada.")
        else:
            print("Turmas disponíveis:")
            for turma in turmas:
                print(f"{turma[0]}. {turma[1]}")

    def adicionar_turma(self, nome, professor):
        # Adiciona uma nova turma
        turma = Turma(nome, professor)
        query = "INSERT INTO turmas (nome, professor) VALUES (%s, %s)"
        valores = (turma.nome, turma.professor)
        self.cursor.execute(query, valores)
        self.conexao.commit()
        print(f"Turma {turma.nome} adicionada com sucesso!")

    def adicionar_aluno_turma(self, matricula_aluno, id_turma):
        # Adiciona um aluno a uma turma específica
        query = "INSERT INTO turma_aluno (turma_id, aluno_matricula) VALUES (%s, %s)"
        valores = (id_turma, matricula_aluno)
        self.cursor.execute(query, valores)
        self.conexao.commit()
        print(f"Aluno adicionado à turma com sucesso!")

    def menu_adicionar_aluno_turma(self):
        # Menu para adicionar um aluno a uma turma
        self.listar_turmas()
        id_turma = input("Digite o ID da turma à qual deseja adicionar o aluno: ")
        matricula_aluno = input("Digite a matrícula do aluno que deseja adicionar: ")
        self.adicionar_aluno_turma(matricula_aluno, id_turma)

    def fechar_conexao(self):
        # Fecha a conexão com o banco de dados
        self.cursor.close()
        self.conexao.close()

# Exemplo de uso do programa
if __name__ == "__main__":
    sistema_escolar = SistemaEscolar()

    # Exibindo menu para operações no sistema escolar
    while True:
        print("\n===== MENU =====")
        print("1. Adicionar aluno")
        print("2. Adicionar turma")
        print("3. Listar turmas")
        print("4. Adicionar aluno a uma turma")
        print("5. Sair do programa")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do aluno: ")
            matricula = input("Digite a matrícula do aluno: ")
            sistema_escolar.adicionar_aluno(nome, matricula)
        elif opcao == "2":
            nome_turma = input("Digite o nome da turma: ")
            professor = input("Digite o nome do professor: ")
            sistema_escolar.adicionar_turma(nome_turma, professor)
        elif opcao == "3":
            sistema_escolar.listar_turmas()
        elif opcao == "4":
            sistema_escolar.menu_adicionar_aluno_turma()
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

    sistema_escolar.fechar_conexao()
