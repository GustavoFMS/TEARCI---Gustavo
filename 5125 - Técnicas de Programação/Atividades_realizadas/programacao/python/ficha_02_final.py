''' Definir uma função (par) que retorne se um numero positivo (n) é par ou não é''' 

def par(n):
    valido = 0
    if n < 0 :
        print(f'Erro: O numero {n} é negativo')
        return valido
    if n % 2 == 0:
        print(F'O numero {n} é par')
        valido = 1
        return valido
    else:
        print(F'O numero {n} não é par')
        return valido


'''
Definir uma função (semáforo). Tem como argumento uma cor (vermelho, amarelo ou verde) e 
como resultado uma das seguintes saídas: 
Semáforo (‘vermelho’) >>> “Passagem proibida” 
Semáforo (‘amarelo’) >>> “Transição para vermelho” 
Semáforo (‘verde’) >>> “Passagem autorizada” 
Semáforo (‘xpto’) >>> “Côr inválida” 
'''
def semaforo(cor):
    valido = 0
    cor = cor.lower()
    if cor == 'vermelho':
        valido = 1
        return 'Passagem Proibida', f'Valido = {valido}'
    elif cor == 'amarelo':
        valido = 1
        return 'Transição para vermelho', f'Valido = {valido}'
    elif cor == 'verde':
        valido = 1
        return 'Passagem autorizada', f'Valido = {valido}'
    else:
        return 'Cor invalida', f'Valido = {valido}'


'''
Definir uma função (fact_w) que calcule o factorial de um número inteiro positivo (n) com recurso à 
instrução WHILE. 
'''

def fact_w(n):
    valido = 0
    fatoracao = 1
    i = n

    if n < 0:
        return 'Valor negativo digitado', f'Valido = {valido}'

    while i > 1:
        fatoracao = fatoracao * i
        i -= 1
        valido = 1
    return (f"A fatoração do numero {n} é {fatoracao}"), f'Valido = {valido}'

'''
Definir uma função (fact_f) que calcule o factorial de um número inteiro positivo (n) com recurso à 
instrução FOR. 
'''

def fact_f(n):
    resultado_fatoracao = 1
    valido = 0
    i = 0

    if n < 0:
        return 'Valor negativo digitado',valido

    for i in range(1, n+1):
        resultado_fatoracao = resultado_fatoracao * i
        i = i + 1
        valido=1
    return (f"A fatoração do numero {n} é {resultado_fatoracao}"), f'Valido = {valido}'
    
'''
Definir a função Factorial (fact_r) de um número inteiro positivo (n) como uma função recursiva 
(f(n)=n*f(n-1)).
'''

def fact_r(n):
    valido = 0
    if n < 0:
        return 'Valor negativo digitado', f'Valido = {valido}'

    if n == 1:
        return 1
    return n * fact_r(n-1)

'''
Definir uma função em que dada uma lista de números inteiros (ex: [1,2,3,4,5,6,7,8,9]), retorne o 
número de elementos (9 no caso exemplo), a soma de todos os elementos (45, no caso exemplo) e a 
média dos elementos (5, no caso exemplo). Nota: Sem recorrer a outras funções (como por ex: len()) 
'''

def sdl(lista):
    resultado_soma = 0
    for i in lista:
        resultado_soma = resultado_soma + i
    media = resultado_soma / (i)

    return (f'O numero total de elementos é = {i}'), f'A soma é = {resultado_soma}', f'A media é = {media}'

'''
O algoritmo é simples: 
-Multiplica-se o primeiro dígito do NIF por 9, o segundo por 8, e assim sucessivamente. Somam-se 
esses produtos. O resultado a dividir por 11 terá que dar resto O ou 1 (zero ou um)
'''

def val_nif(nif):
    valido = 0
    comprimento = len(nif)
    
    if comprimento != 9:
        return "Comprimento Invalido", valido
    
    if not nif.isdigit():
        return "Digito invalido", valido
    
    soma = 0
    contador = 9

    for i in range(comprimento):
        soma += int(nif[i]) * contador
        contador -= 1
    print(soma)

    if not (soma % 11 == 0 or soma % 11 == 1):
        return f'Nif Invalido', f'Valido = {valido}'
    else:
        valido = 1
        return f'Nif Valido', f'Valido = {valido}'