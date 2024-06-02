#Função Saque (keyword only)
def saque(*, parametro_saldo, parametro_valor, parametro_extrato):
    global saldo
    global extrato
    global saques_realizados
    saldo -= parametro_valor
    extrato += f"Saque no valor de R${parametro_valor}\n"
    saques_realizados += 1
    
    return saldo, extrato

#Função Depósito (positional only)
def deposito(parametro_saldo, parametro_valor, parametro_extrato, /):
    global saldo
    global extrato
    saldo += parametro_valor
    extrato += f"Depósito no valor de R${parametro_valor}\n"

    return saldo, extrato

#Função Extrato (positional & keyword)
def gerar_extrato(parametro_saldo, /, *, parametro_extrato):
    print("Extrato")
    print("Não encontramos movimentações na sua conta." if not parametro_extrato else parametro_extrato)
    print(f"Seu saldo atual é de R${parametro_saldo}")

#Função para criar usuários
def criar_usuario(nome, data_nascimento, cpf, endereço):
    global lista_usuarios
    novo_usuario = {"nome": nome,
                    "data_nascimento": data_nascimento,
                    "endereço": endereço
                    }
    chave_valor = {cpf: novo_usuario}
    lista_usuarios.append(chave_valor)
    print(f"\nCadastro realizado com sucesso. Seja bem vindo {novo_usuario["nome"]}!")

#Função para criar conta corrente
def criar_conta(cpf):
    global numero_conta
    NUMERO_AGENCIA = "0001"
    nova_conta = {"Agência": NUMERO_AGENCIA,
                  "Conta Corrente": numero_conta,
                  "Saldo": 0,
                  "Saques Realizados": 0}
    cpf_valor = {cpf: nova_conta}
    lista_contas.append(cpf_valor)
    print(f"Sua conta foi criada! Agência:{NUMERO_AGENCIA} Conta:{numero_conta}")
    numero_conta += 1

VALOR_LIMITE_DO_SAQUE = 500
LIMITE_SAQUE_DIARIO = 3

lista_usuarios = []
lista_contas = []
numero_conta = 1

menu_cadatro = """
Seja bem vindo! Você já é cliente OnBank?
[1] - Se sim, digite seu CPF, apenas os números.
[2] - Caso ainda não seja e deseje se cadastras, digite "c".
[3] - Caso deseje finalizar digite "q".
=> """

menu_servicos = """
Por favor escolha o serviço que deseja utilizar:
========================================================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
========================================================
=> """

while True:
    opcao_cadastro = input(menu_cadatro)

    if any(opcao_cadastro in usuario for usuario in lista_usuarios):
        indice = None
        for i, dicionario in enumerate(lista_contas):
            if opcao_cadastro in dicionario:
                indice = i
                break
        saldo = lista_contas[indice][opcao_cadastro]["Saldo"]
        saques_realizados = lista_contas[indice][opcao_cadastro]["Saques Realizados"]
        nome_usuario = lista_usuarios[indice][opcao_cadastro]["nome"]
        extrato = ""
        while True:
            print(f"Seja bem-vindo {nome_usuario}!")
            opcao_servico = input(menu_servicos)

            if opcao_servico.lower() == "d":

                print("Depósito")
                valor_deposito = float(input("Insira o valor que deseja depositar: "))
        
                if valor_deposito > 0:
                    deposito(saldo, valor_deposito, extrato)
                else:
                    print("Valor inválido, por favor insira um valor positivo.")

            elif opcao_servico.lower() == "s":

                print("Saque")
                valor_saque = float(input("Insira o valor que deseja sacar: "))

                if (valor_saque <= VALOR_LIMITE_DO_SAQUE) and ((saldo - valor_saque) >= 0) and (saques_realizados < LIMITE_SAQUE_DIARIO):
                    saque(parametro_saldo = saldo, parametro_valor = valor_saque, parametro_extrato = extrato)
                    saques_realizados = lista_contas[indice][opcao_cadastro]["Saques Realizados"] = saques_realizados
                else:
                    print(f"""Não foi possível realizar o saque, confira os seguintes requisitos:
============================================================================================
[1] - Valor do saque deve ser no máximo de R$500,00.
[2] - O valor de saque deve ser inferior ou igual ao seu saldo de R${saldo}.
[3] - Você já realizou {saques_realizados} de {LIMITE_SAQUE_DIARIO} saques diários.
============================================================================================""")

            elif opcao_servico.lower() == "e":
                gerar_extrato(saldo, parametro_extrato = extrato)
                lista_contas[indice][opcao_cadastro]["Saldo"] = saldo

            elif opcao_servico.lower() == "q":
                break
    
            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.\n")

    elif opcao_cadastro.lower() == "c":

        input_nome = input("Insira seu nome completo: ")
        input_data_nascimento = input("Insira sua data de nascimento no formato DD/MM/AAAA: ")
        input_cpf = input("Digite seu CPF, apenas os número: ")
        input_endereço = input("Insira seu endereço seguindo o formato 'logradouro, numero - bairro - cidade/sigla estado': ")
        
        criar_usuario(input_nome, input_data_nascimento, input_cpf, input_endereço)
        criar_conta(input_cpf)

    elif opcao_cadastro.lower() == "q":
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.\n")