def soma_while(inf, sup):
    i = inf
    resultado = 0

    while i <= sup:
        resultado = resultado + i
        i += 1
    return resultado

def soma_for(inf, sup):
    resultado = 0

    for i in range(inf, sup+1):
        resultado = resultado + i
    return resultado

def multiplicacao_while(m, n):
    ciclo = 1
    resultado = 0
    
    while ciclo <= n:
        resultado = resultado + m
        ciclo +=1
    return resultado

def multiplicacao_for(m, n):
    resultado = 0

    for ciclo in range(1, n+1):
        resultado = resultado + m
    return resultado

def exponenciacao_while (base, expoente):
    i = 1
    resultado = 1
    while i <= expoente:
        resultado = resultado * base
        i+=1
    return resultado

def exponenciacao_for (base, expoente):
    resultado = 1
    for i in range(1, expoente+1):
        resultado = resultado * base
    return resultado
    
def exponenciacao_with_function_while(base, expoente):
    i = 1
    resultado = 1

    while i <= expoente:
        resultado = multiplicacao_while (resultado, base)
        i+=1
    return resultado

def exponenciacao_with_function_for(base, expoente):
    i = 1
    resultado = 1

    for ciclo in range(1, expoente+1):
        resultado = multiplicacao_while (resultado, base)
    return resultado
    
#print(soma_while(inf = int(input("Digite o valor inferior: ")), sup = int(input("Digite o valor superior: ")))) # chamada da função para somar usando while
#print(soma_for(inf = int(input("Digite o valor inferior: ")), sup = int(input("Digite o valor superior: ")))) # chamada da função para somar usando for
#print(multiplicacao_while(m = int(input("Digite o primeiro valor: ")), n = int(input("Digite o segundo valor: "))))
#print(multiplicacao_for(m = int(input("Digite o primeiro valor: ")), n = int(input("Digite o segundo valor: "))))
#print(exponenciacao_for(numero = int(input("Digite o numero: ")), expoente = int(input("Digite o expoente: "))))
#print(exponenciacao_with_function_while(5, 2))
#print(exponenciacao_with_function_while(2, 4))