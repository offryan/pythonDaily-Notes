dec = int(input('Digite um número decimal: '))
bin = ''

while dec != 0:
    
    r = dec%2
    bin = bin + str(r)
    dec = dec//2

print(bin)