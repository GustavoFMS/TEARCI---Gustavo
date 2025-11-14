'''
for i in range(6):
    print(i)
print('-'*30)

for i in range(2, 10):
    print(i)
print('-'*30)

for i in range(2,20,3):
    print(i)
print('-'*30)

for i in range(20,2,-3):
    print(i)
print('-'*30)

print(type(range(6)))
'''

'''
str = 'Python'
print(len(str))
print(str[0])
print(str[-3])
print(str[0:2])
print(str[:2])
print(str[::2])
print(str[::-1])
'on' in str
'''

'''
str = 'Python'
print(str.count('y'))
print(str.index('n'))
str = str+"!"
print(str)
for i in str:
    print(i)
'''

'''
Validações:

x = 0
x >= 0 and x <= 9 #True
x in range(10) #True
10 in range(10) #False

'''
'''
str = 'abcd.pt'
len(str) #7

print('-'*30)
for i in str:
    if i>='0' and i<='9':
        print(f'{i} é um valor númerico')
    else:
        print(f'{i} não é valor númerico')
print('-'*30)

for i in str:
    if i in range(10):
        print(True)
    else:
        print(False)
print('-'*30)

for i in str:
    if i>= 'a' and i<='z':
        print(f'{i} está entre a e z')
    else:
        print(f'{i} não está')
print('-'*30)

for i in str:
    if ord(i) in range (ord('a'), ord('z')+1):
        print(True)
    else:
        print(False)
for i in str:
    if not(i in 'KWN'):
        print(True)
    else:
        print(False)

'''

'''
    for i in range(0, len(str)):
        print(str[i])
'''

# Validar um nome
def validar_nome(nome):
    valido = 0

    if len(nome) < 6:
        print("O comprimento é insuficiente")
        return valido
    if nome.count(' ') == 0:
        for i in nome:
            if not (('a' <= i <= 'z') or ('A' <= i <= 'Z') or (i == ' ')):
                print("Seu nome não tem espaços e possui caracteres invalidos")
                return valido    
        print('Seu nome não tem espaços')
        return valido

    for i in nome:
        if not (('a' <= i <= 'z') or ('A' <= i <= 'Z') or (i == ' ')):
            print("Seu nome possui caracteres invalidos")
            return valido

    print('Tudo ok')
    valido = 1
    return valido

# Validar um email 
def validar_email_iefp(email):
    valido = 0
    arroba = email.index('@')

    if not('@formacao.iefp.pt' in email[-17:]):
        print('Seu email não termina em @formacao.iefp.pt')
        return valido

    for i in email[0:arroba]:
        if not(i.isnumeric() == True):
            print('Valores inseridos antes do @ são invalidos')
            return valido
     
    print('Tudo ok')
    valido = 1
    return valido

# Validar um telefone
def validar_telefone(telefone):
    valido = 0

    if not len(telefone) == 9:
        print('Comprimento Inválido')
        return valido
    
    if not telefone.isdigit():
        print('Seu numero tem caracteres invalidos!')
        return valido

    if not (telefone[0]=='9'):
        print('Primeiro digito invalido')
        return valido
    
    print('Tudo ok')
    valido = 1
    return valido

# Validar um codigo_Postal
def validar_codigopostal(codigopostal):
    valido = 0

    if not len(codigopostal) == 8:
        print('Comprimento do inválido')
        return valido

    if not codigopostal[:4].isdigit():
        print('Caracteres inválido nos primeiros quatros numeros')
        return valido
    
    if codigopostal[4] != '-':
        print('Codigo postal sem separadores')
        return valido
    
    if not codigopostal[5:].isdigit():
        print('Numeros de Extensão invalido')
        return valido
    
    print('Tudo ok')
    valido = 1
    return valido