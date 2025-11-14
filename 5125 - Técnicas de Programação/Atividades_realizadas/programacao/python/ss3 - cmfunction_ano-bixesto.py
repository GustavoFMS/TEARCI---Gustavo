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

print(ano_bissexto(2000)) # É um ano bissexto
print(ano_bissexto(2100)) # É um ano bissexto