# PROJETO CLINICA DE ODONTOLOGIA - VE.
adms = [["Victor", "12345", True]]
Pacientes = [["Enzo", "15338918420", "12345", "83998279055", "", "", False]]
Dentistas = []
Consultorios = []
Agendamentos = []
adm_logado = False
CPF_paciente_logado = ""
ind1 = 0
ind2 = -1

# MENU PRINCIPAL

while True:
    print("\n========================================")
    print("      CLÍNICA ODONTOLOGIA — MENU      ")
    print("========================================")
    print("\n1 - Acessar como paciente")
    print("2 - Acessar como administrador")
    print("0 - Sair do sistema")

    opção = input("\nDigite qual opção deseja: ")

    if opção == "1":
        print("\nVocê está acessando como paciente.")
        cpf = input("\nDigite seu CPF: ")

        paciente_encontrado = -1

        for i in range(len(Pacientes)):
            if Pacientes[i][1] == cpf:
                paciente_encontrado = i
                break

        if paciente_encontrado == -1:
            print("\nCPF não foi encontrado. Vamos realizar seu cadastro!")
            nome = input("Fale seu nome: ")
            telefone = input("Digite seu telefone: ")
            senha = input("Crie uma senha: ")

            Pacientes.append([nome, cpf, senha, telefone, "", "", False])

            paciente_encontrado = len(Pacientes) - 1
            print("\nCadastro realizado com sucesso!")
            print(f"\nBem-vindo de volta, {Pacientes[paciente_encontrado][0]}!")

 # ============ acesso administrador ============       
    elif opção == "2":
        print("\n ======= LOGIN ADIMINISTRADOR =======")
        login = input("\nDigite seu login: ")
        senha = input("\nDigite sua senha: ")
        adm_logado = False

        for adm in adms:
            if adm[0] == login and adm[1] == senha:
                adm_logado = True
                break
        if adm_logado == False:
            print("\nLogin ou senha incorretos. Tente novamente.")
        else:
            print("\nBem-vindo ao menu do administrador!")
            while adm_logado == True:
                print("\n===== MENU ADMINISTRATIVO =====")
                print("1 - Gestão de dentistas")
                print("2 - Gestão de consultórios")
                print("3 - Gestão de pacientes")
                print("4 - Gestão geral")
                print("0 - Sair do menu administrativo")
                opção_adm = input("\nEscolha uma opção: ")

                if opção_adm == "1":
                    print("\n===== GESTÃO DE DENTISTAS =====")
                    print("1 - Cadastrar dentista")
                    print("2 - Listar dentistas")
                    print("3 - Buscar dentista por ID")
                    print("4 - Atualizar dentista")
                    print("5 - Excluir dentista")
                    print("0 - Voltar")
                    opção_dentista = input("\nEscolha uma opção: ")

                    if opção_dentista == "1":
                        código = input("ID do dentista: ")
                        existe = False
                        for dentista in Dentistas:
                            if dentista[0] == código:
                                existe = True
                        if existe == True:
                            print("Já existe um dentista com esse ID.")
                        else:
                            nome = input("Nome do dentista: ")
                            cro = input("CRO do dentista: ")
                            Especialidade = input("Especialidade do dentista: ")
                            cro_existe = False
                            for dentista in Dentistas:
                                if dentista[2] == cro:
                                    cro_existe = True
                            if cro_existe == True:
                                print("Já existe um dentista com esse CRO.")
                            elif código == "" or nome == "" or cro == "" or Especialidade == "":
                                print("Todos os campos devem ser preenchidos.")
                            else:
                                Dentistas.append([código, nome, cro, Especialidade ])
                                print("Dentistas cadastrados com sucesso!")

                    elif opção_dentista == "2":
                        if len(Dentistas) == 0:
                            print("Nunhum dentista cadastrado.")
                        else:
                            for dentista in Dentistas:
                                print("ID:", dentista[0], "| Nome:", dentista[1], "| CRO:", dentista[2], "| Especialidade:", dentista[3])
                                