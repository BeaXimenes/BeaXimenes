#Faça um algoritmo que leia o salario de um
#funcionário e mostre seu novo salário, com 15% de
# aumento.

s = float(input("Qual o valor atual do salário do funcionário?: R$ "))

novo = s + (s * 15 / 100)
print(f"Com o reajuste salarial de 15%, seu salário de R${s:.2f} passará a custar R${novo:.2f}.")