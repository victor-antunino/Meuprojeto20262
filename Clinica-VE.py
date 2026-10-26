# PROJETO CLINICA DE ODONTOLOGIA - VE.
adms = [["Victor", "12345", True]]
Pacientes = [["Enzo", "15338918420", "12345", "83998279055", "", "", False]]
Dentistas = [["D1", "Larissa", "123", "Ortodontia"],["D2", "Maria", "321", "Endodontia"],["D3", "Julia", "999", "Facetas"]]
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
        print("\n===== ACESSO DO PACIENTE =====")

        cpf_valido = False
        while cpf_valido == False:
            cpf = input("Informe seu CPF (ou digite 0 para voltar ao menu): ")

            if cpf == "0":
                break

            cpf_invalido = False
            for i in range(len(cpf)):
                if cpf[i] < "0" or cpf[i] > "9":
                    cpf_invalido = True
                    break

            if len(cpf) != 11 or cpf_invalido == True:
                print("CPF inválido! O CPF deve conter exatamente 11 dígitos numéricos. Tente novamente.")
            else:
                cpf_valido = True

        if cpf != "0":
            indice_paciente = -1
            for i in range(len(Pacientes)):
                if Pacientes[i][1] == cpf:
                    indice_paciente = i
                    break

            if indice_paciente != -1:
                senha = input("Informe sua senha: ")
                if Pacientes[indice_paciente][2] == senha:
                    CPF_paciente_logado = cpf
                    print("Bem-vindo(a),", Pacientes[indice_paciente][0] + "!")
                else:
                    print("Senha incorreta. Acesso negado.")

            else:
                print("CPF nao cadastrado.")
                cadastro = input("Deseja fazer autocadastro? Digite S para Sim ou N para Não: ").lower()

                if cadastro == "S" or "Sim":
                    nome = input("Digite seu nome: ")
                    senha = input("Crie uma senha: ")
                    telefone = input("Digite seu telefone: ")

                    if nome == "" or senha == "" or telefone == "":
                        print("Cadastro cancelado, todos os campos precisam ser preenchidos.")
                    else:
                        Pacientes.append([nome, cpf, senha, telefone, "", "", False])
                        CPF_paciente_logado = cpf
                        print("Cadastro realizado com sucesso! Bem-vindo(a),", nome + "!")

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
                    while True:
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
                                    break
                            if codigo == "":
                                print("O ID não pode ficar vazio.")
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
                                        break
                                if código == "" or nome == "" or cro == "" or Especialidade == "":
                                    print("Todos os campos devem ser preenchidos.")
                                elif cro_existe == True:
                                    print("Já existe um dentista com esse CRO.")
                                else:
                                    Dentistas.append([código, nome, cro, Especialidade ])
                                    print("\nDentistas cadastrados com sucesso!")

                        elif opção_dentista == "2":
                            if len(Dentistas) == 0:
                                print("Nunhum dentista cadastrado.")
                            else:
                                for dentista in Dentistas:
                                    print("\n ID:", dentista[0], "\n Nome:", dentista[1], "\n CRO:", dentista[2], "\n Especialidade:", dentista[3])

                        elif opção_dentista == "3":
                            codigo = input("Buscar pelo ID:")
                            indice = -1
                            for i in range(len(Dentistas)):
                                if Dentistas[i][0] == codigo:
                                    indice = i
                                    break
                            if indice == -1:
                                    print("Dentista não encontrado.")
                            else:
                                print("ID: ", Dentistas[indice][0])
                                print("Nome: ", Dentistas[indice][1])
                                print("CRO: ", Dentistas[indice][2])
                                print("Especialidade: ", Dentistas[indice][3])
                        
                        elif opção_dentista == "4":
                            codigo = input("ID do dentista para atualizar:" )
                            indice = -1
                            for i in range(len(Dentistas)):
                                if Dentistas [i][0] == codigo:
                                    indice = i
                                    break
                            if indice == -1:
                                print("Dentista não encontrado.")
                            else:
                                print("1 - Alterar nome:")
                                print("\n2 - Alterar CRO:")
                                print("\n3 - Alterar especialidade:")
                                campo = input("escolha uma opção:")

                                if campo == "1":
                                    novo = input("Novo nome: ")
                                    if novo != "":
                                        print("Nome não pode ficar vazio.")
                                    else:
                                        Dentistas[indice][1] = novo
                                        print("Nome Atualizado!")

                                elif campo == "2":
                                    novo = input("Novo CRO: ")
                                    existe = False
                                    for i in range(len(Dentistas)):
                                        if i != indice and Dentistas[i][2] == novo:
                                             existe == True
                                             break
                                    if novo == "" or existe == True:
                                        print("CRO vazio ou já cadastrado.")
                                    else:
                                        Dentistas[indice][2] == novo
                                        print("CRO atualizado.")
                                elif campo == "3":
                                    novo = input("Nova especialidade:")
                                    if novo != "":
                                        print("Especialidade não pode ficar vazia.")
                                    else:
                                        Dentistas[indice][3] = novo
                                        print("Especialidade atualizada!")
                                else:
                                    print("Opção invalida.")

                        elif opção_dentista == "5":
                            codigo = input("ID do dentista para remover:")
                            indice = -1
                            for i in range(len(Dentistas)):
                                if Dentistas[i][0] == codigo:
                                    indice = 1
                                    break
                            if indice == -1:
                                print("Dentista não encontrado.")
                            else:
                                tem_consulta = False
                                for consulta in Agendamentos:
                                    if consulta[1] == codigo:
                                        tem_consulta = True
                                        break
                                if tem_consulta == True:
                                    print("Não pode remover: o dentista possui consultas.")
                                else:
                                    confirmar = input("Confirmar remoção? (s/n):")
                                    if confirmar == "s" or confirmar == "S":
                                        Dentistas.pop(indice)
                                        for sala in Consultorios:
                                            for j in range(len(sala[1])):
                                                if sala[1][j] == codigo:
                                                    sala[1].pop(j)
                                                    break
                                        print("Dentista removido.")
                                    else:
                                        print("Remoção Cancelada.")

                        elif opção_dentista == "0":
                            break
                        else:
                            print("Opção Invalida.")

                if opção_adm == "2":
                       while True:
                        print("\n===== GESTÃO DE CONSULTORIOS =====")
                        print("1 - Cadastrar sala")
                        print("2 - Listar salas e dentistas vinculados")
                        print("3 - Vincular dentista a uma sala")
                        print("4 - Desvincular dentista de uma sala")
                        print("0 - Voltar")
                        opção_sala = input("escolha uma opção:")

                        if opção_sala == "1":
                            sala_nome = input("Nome da sala: ")
                            existe = False
                            for sala in Consultorios:
                                if sala[0] == sala_nome:
                                    existe = True
                                    break
                            if sala_nome == "" or existe == True:
                                print("Sala vazia ou ja castrada!.")
                            else:
                                Consultorios.append([sala_nome, []])
                                print("Sala cadastrada.")

                        elif opção_sala == "2":
                            if len(Consultorios) == 0:
                                print("Nenhuma sala cadastrada.")
                            else:
                                for sala in Consultorios:
                                    print("\nSala:",sala[0])
                                    if len (sala[1]) == 0:
                                        print("Nenhum dentista vinculado.")
                                    else:
                                        for codigo in sala[1]:
                                            nome_dentista = "não encotrado"
                                            for dentista in Dentistas:
                                                if dentista[0] == codigo:
                                                    nome_dentista = dentista[1]
                                                    break
                                            print("ID:", codigo, "\nNome:", nome_dentista)

                        elif opção_sala == "3":
                            sala_nome = input("Nome da sala: ")
                            indice_sala = -1
                            for i in range(len(Consultorios)):
                                if Consultorios[i][0] == sala_nome:
                                    indice_sala = i
                                    break
                            if indice_sala == -1:
                                    print("Sala não encontrada.")
                            else:
                                codigo = input("ID do dentista: ")
                                dentista_existe = False
                                for dentista in Dentistas:
                                    if dentista[0] == codigo:
                                        dentista_existe = True
                                        break
                                if dentista_existe == False:
                                    print("Dentista não encontrado.")
                                else:
                                    ja_vinculado = False
                                    for item in Consultorios[indice_sala][1]:
                                        if item == codigo:
                                            ja_vinculado = True
                                            break
                                    if ja_vinculado == True:
                                        print("Esse dentista ja esta vinculado a esta sala.")
                                    else:
                                        Consultorios[indice_sala][1].append(codigo)
                                        print("Dentista vinculado a sala!")
                                        
                        elif opção_sala == "4":
                            sala_nome = input("Nome da sala: ")
                            indice_sala = -1
                            for i in range(len(Consultorios)):
                                if Consultorios[i][0] == sala_nome:
                                    indice_sala = i
                                    break
                            if indice_sala == -1:
                                print("Sala não encontrada.")
                            else:
                                codigo = input("ID do dentista para desvincular:")
                                indice_vinculo = -1
                                for i in range(len(Consultorios[indice_sala][1])):
                                    if Consultorios[indice_sala][1][i] == codigo:
                                        indice_vinculo = i
                                        break
                                if indice_vinculo == -1:
                                    print("O dentista não esta vinculado a esta sala.")
                                else:
                                    Consultorios[indice_sala][1].pop(indice_vinculo)
                                    print("Vinculo removido.")

                        elif opção_sala == "0":
                            break
                        else:
                            print("Opção invalida")

                elif opção_adm == "3":
                    while True:
                        print("\n===== GESTÃO DE PACIENTES =====")
                        print("1 - Cadastrar paciente")
                        print("2 - Listar pacientes")
                        print("3 - Buscar por nome ou CPF")
                        print("4 - Atualizar paciente")
                        print("5 - Registrar observações / alergias")
                        print("6 - Remover pacientes")
                        print("0 - Voltar")
                        opção_cadastro = input("Escolha uma opção: ")

                        if opção_cadastro == "1":
                            nome = input("Nome:")
                            cpf = input("CPF (11 digitos): ")
                            senha = input("Senha: ")
                            telefone = input("Telefone: ")
                            for i in range(len(cpf)):
                                if cpf[i] < "0" or cpf[i] > "9":
                                    cpf_invalido = True
                                    break
                            existe = False
                            for paciente in Pacientes:
                                if paciente[1] == cpf:
                                    existe = True
                                    break
                            if nome == "" or senha == "" or telefone == "":
                                print(" Todos os campos devem ser preeenchidos.")
                            elif len(cpf) != 11 or cpf_invalido == True:
                                print(" CPF precisa ter exatamente 11 digitos numericos.")
                            elif existe == True:
                                print("Esse CPF já esta cadastrado.")
                            else:
                                Pacientes.append([nome, cpf, senha, telefone, "", "", False])
                                print("Paciente cadastrado!")