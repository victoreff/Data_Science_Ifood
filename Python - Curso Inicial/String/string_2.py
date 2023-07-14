
nome = "Victor"
idade = 20
Cidade = "Manaus"

print("Olá meu nome é {}, tenho {} anos, e sou de {}!".format(nome, idade, Cidade))

saldo = 45.478
dados = {"nome": "Victor", "idade": 20, }
print("Nome:{nome} Idade:{idade}".format(**dados))

print("Nome: {}, idade: {} anos, seu saldo é {:.2f} reais".format(nome, idade, saldo))
