MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe a sua idade"))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

elif idade == IDADE_ESPECIAL:
    print("Pode aulas teóricas")

else:
    print("Não pode! Burro")

    
