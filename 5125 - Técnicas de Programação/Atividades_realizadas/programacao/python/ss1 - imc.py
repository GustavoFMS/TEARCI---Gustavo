print(" ")
print(" "*20,"IMC"," "*20)

peso = float(input("Peso: "))
altura = float(input("Altura: "))
imc = peso / (altura**2)

print(f"O seu IMC é igual a {imc:.2f}")

if(imc < 18.5):
    print(f"Classificação: MAGREZA")
elif(imc >= 18.5 and imc < 24.9):
    print(f"Classificação: NORMAL")
elif(imc >= 25 and imc < 29.9):
    print(f"Classificação: SOBREPESO")
elif(imc >= 30 and imc < 34.9):
    print(f"Classificação: OBESIDADE GRAU I")
elif(imc >= 35 and imc < 39.9):
    print(f"Classificação: OBESIDADE GRAU I")    
else:
    print(f"Classificação: OBESIDADE GRAU I")