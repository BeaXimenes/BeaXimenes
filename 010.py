#Crie um programa que leia quanto dinheiro uma pessoa tem
#na carteira e mostre quantos dólares ela pode comprar.
#Considere U$$1.00 = R%3.27

carteira = float(input("Digite quantos R$(reais) você tem na carteira: "))
calculo = carteira / 3.27
print(f"Com R${carteira:.2f} reais você consegue comprar U$${calculo:.2f} dólares.")

