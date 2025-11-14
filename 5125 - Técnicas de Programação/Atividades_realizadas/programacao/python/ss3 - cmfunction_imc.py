def imc(peso, altura):
    imc = peso / (altura**2)

    if(imc < 18.5):
        return(f"Seu IMC é {imc:.2f} | Classificação: MAGREZA")
    elif(imc >= 18.5 and imc < 24.9):
        return(f"Seu IMC é {imc:.2f} | Classificação: NORMAL")
    elif(imc >= 25 and imc < 29.9):
        return(f"Seu IMC é {imc:.2f} | Classificação: SOBREPESO")
    elif(imc >= 30 and imc < 34.9):
        return(f"Seu IMC é {imc:.2f} | Classificação: OBESIDADE GRAU I")
    elif(imc >= 35 and imc < 39.9):
        return(f"Seu IMC é {imc:.2f} | Classificação: OBESIDADE GRAU I")    
    else:
        return(f"Seu IMC é {imc:.2f} | Classificação: OBESIDADE GRAU I")

print(imc(peso = float(input("Peso: ")), 
          altura = float(input("Altura: "))))


