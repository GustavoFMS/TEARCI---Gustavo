def fatoracaowhile(numero):
    fatoracao = numero
    i = 1

    while i < numero:
        fatoracao = fatoracao * i
        i += 1
    return f'\n→ Fatorial de {numero}! = {fatoracao}'

def fatoracaofor(numero):
    fatoracao = numero
    i = 1

    for i in range(i, fatoracao, 1):
        fatoracao = fatoracao * i
    return f'\n→ Fatorial de {numero}! = {fatoracao}'

numero = int(input("Qual numero deseja saber o fatorial? \n→ "))
print(fatoracaowhile(numero))
print(fatoracaofor(numero))
