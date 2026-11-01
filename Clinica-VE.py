# PROJETO CLINICA DE ODONTOLOGIA - VE.
adms = [["Victor", "12345", True]]
Dentistas = [["D1", "Larissa", "123", "Ortodontia"], ["D2", "Maria", "321", "Endodontia"], ["D3", "Julia", "999", "Facetas"]]
Pacientes = []
Consultorios = []
Agendamentos = []
consulta_agendadas = []
consultas_canceladas = []
adm_logado = False
CPF_paciente_logado = ""
ind = -1

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
            cpf = input("\nInforme seu CPF ou digite 0 para voltar ao menu: ")
            if cpf == "0":
                break

            cpf_invalido = False
            for i in range(len(cpf)):
                if cpf[i] < "0" or cpf[i] > "9":
                    cpf_invalido = True
                    break

            if len(cpf) != 11 or cpf_invalido == True:
                print("CPF inválido, ele deve ter 11 dígitos, digite novamente.")
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
                print("\nCPF nao cadastrado.")
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
                        print("Cadastro realizado com sucesso, bem vindo(a),", nome)

            while CPF_paciente_logado != "":
                print("\n--- Menu do Paciente ---")
                print("1 - Ver o corpo clínico")
                print("2 - Agendar sua consulta")
                print("3 - Visualizar minhas consultas")
                print("4 - Cancelar consulta")
                print("0 - Voltar para o menu principal")

                opcao_paciente = input("\nEscolha uma opção: ")

                if opcao_paciente == "1":
                    print("\n--- CORPO CLÍNICO ---")
                    if len(Dentistas) == 0:
                        print("Nenhum dentista cadastrado no momento.")
                    else:
                        for d in range(len(Dentistas)):
                            print("ID:", Dentistas[d][0], "| Nome:", Dentistas[d][1], "| CRO:", Dentistas[d][2], "| Especialidade:", Dentistas[d][3])

                elif opcao_paciente == "2":
                    print("\n--- Agendar Consulta ---")
                    if len(Dentistas) == 0:
                        print("Nao ha dentistas cadastrados.")
                    else:
                        print("Temos dentistas disponiveis")
                        for d in range(len(Dentistas)):
                            print("ID:", Dentistas[d][0], "| Nome:", Dentistas[d][1], "| Especialidade:",Dentistas[d][3])
                        id_dentista = input("\nDigite o ID do dentista desejado: ")
                        # criei essa variavel para ser aquela que vai saber se o tal do dentista existe ou não
                        dentista_existe =False
                        for d in range(len(Dentistas)):
                            if Dentistas [d][0] == id_dentista:
                                dentista_existe = True
                                break

                        if dentista_existe == False:
                            print("Não foi possível localizar o dentista")
                        else:
                            data_consulta = input("Informe a data da consulta (Dia/Mês/Ano): ")
                            horario_consulta = input("Informe o horário da consulta (00:00): ")
                            if data_consulta == "" or horario_consulta == "":
                                print("Data e horario nao podem ficar sem nada")
                            else:
                                horario_paia = False
                                for c in range(len(consulta_agendadas)):
                                    if consulta_agendadas[c][1] == id_dentista and consulta_agendadas[c][2] == data_consulta and consulta_agendadas[c][3] == horario_consulta:
                                        horario_paia = True
                                        break

                                if horario_paia == True:
                                    print("Infelizmente você terá que remarcar sua consulta, esse dentista está com uma consulta marcada para esse dia e horário")
                                else:
                                    consulta_agendadas.append([CPF_paciente_logado, id_dentista, data_consulta, horario_consulta])
                                    print("Consulta agendada com sucesso")

                elif opcao_paciente == "3":
                    print("\n--- Minhas Consultas ---")
                    tem_consulta = False
                    for c in range(len(consulta_agendadas)):
                        if consulta_agendadas[c][0] == CPF_paciente_logado:
                            tem_consulta = True
                            print("Dentista ID: ", consulta_agendadas[c][1], "| Data: ", consulta_agendadas[c][2], "| Horário: ", consulta_agendadas[c][3])
                    if  tem_consulta == False:
                        print("Você não tem consultas agendadas")

                elif opcao_paciente == "4":
                    print("\n--- Cancelar Consulta ---")
                    data_cancelar = input("Digite a data da consulta para cancelar: ")
                    horario_cancelar = input("Digite o horário da consulta para cancelar: ")

                    for c in range(len(consulta_agendadas)):
                        if consulta_agendadas[c][0] == CPF_paciente_logado and consulta_agendadas[c][2] == data_cancelar and consulta_agendadas[c][3] == horario_cancelar:
                            ind = c
                            break

                    if ind == -1: #Cria uma variável de controle com o valor -1. Assume-se inicialmente que a consulta ainda não foi encontrada.
                        print("\nNenhuma consulta foi encontrada.")
                    else:
                        for c in range(len(consulta_agendadas)):
                            if c != ind:
                                consultas_canceladas.append(consulta_agendadas[c])
                        consulta_agendadas = consultas_canceladas
                        print("\nConsulta cancelada com sucesso!")

                elif opcao_paciente == "0":
                    print("\nVocê irá sair daqui")
                    CPF_paciente_logado = ""
                    break
                else:
                    print("Opção inválida amigo, escolha uma opção entre 0 e 4.")

 # ============ acesso administrador ============    
    
    elif opcao == "2":
        print("\n ======= LOGIN ADIMINISTRADOR =======")
        login = input("\nDigite seu login: ")
        senha = input("Digite sua senha: ")
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
                opcao_adm = input("\nEscolha uma opção: ")

                if opcao_adm == "1":
                    while True:
                        print("\n===== GESTÃO DE DENTISTAS =====")
                        print("1 - Cadastrar dentista")
                        print("2 - Listar dentistas")
                        print("3 - Buscar dentista por ID")
                        print("4 - Atualizar dentista")
                        print("5 - Excluir dentista")
                        print("0 - Voltar")
                        opcao_dentista = input("\nEscolha uma opção: ")

                        if opcao_dentista == "1":
                            codigo = input("ID do dentista: ")
                            existe = False
                            for dentista in Dentistas:
                                if dentista[0].lower() == codigo.lower():
                                    existe = True
                                    break
                            if codigo == "":
                                print("O ID não pode ficar vazio.")
                            elif existe == True:
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
                                if codigo == "" or nome == "" or cro == "" or Especialidade == "":
                                    print("Todos os campos devem ser preenchidos.")
                                elif cro_existe == True:
                                    print("Já existe um dentista com esse CRO.")
                                else:
                                    Dentistas.append([codigo, nome, cro, Especialidade ])
                                    print("\nDentista cadastrado com sucesso!")

                        elif opcao_dentista == "2":
                            if len(Dentistas) == 0:
                                print("Nunhum dentista cadastrado.")
                            else:
                                for dentista in Dentistas:
                                    print("\n ID:", dentista[0], "\n Nome:", dentista[1], "\n CRO:", dentista[2], "\n Especialidade:", dentista[3])

                        elif opcao_dentista == "3":
                            codigo = input("Buscar pelo ID:")
                            indice = -1
                            for i in range(len(Dentistas)):
                                if Dentistas[i][0].lower() == codigo.lower():
                                    indice = i
                                    break
                            if indice == -1:
                                    print("Dentista não encontrado.")
                            else:
                                print("\nID: ", Dentistas[indice][0])
                                print("Nome: ", Dentistas[indice][1])
                                print("CRO: ", Dentistas[indice][2])
                                print("Especialidade: ", Dentistas[indice][3])
                        
                        elif opcao_dentista == "4":
                            codigo = input("ID do dentista para atualizar:" )
                            indice = -1
                            for i in range(len(Dentistas)):
                                if Dentistas [i][0].lower() == codigo.lower():
                                    indice = i
                                    break
                            if indice == -1:
                                print("Dentista não encontrado.")
                            else:
                                print("1 - Alterar nome")
                                print("\n2 - Alterar CRO")
                                print("\n3 - Alterar especialidade")
                                campo = input("escolha uma opção")

                                if campo == "1":
                                    novo = input("Novo nome: ")
                                    if novo == "":
                                        print("Nome não pode ficar vazio.")
                                    else:
                                        Dentistas[indice][1] = novo
                                        print("Nome Atualizado!")

                                elif campo == "2":
                                    novo = input("Novo CRO: ")
                                    existe = False
                                    for i in range(len(Dentistas)):
                                        if i != indice and Dentistas[i][2] == novo:
                                             existe = True
                                             break
                                    if novo == "" or existe == True:
                                        print("CRO vazio ou já cadastrado.")
                                    else:
                                        Dentistas[indice][2] = novo
                                        print("CRO atualizado.")
                                elif campo == "3":
                                    novo = input("Nova especialidade:")
                                    if novo == "":
                                        print("Especialidade não pode ficar vazia.")
                                    else:
                                        Dentistas[indice][3] = novo
                                        print("Especialidade atualizada!")
                                else:
                                    print("Opção invalida.")

                        elif opcao_dentista == "5":
                            codigo = input("ID do dentista para remover:")
                            indice = -1
                            for i in range(len(Dentistas)):
                                if Dentistas[i][0].lower() == codigo.lower():
                                    indice = i
                                    break
                            if indice == -1:
                                print("Dentista não encontrado.")
                            else:
                                tem_consulta = False
                                for consulta in Agendamentos:
                                    if consulta[1].lower() == codigo.lower():
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
                                                if sala[1][j].lower() == codigo.lower():
                                                    sala[1].pop(j)
                                                    break
                                        print("Dentista removido.")
                                    else:
                                        print("Remoção Cancelada.")

                        elif opcao_dentista == "0":
                            break
                        else:
                            print("Opção Invalida.")

                elif opcao_adm == "2":
                       while True:
                        print("\n===== GESTÃO DE CONSULTORIOS =====")
                        print("1 - Cadastrar sala")
                        print("2 - Listar salas e dentistas vinculados")
                        print("3 - Vincular dentista a uma sala")
                        print("4 - Desvincular dentista de uma sala")
                        print("0 - Voltar")
                        opcao_sala = input("escolha uma opção:")

                        if opcao_sala == "1":
                            sala_nome = input("Nome da sala: ")
                            existe = False
                            for sala in Consultorios:
                                if sala[0].lower() == sala_nome.lower():
                                    existe = True
                                    break
                            if sala_nome == "" or existe == True:
                                print("Sala vazia ou ja castrada!.")
                            else:
                                Consultorios.append([sala_nome, []])
                                print("Sala cadastrada.")

                        elif opcao_sala == "2":
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

                        elif opcao_sala == "3":
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
                                    if dentista[0].lower() == codigo.lower():
                                        dentista_existe = True
                                        codigo = dentista[0]
                                        break
                                if dentista_existe == False:
                                    print("Dentista não encontrado.")
                                else:
                                    ja_vinculado = False
                                    for item in Consultorios[indice_sala][1]:
                                        if item.lower() == codigo.lower():
                                            ja_vinculado = True
                                            break
                                    if ja_vinculado == True:
                                        print("Esse dentista ja esta vinculado a esta sala.")
                                    else:
                                        Consultorios[indice_sala][1].append(codigo)
                                        print("Dentista vinculado a sala!")
                                        
                        elif opcao_sala == "4":
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
                                    if Consultorios[indice_sala][1][i].lower() == codigo.lower():
                                        indice_vinculo = i
                                        break
                                if indice_vinculo == -1:
                                    print("O dentista não esta vinculado a esta sala.")
                                else:
                                    Consultorios[indice_sala][1].pop(indice_vinculo)
                                    print("Vinculo removido.")

                        elif opcao_sala == "0":
                            break
                        else:
                            print("Opção invalida")

                elif opcao_adm == "3":
                    while True:
                        print("\n===== GESTÃO DE PACIENTES =====")
                        print("1 - Cadastrar paciente")
                        print("2 - Listar pacientes")
                        print("3 - Buscar por nome ou CPF")
                        print("4 - Atualizar paciente")
                        print("5 - Registrar observações / alergias")
                        print("6 - Remover pacientes")
                        print("0 - Voltar")
                        opcao_cadastro = input("Escolha uma opção: ")

                        if opcao_cadastro == "1":
                            nome = input("Nome:")
                            cpf = input("CPF (11 digitos): ")
                            senha = input("Senha: ")
                            telefone = input("Telefone: ")
                            cpf_invalido = False
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

                        elif opcao_cadastro == "2":
                            if len(Pacientes) == 0:
                                print("Nenhum paciente cadastrado.")
                            else:
                                for paciente in Pacientes:
                                    print("\nNome: ", paciente[0])
                                    print("CPF: ", paciente[1])
                                    print("Telefone: ", paciente[3])
                                    print("Observações: ", paciente[4])
                                    print("Alergias: ", paciente[5])

                        elif opcao_cadastro == "3":
                            busca = input("Informe nome ou CPF: ")
                            encontrou = False
                            for paciente in Pacientes:
                                if paciente[0] == busca or paciente[1] == busca:
                                    encontrou = True
                                    print("\nNome: ", paciente[0]) 
                                    print("CPF: ", paciente[1])
                                    print("Telefone:", paciente[3])
                                    print("Observações: ", paciente[4])
                                    print("Alergias: ", paciente[5])
                            if encontrou == False:
                                print("Paciente não encontrado.")

                        elif opcao_cadastro == "4":
                            cpf = input("CPF do paciente para atualizar: ")
                            indice = -1
                            for i in range(len(Pacientes)):
                                if Pacientes[i][1] == cpf:
                                    indice = i
                                    break
                            if indice == -1:
                                print("Paciente não encontrado.")
                            else:
                                print("\n1 - Alterar nome")
                                print("2 - Alterar CPF")
                                print("3 - Alterar senha")
                                print("4 - Alterar telefone")
                                campo = input("Escolha uma opção:")
                                if campo == "1":
                                    novo = input("Novo nome: ")
                                    if novo == "":
                                        print("Nome vazio não é permitido.")
                                    else:
                                        Pacientes[indice][0] = novo
                                        print(" Nome atualizado!")
                                elif campo == "2":
                                    novo = input("Novo CPF: ")
                                    cpf_invalido = False
                                    for i in range(len(novo)):
                                        if novo[i] < "0" or novo[i] > "9":
                                            cpf_invalido = True
                                            break
                                    existe = False
                                    for i in range(len(Pacientes)):
                                        if i != indice and Pacientes[i][1] == novo:
                                            existe = True
                                            break
                                    if len(novo) != 11 or cpf_invalido == True or existe == True:
                                        print("CPF inavalido ou já cadastrado.")
                                    else:
                                        for consulta in Agendamentos:
                                            if consulta[0] == cpf:
                                                consulta[0] = novo
                                        Pacientes[indice][1] = novo
                                        print("CPF atualizado (atualizado nas consultas tambem).")

                                elif campo == "3":
                                    novo = input("Nova senha: ")
                                    if novo == "":
                                        print("Senha não pode ficar vazia.")
                                    else:
                                        Pacientes[indice][2] = novo
                                        print("Senha Atualizada!")

                                elif campo == "4":
                                    novo = input("Novo Telefone: ")
                                    if novo == "":
                                        print("Telefone não pode ficar vazio.")
                                    else:
                                        Pacientes[indice][3] = novo
                                        print("Telefone Atualizado!")
                                else:
                                    print("Opção Invalida.")

                        elif opcao_cadastro == "5":
                            cpf = input("CPF do paciente: ")
                            indice = -1
                            for i in range(len(Pacientes)):
                                if Pacientes[i][1] == cpf:
                                    indice = i
                                    break
                            if indice == -1:
                                print("Paciente não encontrado.")
                            else:
                                print("\n1- Observações")
                                print("2- Alergias")
                                campo = input("Escolha uma opção: ")
                                if campo == "1":
                                    novo = input("Nova Observação: ")
                                    Pacientes[indice][4] = novo
                                    print("Observação Atualizada!")
                                elif campo == "2":
                                    novo = input("Nova alergia: ")
                                    Pacientes[indice][5] = novo
                                    print("Alergia Atualizada!")
                                else:
                                    print("Opção invalida.")

                        elif opcao_cadastro == "6":
                            cpf = input("CPF do paciente para remover: ")
                            indice = -1
                            for i in range(len(Pacientes)):
                                if Pacientes[i][1] == cpf:
                                    indice = i
                                    break
                            if indice == -1:
                                print("Paciente não encontrado.")
                            else:
                                 tem_consulta = False
                                 for consulta in Agendamentos:
                                    if consulta[0] == cpf:
                                        tem_consulta = True
                                        break                             
                                 if tem_consulta == True:
                                    print("Não pode remover paciente com consultas marcadas.")
                                 else:
                                    confirmar = input("Confirmar remoção? (s/n): ")
                                    if confirmar == "s" or confirmar == "S":
                                        Pacientes.pop(indice)
                                        print("Paciente removido.")
                                    else:
                                        print("Remoção cancelada.")

                        elif opcao_cadastro == "0":
                            break
                        else:
                            print("Opção invalida.")

                elif opcao_adm == "4":
                    while True:
                        print("\n===== AGENDA GERAL =====")
                        print("1 - Vizualizar todas as consultas")
                        print("2 - Filtrar por dentista")
                        print("3 - Filtrar por data")
                        print("4 - Cancelar consulta de qualquer paciente")
                        print("0 - Voltar")
                        opcao_agenda = input("Escolha uma opção: ")

                        if opcao_agenda == "1":
                            if len(Agendamentos) == 0:
                                print("Não a consultas na agenda. ")
                            else:
                                for i in range(len(Agendamentos)):
                                    consulta = Agendamentos[i]
                                    nome_paciente = "Não encontrado"
                                    nome_dentista = "Não encontrado"
                                    for paciente in Pacientes:
                                        if paciente[1] == consulta[0]:
                                            nome_paciente = paciente[0]
                                            break
                                    for dentista in Dentistas:
                                        if dentista[0] == consulta[1]:
                                            nome_dentista = dentista[1]
                                            break
                                    print("\n Número:", i + 1)
                                    print("Paciente:", nome_paciente, "| CPF:", consulta[0])
                                    print("Dentista:", nome_dentista, "| ID:", consulta[1])
                                    print("Data:", consulta[2], "| Horário:", consulta[3])

                        elif opcao_agenda == "2":
                            codigo = input("ID do dentista: ")
                            encontrou = False
                            for consulta in Agendamentos:
                                if consulta[1].lower() == codigo.lower():
                                    encontrou = True
                                    print("CPF: ", consulta[0], "| Data:", consulta[2], "| Horario: ", consulta[3])
                            if encontrou == False:
                                print("Não existem consultas desse dentista.")

                        elif opcao_agenda == "3":
                            data = input("Data para filtrar (DD/MM/AAAA): ")
                            encontrou = False
                            for consulta in Agendamentos:
                                if consulta[2] == data:
                                    encontrou = True
                                    print("CPF :", consulta[0], "| Dentista ID :", consulta[1], "| Horarios :", consulta[3])
                            if encontrou == False:
                                print("Não existem consultas nessa data.")

                        elif opcao_agenda == "4":
                            if len(Agendamentos) == 0:
                                print("Não tem consultas para cancelar.")
                            else:
                                for i in range(len(Agendamentos)):
                                    consulta = Agendamentos[i]
                                    print("Número: ", i + 1, "| CPF :", consulta[0], "| Dentista ID: ", consulta[1], "| Horario: ", consulta[3])
                                numero = input("Número da consulta para cancelar: ")
                                indice = -1
                                for i in range(len(Agendamentos)):
                                    if numero == str(i + 1):
                                        indice = i
                                        break
                                if indice == -1:
                                    print("Número invalido.")
                                else:
                                    confirmar = input("Confirmar cancelamento? (s/n): ")
                                    if confirmar == "s" or confirmar == "S":
                                        Agendamentos.pop(indice)
                                        print("Consulta cancelada pela secretaria.")
                                    else:
                                        print("Cancelamento desistido.")
                        elif opcao_agenda == "0":
                            break
                        else:
                            print("Opção invalida.")
                elif opcao_adm == "0":
                    adm_logado = False
                    print("Saindo da administração...")
                else:
                    print("Opção invalida.")
                    
    elif opcao == "0":
        print("Sistema de atendimento encerrado. Volte sempre!")
        break
    else:
        print("Opção invalida. Escolha 0, 1 ou 2.")