#Escreva um programa que pergunte a quantidade de Km
#percorridos por um carro alugado e a quantidade de dias
#pelos quais ele foi alugado. Calcule o preçoa pagar, sabendo
#que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Quantos km foram percorridos com o carro desde a locação? "))
dias = int(input("Há quantos dias o carro foi alugado? "))

dias1 = dias * 60
km1 = km * 0.15

soma = dias1 + km1
print(f"Valor total a pagar: R${soma:.2f}.")