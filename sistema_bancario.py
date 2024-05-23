menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 3
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        #print("Deposito")
        valor = float(input("Informe o valor a ser depositatado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else: 
            print("Operação invalido. O numero informado não é valido")

    elif opcao == "2":
        #print("Saque")
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo: 
            print("Operação falhou! Saldo insuficiente")

        elif excedeu_limite:
            print("Operaçao invalido. O valor do saque excede o limite")

        elif excedeu_saques: 
            print("Operação invalida, numero maximo de saques excedido")

        elif valor > 0:
            saldo += valor
            extrato +=f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou. Numero informado é invalido")

    elif opcao == "3":
        #print("Extrato")
        print("\n==================Etrato==================")
        print("Não foram realizado movimentação" if not extrato else extrato)
        print(f"\nSaldo R$ {saldo:.2f}\n")
        print("==========================================")

    elif opcao == "4":
        print("Saindo")
        break

    else:
        print("Operação invalida, por favor, selecione novamente a operaçao desejada.")