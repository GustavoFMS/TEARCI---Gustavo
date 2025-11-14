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
    
print(pascoa(ano = int(input("Qual ano você deseja saber o dia da pascoa: \n→ "))))