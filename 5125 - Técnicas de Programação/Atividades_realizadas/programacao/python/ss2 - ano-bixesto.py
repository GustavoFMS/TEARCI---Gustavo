
ano = int(input("Qual ano você deseja saber se é bissexto? \n→ "))

if (ano % 4 == 0):
    if (ano % 100 == 0):
        if (ano % 400 == 0):
            print("É um ano bissexto") 
        else:
            print("Não é bissexto")
    else:
        print("É bissexto")
else:
    print("Não é bissexto")
"""
if (ano % 400 == 0):
    print("É um ano bixesto") 
elif(ano % 100 == 0):
    print("Não é bixesto")
elif(ano % 4 == 0):
    print("É um ano bixesto")
else:
    print("Não é bixesto")
"""