valor = float(input("Digite o valor da compra:"))
parcelas = int(input("Digite o valor da parcela, somente 2|4|6|8:"))

match(parcelas):
    
    case 2: valor = valor * 1.03
    case 4: valor = valor * 1.07 
    case 6: valor = valor * 1.09
    case 8: valor = valor * 1.12
    case _: valor = 0

if valor == 0:
    print("Opção inválida")
else:
    print(f"O valor de cada parcela é R${valor/parcelas}")
    
    
#if parcelas == 2:
#    juro = 3/100
#elif parcelas == 4:
    #juro = 7/100
#elif parcelas == 6:
    #juro = 9/100
#elif parcelas == 9:
    #juro = 12/100

#if juro == 0:
    #print("Parcelamento inválido")
#else:
    #total = valor*(1+juro)
    #print(f"Valor da parcela: R$ {total/parcelas}")
      