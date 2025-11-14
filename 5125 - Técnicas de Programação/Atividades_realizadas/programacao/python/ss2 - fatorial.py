numero = int(input("Qual numero deseja saber o fatorial? \n→ "))
fatorial = 1
i = numero

while i > 1:
    fatorial = fatorial * i
    i -= 1
print(f"| A fatoração do numero {numero} | \n→ {fatorial}")