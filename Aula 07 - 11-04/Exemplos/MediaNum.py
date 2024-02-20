
contador = 0
soma = 0

while True:
    
    num = int(input('Digite um número inteiro (0 para sair): '))
    
    if num in 'sS':
        soma = soma + int(num)
    
        contador = contador + 1 
         
        break
    
    media = soma/contador
    print(f'A média dos números digitados é: {media}')