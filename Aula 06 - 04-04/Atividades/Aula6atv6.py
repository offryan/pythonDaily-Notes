nota1 = float(input('Digite a 1° nota: '))
nota2 = float(input('Digite a 2° nota: '))
media = (nota1 + nota2)/2

if media >= 9.0 or media <= 10:
    print('conceito: A\nMensagem: Aprovado')
elif media >= 7.5 or media < 9:
    print('conceito: B\nMensagem: Aprovado')
elif media >= 6.0 or media < 7.5:
    print('conceito: C\nMensagem: Aprovado')
elif media >= 4.0 or media < 6.0:
    print('conceito: D\nMensagem: Aprovado')
elif media < 4:
    print('conceito: E\nMensagem: Aprovado')
