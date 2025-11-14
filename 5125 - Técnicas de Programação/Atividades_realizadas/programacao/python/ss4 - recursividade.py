def fact (n):
    if n == 1:
        return 1
    return n * fact(n-1)

def soma_n_r(num1, num2):
    if num2 == num1:
        return num1
    return num2 + soma_n_r(num1, num2-1)

def mult_r(mult1, mult2):
    if mult2 == 0 or mult1 == 0:
        return 0
    return mult1 + mult_r(mult1, mult2-1)

def Pot_r(base, exp):
    if exp==1:
        return base
    return base * Pot_r(base, exp-1) 

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def mover_caixa(n, orig, dest, aux=' '):
    if n== 1:
        print(f'Caixa {n} {orig} --> {dest}')
    else:
        mover_caixa(n-1, orig, aux, dest)
        print(f'Caixa {n} {orig} --> {dest}')
        mover_caixa(n-1, orig, aux, dest)