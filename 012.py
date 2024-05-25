#Faça um algorítmo que leia o preço de um produto
#e mostre seu novo preço, com 5% de desconto.

num = float(input("Qual o valor do produto a ser consultado? "))

desconto = num - (num * 5 / 100)
print(f"O preço que custava R${num:.2f}, com desconto de 5% custa R${desconto:.2f}.")
