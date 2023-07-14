
"""
contador = 0
while contador <= 5:
    print(contador)
    contador += 1

while True:
    numero = int(input('Informe um número:'))

    if numero == 10:
        break

    print(numero)

"""

"""
for numero in range(100):

    if numero % 2 == 0:
        continue
    
    if numero == 10:
        break

    print(numero)"""

while True:
    numero = int(input("Qual o número:"))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)
