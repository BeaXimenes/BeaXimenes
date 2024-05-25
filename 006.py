#Crie um algoritmo que leia um número e mostre seu dobro,
#triplo e raiz quadrada.

num = int(input("Digite um número: "))

dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

print(f"O dobro de {num} corresponde a: {dobro};")
print(f"O triplo de {num} corresponde a: {triplo};")
print(f"E a raiz de {num} corresponde a {raiz:.2f}.")