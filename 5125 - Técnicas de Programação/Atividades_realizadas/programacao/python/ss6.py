''' 
Algoritmo - ISBN
- multiplicar cada digito alternadamente por 1 e 3
- somar esses produtos
- se a soma for divisivel por 10 o checkdigit é valido
# 13 digitos
    # 1 - 3 digitos
    # 2 - 1 digitos
    # 3 - 3 digitos
    # 4 - 5 digitos
    # 5 - checkdigit(0) 
    # only digits
'''

def multiplicar_intercalado(num):
    if num == 1:
        return 3
    else:
        return 1

def isbn (codigo):
    valido = 0
    mult = 1
    multiplicador = 1
    resultado_multiplicacao = 0

    # Validando o comprimento
    if not len(codigo) == 13:
        print(f"Seu codigo possui o comprimento invalido: {len(codigo)} de tamanho")
        return valido
    
    # Validando se é digito
    if not codigo.isdigit():
        print(f"Digito invalido!")
        return valido
    
    # Multiplicação
    for i, num in enumerate(codigo):
        mult = int(num) * multiplicador
        print(mult)
        multiplicador = multiplicar_intercalado(multiplicador)
        resultado_multiplicacao +=  mult
    print(resultado_multiplicacao)

    '''
    for i, num in enumerate(codigo):
        if i % 2 == 0:
            mult = int(num) * 1
            print(mult)
        else:
            mult = int(num) * 3
            print(mult)
        resultado_multiplicacao +=  mult
    '''
    # Verificar o checkdigit se é um codigo valido
    if not (resultado_multiplicacao % 10 == 0):
        print("O codigo digitado é invalido!")
        return valido
    
    # Se tudo der ok
    print('Codigo valido')
    valido = 1
    return valido

''' 
Algoritmo 2 - Matricula de Carro PT
- Nº de caracteres
- Validações de caracteres
    digitos (0 a 9)
    letras entre a - z sem (YKW)
- Agrupamento
    Dois a dois do mesmo tipo
-Sequencia valida
    tipo 1: 
        AA 00 AA
'''

def validar_placa(matricula):
    valido = 0
   # Comprimento da matricula 
    if len(matricula) != 6:
        print("Comprimento Invalido")
        return valido