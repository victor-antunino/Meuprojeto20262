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

    opção = int(input("\nDigite qual opção deseja: "))

    if opção == "1":
        print("\nVocê está acessando como paciente.")
        nome = input("\nDigite seu nome: ")
        cpf = input("\nDigite seu CPF: ")
        telefone = input("\nDigite seu telefone: ")
        paciente = -1
        for i in range(len(Pacientes)):
            if Pacientes[i][0] == cpf:
                paciente = i
                break

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

            