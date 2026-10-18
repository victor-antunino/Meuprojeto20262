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
    print("      CLÍNICA ODONTOLÓGICA — MENU      ")
    print("========================================")
    print("\n1 - Acessar como paciente")
    print("2 - Acessar como administrador")
    print("0 - Sair do sistema")

    opcao = input("\nDigite qual opção deseja: ")

    if opcao == "1":
        CPF_paciente_logado = ""
        cpf = input("Informe seu CPF: ").strip()

        indice_paciente = -1
        for i in range(len(Pacientes)):
            if Pacientes[i][1] == cpf:
                indice_paciente = i
                break

        if cpf == "":
            print("O CPF nao pode ficar vazio.")

        elif indice_paciente != -1:
            senha = input("Informe sua senha: ")
            if Pacientes[indice_paciente][2] == senha:
                CPF_paciente_logado = cpf
                print("Bem-vindo(a),", Pacientes[indice_paciente][0] + "!")
            else:
                print("Senha incorreta. Acesso negado.")

        else:
            print("CPF nao cadastrado.")
            cadastro = input("Deseja fazer autocadastro? Digite S para sim ou N para não: ").lower()

            if cadastro == "s":
                nome = input("Nome: ").strip()
                senha = input("Crie uma senha: ")
                telefone = input("Telefone: ").strip()

                cpf_invalido = False
                for i in range(len(cpf)):
                    if cpf[i] < "0" or cpf[i] > "9":
                        cpf_invalido = True
                        break

                if nome == "" or senha == "" or telefone == "":
                    print("Cadastro cancelado: preencha todos os campos.")
                elif len(cpf) != 11 or cpf_invalido == True:
                    print("Cadastro cancelado: o CPF deve ter 11 digitos.")
                else:
                    Pacientes.append([nome, cpf, senha, telefone, "", "", False])
                    CPF_paciente_logado = cpf
                    print("Cadastro realizado! Bem-vindo(a),", nome + "!")

 # ============ acesso administrador ============       
    elif opcao == "2":
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
                                