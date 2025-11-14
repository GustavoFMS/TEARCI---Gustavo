def sinal (numero):
    if numero > 0:
        return "O numero é Positivo"
    elif numero < 0:
        return "O numero é Negativo"
    else:
        return "O numero é igual Zero"

print(sinal(int(input("Digite um número: \n→ ")))) 