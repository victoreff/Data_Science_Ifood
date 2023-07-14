# Faca um programa que receba dois numeros e mostre qual deles é o maior.

num1 = int(input("Me de um número"))
num2 = int(input("Me de o segundo número"))

if num1 > num2:
    print("O número 1 é maior do que o número 2 ".format(num1, num2))
elif num1 < num2:
    print("O número 2 é maior do que o número 1")
elif num1 == num2:
    print("São iguais")
