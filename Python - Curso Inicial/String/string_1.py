"""
nome = str(input("Qual o seu nome ?"))

print(nome.upper())
print(nome.lower())
print(nome.title())
"""

texto = "  Olá mundo   "

print(texto)
print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")

menu = "Python"
print("###" + menu + "###")
print(menu.center(14,))
print(".".join(menu))
