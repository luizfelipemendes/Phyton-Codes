#Programa de Cadastro de Alunos - Universidade

#Cadastro usuário de login de cadastro

pinrt("BEM VINDO AO SISTEMA DE CADASTRO DOS ALUNOS DA SUA UNIVERSIDADE")


def funcap_login_cadas(opcao_entrada):

print("Programa de Cadastro de Alunos\n")
opcao_entrada = (int(input("Você possui login de rede? Se sim, digite 1. Caso não, digite 2:")))
if opcao_entrada == 2:
    login_entra_cadas = (str(input("Digite seu email para cadastrar o login de entrada:")))
    senha_entra_cadas = (str(input("Digite uma senha de entrada para cadastro:")))
    print("Tabela de permissão de acesso\n")
    print("  1 -    Admin")
    print("  2 -    Recepção")
    print("  3 -    Cadastro\n")
    permissao = int(input("Digite o nível de permissão conforme tabela acima"))
    a = open("usuarios.txt", "w")
    a.write("login: %s - senha: %s - permissao: %s - permissao: %s \n")
    a.close
    login = (str(input("Digite seu login do sistema:\n")))   #Login no sistema
    senha = (str(input("Digite sua senha:\n")))
else:
    opcao_entrada == 1
    login = (str(input("Digite seu login do sistema:\n")))
    senha = (str(input("Digite sua senha:\n")))


print("    MENU DE OPÇÔES\N")

print("   1 -  Para cadastro de um novo login\n")
print("   2 -  Para remover um  login\n")
print("   3 -  Para cadastro de um novo aluno\n")
print("   4 -  Para consultar um aluno\n")
print("   5 -  Para editar cadastro de um aluno\n")
print("   6 -  Para excluir um aluno\n")
print("   7 -  Para realizar o logout\n")

print("Digite a opção desejada:")

if opcao == 1:
    return ()
if opcao == 2:
    return(funcao_remv_aluno)
if opcao == 3:


#1 - Inserir de Aluno

print("Inclusão de aluno")

arq = ""
Nome = str(input("Digite o Nome: "))
Telefone = str(input("Digite o Telefone: "))
Endereço = str(input("Digite o seu endereço: "))
Idade = str(input("Digite a sua  Idade: "))
CPF = str(input("Digite o seu CPF: "))

arq = open("Lista de dados Clientes Hotel.txt", "w")

arq.write("Nome: %s - Telefone: %s - Endereço: %s - Idade: %s - CPF: %s\n"%(Nome, Telefone, Endereço, Idade, CPF))

arq.close

arq = file("Lista de dados Clientes Hotel.txt")
 
print ("\nLista de dados Clientes Hotel\n")

for Dados in arq:

        print(Dados)


#Função Buscar


def funcao_buscar(x):
    x = int(input("Digite o número do CPF do aluno"))
    arq = open("Lista de dados Clientes Hotel.txt", "r")
    aluno_busca = arq.readliness()
   for alunos in aluno_busca:
       return()

#2 - Remover aluno

def funcao_remv_aluno(x):
    x = int(input("Digite o número do CPF do aluno"))
    arq = open("Lista de dados Clientes Hotel.txt", "w")
    for x in arq:
        x = x.split("")
        print("Aluno removido com sucesso")
    







