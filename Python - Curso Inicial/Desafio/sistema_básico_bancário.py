extrato = ""
saldo = 0
valor_limite_de_saque = 500
numero_de_saques = 0
LIMITE_DE_OPERACAO_SAQUE = 3

menu = (
    "Olá! Seja Bem-vindo ao Sistema Bancário\nEscolha um serviço:\n[D] Depósito\n[S] Sacar\n[E] Extrato\n[Q] Sair\n")

while True:
    opcao = input(menu)

    if opcao == "D":

        valor_do_deposito = float(
            input("Qual o valor que você quer depositar? "))

        if valor_do_deposito > 0:
            saldo += valor_do_deposito
            extrato += "Depósito de {:.2f}\n".format(valor_do_deposito)
            print("Parabéns, você depositou {} reais\n Escolha outra opção:".format(
                valor_do_deposito))

        else:
            print("Operação falhou, valor inválido!")

    elif opcao == "S":
        valor_do_saque = float(
            input("Qual o valor do saque? "))

        if valor_do_saque > saldo:
            print("Você não tem saldo!")

        elif numero_de_saques >= LIMITE_DE_OPERACAO_SAQUE:
            print("Você excedeu o limite de saques")

        else:
            saldo -= valor_do_saque
            numero_de_saques += 1
            extrato += "Saque de {:.2f}\n".format(valor_do_saque)
            print("Saque Realizado com Sucesso!\n Escolha outra Opção:")

    elif opcao == "E":
        print("Extrato".center(20, " "))

        if extrato == "":
            print("Não houve movimentações")
        else:
            print("Suas Movimentações são:\n{}\nSaldo Total: {:.2f}".format(
                extrato, saldo))

    elif opcao == "Q":
        print("Muito obrigado por acessar nosso sistema!\n Até a proxima!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
