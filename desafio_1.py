menu = """
Por favor escolha o serviço que deseja utilizar:
========================================================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
========================================================
=> """

saldo = 0
VALOR_LIMITE_DO_SAQUE = 500
extrato = ""
saques_realizados = 0
LIMITE_SAQUE_DIARIO = 3

while True:
    
    opcao = input(menu)

    if opcao.lower() == "d":

        print("Depósito")
        valor_deposito = float(input("Insira o valor que deseja depositar: "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito no valor de R${valor_deposito}\n"
        else:
            print("Valor inválido, por favor insira um valor positivo.")

    elif opcao.lower() == "s":

        print("Saque")
        valor_saque = float(input("Insira o valor que deseja sacar: "))

        if (valor_saque <= VALOR_LIMITE_DO_SAQUE) and ((saldo - valor_saque) >= 0) and (saques_realizados < LIMITE_SAQUE_DIARIO):
            saldo -= valor_saque
            extrato += f"Saque no valor de R${valor_saque}\n"
            saques_realizados += 1
        else:
            print(f"""Não foi possível realizar o saque, confira os seguintes requisitos:
============================================================================================
[1] - Valor do saque deve ser no máximo de R$500,00.
[2] - O valor de saque deve ser inferior ou igual ao seu saldo de R${saldo}.
[3] - Você já realizou {saques_realizados} de {LIMITE_SAQUE_DIARIO} saques diários.
============================================================================================""")

    elif opcao.lower() == "e":
        print("Extrato")
        print("Não encontramos movimentações na sua conta." if not extrato else extrato)
        print(f"Seu saldo atual é de R${saldo}")

    elif opcao.lower() == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.\n")