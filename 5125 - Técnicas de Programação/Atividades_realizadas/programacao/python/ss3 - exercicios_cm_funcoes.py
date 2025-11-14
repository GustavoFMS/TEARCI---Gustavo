def ciclodesomar():
    contador = 0
    soma = 0

    while contador<100:
        soma +=1 #soma= soma+1
        contador+=1 #contador= contador+1
    return f"A soma é igual a {soma}"

#print(ciclodesomar()) #Basta remover o primeiro # antes do print para realizar o teste

def ano_bissexto(ano):
    if (ano % 4 == 0):
        if (ano % 100 == 0):
            if (ano % 400 == 0):
                return "É um ano bissexto" 
            else:
                return "Não é bissexto"
        else:
            return "É bissexto"
    else:
        return "Não é bissexto"

#print(ano_bissexto(int(input("Digite o ano que desejas saber o dia da pascoa: \n→ ")))) #Basta remover o primeiro # antes do print para realizar o teste

def ciclosomar():
    soma = 0

    for i in range(100):
        soma = soma + i
        """print(f"soma = {soma}")"""
    return f"A soma é igual a {soma}"

#print(ciclosomar()) #Basta remover o primeiro # antes do print para realizar o teste

'''
def celsius(c):
    resultado = (c * 1.8) + 32
    print(f"{resultado}ºF")

def fahrenheit(f):
    resultado = (f - 32) / 1.8
    print(f"{resultado}ºC")

resposta = "vazio"

while((resposta != "C" and resposta!="c") and (resposta!="F" and resposta!="f")):
    resposta = str(input("\nQual você quer converter?  C ou F \n→"))

    if(resposta=="C" or resposta=="c"):
        celsius(int(input("\nInforme os graus celcius ºC: ")))
    elif(resposta=="F" or resposta=="f"):
        fahrenheit(int(input("\nInforme os graus fahrenheit ºF: ")))
'''

# Para testar o algoritmo acima basta tirar as aspas triplas acima e abaixo do código

def ciclodesomar():
    contador = 0
    soma = 0

    while contador<100:
        soma +=1 #soma= soma+1
        contador+=1 #contador= contador+1
    return f"A soma é igual a {soma}"

#print(ciclodesomar()) #Basta remover o primeiro # antes do print para realizar o teste

def fatorial(numero):
    fatoracao = 1
    i = numero
    while i > 1:
        fatoracao = fatoracao * i
        i -= 1
    return (f"| A fatoração do numero {numero} | \n→ Fatoração = {fatoracao}")


#print(fatorial(int(input("Qual numero deseja saber o fatorial? \n→ ")))) #Basta remover o primeiro # antes do print para realizar o teste

def hello(nome):
    return f'Hello {nome}!'

#print(hello('world')) #Basta remover o primeiro # antes do print para realizar o teste

def imc(peso, altura):
    imc = peso / (altura**2)

    if(imc < 18.5):
        return(f"Seu IMC é {imc:.2f} | Classificação: MAGREZA")
    elif(imc >= 18.5 and imc < 24.9):
        return(f"Seu IMC é {imc:.2f} | Classificação: NORMAL")
    elif(imc >= 25 and imc < 29.9):
        return(f"Seu IMC é {imc:.2f} | Classificação: SOBREPESO")
    elif(imc >= 30 and imc < 34.9):
        return(f"Seu IMC é {imc:.2f} | Classificação: OBESIDADE GRAU I")
    elif(imc >= 35 and imc < 39.9):
        return(f"Seu IMC é {imc:.2f} | Classificação: OBESIDADE GRAU I")    
    else:
        return(f"Seu IMC é {imc:.2f} | Classificação: OBESIDADE GRAU I")

#print(imc(peso = float(input("Peso: ")), altura = float(input("Altura: ")))) #Basta remover o primeiro # antes do print para realizar o teste

'''
def jogo(equipe_casa, equipe_fora, golos_casa, golos_fora):
    print("\n","*" * 20, "Jogo","*" * 20)
    print(f"Nome da Equipa da Casa: {equipe_casa}")
    print(f"Nome da Equipa de Fora: {equipe_fora}")
    print(f"Golos equipe casa: {golos_casa}")
    print(f"Golos equipe fora: {golos_fora}")
    print("\n","-" * 20, "Resultado","-" * 20)

    if (golos_casa > golos_fora):
        return(f"A equipe da casa venceu por: \n{equipe_casa} | {golos_casa} x {golos_fora} | {equipe_fora}")
    elif (golos_casa < golos_fora):
        return(f"A equipe de fora venceu por: \n{equipe_fora} | {golos_fora} x {golos_casa} | {equipe_casa}")
    else:
        return(f"O jogo empatou em: \n{equipe_casa}| {golos_casa} x {golos_fora} |{equipe_fora}")

print(jogo("Benfica", "Porto", 2, 1))
print("\n","*" * 20, "Jogo","*" * 20)
'''

# Para testar o algoritmo acima basta tirar as aspas triplas acima e abaixo do código

def par (numero):
    if(numero % 2 == 1):
        return (f"O numero {numero} é: impar")
    else:
        return (f"O numero {numero} é: par")

#print(par(int(input("Digite um numero: \n→ ")))) #Basta remover o primeiro # antes do print para realizar o teste

def pascoa(ano):
    x = 24 # variaveis da formula para o calculo da pascoa, obs: NÃO ALTERAR
    y = 5 # variaveis da formula para o calculo da pascoa, obs: NÃO ALTERAR
    a = ano % 19 # variaveis da formula para o calculo da pascoa, obs: NÃO ALTERAR
    b = ano % 4 # variaveis da formula para o calculo da pascoa, obs: NÃO ALTERAR
    c = ano % 7 # variaveis da formula para o calculo da pascoa, obs: NÃO ALTERAR
    d = (( 19 * a ) + x) % 30 # variaveis da formula para o calculo da pascoa, obs: NÃO ALTERAR
    e = (( 2 * b ) + ( 4 * c ) + ( 6 * d ) + y) % 7 # variaveis da formula para o calculo da pascoa, obs: NÃO ALTERAR

    if ( d + e ) < 10 :
        dia = d+e+22 # variaveis da formula para o calculo da pascoa, obs: NÃO ALTERAR
        mes = "Março" # variaveis da formula para o calculo da pascoa, obs: NÃO ALTERAR
        return f"Dia: {dia}/{mes}"
    else:
        dia = d+e-9 # variaveis da formula para o calculo da pascoa, obs: NÃO ALTERAR
        mes = "Abril" # variaveis da formula para o calculo da pascoa, obs: NÃO ALTERAR
        return f"Dia: {dia}/{mes}"
    
#print(pascoa(ano = int(input("Qual ano você deseja saber o dia da pascoa: \n→ ")))) #Basta remover o primeiro # antes do print para realizar o teste

def sinal (numero):
    if numero > 0:
        return "O numero é Positivo"
    elif numero < 0:
        return "O numero é Negativo"
    else:
        return "O numero é igual Zero"

#print(sinal(int(input("Digite um número: \n→ ")))) #Basta remover o primeiro # antes do print para realizar o teste