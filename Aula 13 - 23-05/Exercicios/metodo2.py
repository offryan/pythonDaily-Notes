def soma(a, b):
    return a+b

def subtracao(a, b):
    return a-b

def multiplicacao(a, b):
    return a*b

def divisao(a, b):
    return a/b

def raiz(a):
    return a**0.5

while True:
    print("[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão")
    print("[5] Raiz quadrada\n[0] Sair")
    op = input("Digite uma opção: ")
    if op == 0: break
    elif op == 5:
        a = float(input("Digite o valor: "))
        print(f"Raiz de {a} = {raiz(a)}")
    else:
        a = float(input("Digite o primeiro valor"))
        b = float(input("Digite o segundo valor"))
        if op == 1: print(soma(a,b))
        if op == 2: print(subtracao(a,b))
        if op == 3: print(multiplicacao(a,b))
        else: divisao(a,b)