"""def par (numero):
    return numero % 2 == 0"""

def par (numero):
    if(numero % 2 == 1):
        return (f"O numero {numero} é: impar")
    else:
        return (f"O numero {numero} é: par")

print(par(int(input("Digite um numero: \n→ "))))