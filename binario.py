try:
    decimal=int (input('Introduzca un numero decimal: '))
except:
    print('¡Valor no valido!')

#obtemos el binario en cadenas
if(decimal>=0):
    binario=str(bin(decimal))
    # eliminamos 0b
    binario=binario[2:]
    print(binario)
else:
    print('Por favor un decimal positivo')


