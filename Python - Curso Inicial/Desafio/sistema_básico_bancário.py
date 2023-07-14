""""
Sistema Bancário Simples em Python

Bem-vindo ao repositório do Sistema Bancário Simples em Python! Este projeto implementa um sistema básico de gerenciamento de conta bancária, permitindo depósitos, saques e a visualização do extrato.

O sistema utiliza a linguagem de programação Python e oferece uma interface de linha de comando simples e intuitiva. Ao executar o programa, o usuário é apresentado a um menu com as opções de depósito, saque, extrato e sair.

Durante a execução, o usuário pode realizar depósitos informando o valor desejado, verificar o saldo disponível, efetuar saques respeitando um limite de operações e consultar o extrato contendo todas as movimentações realizadas.

O projeto utiliza variáveis para rastrear o saldo, o número de saques, o limite de operações e o extrato. O código é estruturado em um loop contínuo, permitindo que o usuário execute múltiplas operações antes de decidir sair do sistema.

Este repositório serve como um exemplo básico de aplicação de conceitos de programação em Python para criar um sistema bancário simples. É útil para fins educacionais e para quem deseja entender os fundamentos de um sistema de conta bancária.

Fique à vontade para explorar o código-fonte, fazer melhorias ou adaptá-lo às suas necessidades. Contribuições são bem-vindas!

Divirta-se usando o Sistema Bancário Simples em Python!
"""


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
