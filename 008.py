#Escreva um programa que leia um valor em metros e
#exiba convertido em centímetros e em milímetros,
#quilometros, hectometros, decâmetros e decímetros.

m = float(input("Digite um valor em metros: "))

cm = m*100
mm = m*1000
km = m/1000
hm = m/100
dam = m/10
dm = m*10

print(f"{m}m em centímetros é: {cm:.2f}cm")
print(f"{m}m em milímetros é: {mm:.2f}ml")
print(f"{m}m em quilômetros é: {km:.2f}km")
print(f"{m}m em hectômetro é: {hm:.2f}hm")
print(f"{m}m em decâmetro é: {dam:.2f}dam")
print(f"{m}m em decímetro é: {dm:.2f}dm")