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
