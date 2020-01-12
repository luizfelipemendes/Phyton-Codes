
print("Programa de Cadastro de Alunos\n")
opcao_entrada = (int(input("Você possui login de rede? Se sim, digite 1. Caso não, digite 2:")))
if opcao_entrada == 2:
    login_entra_cadas = (str(input("Digite seu email para cadastrar o login de entrada:")))
    senha_entra_cadas = (str(input("Digite uma senha de entrada para cadastro:")))
    print("Tabela de permissão de acesso\n")
    print("  1 -    Admin")
    print("  2 -    Recepção")
    print("  3 -    Cadastro")
    permissao = int(input("Digite o nível de permissão conforme tabela acima"))
else:
    opcao_entrada == 1
    login = (str(input("Digite seu login do sistema:\n")))
    senha = (str(input("Digite sua senha:\n")))
