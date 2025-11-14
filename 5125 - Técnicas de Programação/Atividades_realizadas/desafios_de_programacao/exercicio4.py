peso = float(input("Qual é o seu peso: \n→ "))
altura = float(input("Qual é a sua altura: \n→ "))
imc = peso / (altura**2)

if imc < 18.5:
    print(f"Seu imc é: {imc:.2f}kg/m² | Sua classificação é: Baixo do Peso")
elif imc >= 18.5 and imc < 25:
    print(f"Seu imc é: {imc:.2f}kg/m² | Sua classificação é: Peso adequado")
elif imc >= 25 and imc < 30:
    print(f"Seu imc é: {imc:.2f}kg/m² | Sua classificação é: Sobrepeso")
else:
    print(f"Seu imc é: {imc:.2f}kg/m² | Sua classificação é: Obesidade")

