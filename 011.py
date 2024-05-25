#Faça um programa que leia a largura e a altura de uma parede em
#metros. Clacule a sua área e a quantidade de tinta necessária para
#pinta-la. Sabendo-se que cada litro de tinta pinta uma área de 2m².

b = float(input("Quantos metros tem a base da área a ser pintada? "))
h = float(input("E quantos metros tem a altura dessa área? "))

calculo = b*h
print()
print(f"Sua parede tem a dimensão de {b} x {h} e sua área é de {calculo}m.")
l = calculo/2
print(f"Você precisará de {l}litros de tinta para pintá-la.")
