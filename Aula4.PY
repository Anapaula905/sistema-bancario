saldo = 0
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUE = 500
LIMITE_SAQUES = 3

while True:
    print("\n========== BANCO ==========")
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[q] Sair")
    print("============================")

    opcao = input("Escolha uma opção: ").lower()

    # DEPÓSITO
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    # SAQUE
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))

        if valor <= 0:
            print("Valor de saque inválido.")

        elif valor > LIMITE_DE_SAQUE:
            print(f"O valor máximo por saque é de R$ {LIMITE_DE_SAQUE:.2f}.")

        elif valor > saldo:
            print("Saldo insuficiente.")

        elif numero_de_saques >= LIMITE_SAQUES:
            print("Limite diário de saques atingido.")

        else:
            saldo -= valor
            numero_de_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("Saque realizado com sucesso.")

    # EXTRATO
    elif opcao == "e":
        print("\n========== EXTRATO ==========")

        if extrato:
            print(extrato)
        else:
            print("Não foram realizadas movimentações.")

        print(f"Saldo atual: R$ {saldo:.2f}")

    # SAIR
    elif opcao == "q":
        print("Obrigado por utilizar nosso banco!")
        break

    # OPÇÃO INVÁLIDA
    else:
        print("Operação inválida. Por favor, escolha uma opção válida.")