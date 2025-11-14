def fatorial(numero = int(input("Qual numero deseja saber o fatorial? \n→ "))):
    fatoracao = 1
    i = numero
    while i > 1:
        fatoracao = fatoracao * i
        i -= 1
    return (f"| A fatoração do numero {numero} | \n→ {fatoracao}")

print(fatorial())