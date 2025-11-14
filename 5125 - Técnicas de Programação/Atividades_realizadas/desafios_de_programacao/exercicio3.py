km = float(input("Digite a quantidade de km percorridos: "))
gm = float(input("Valor gasto medio (l/100km's): "))
preco = float(input("Preço do combustivel em  €: "))
consumo = km * gm / 100
custo = km * gm * preco / 100
print(f"O valor consumido foi de {consumo} L , o custo da viagem foi de {custo:.2f} €")