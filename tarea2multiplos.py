# Se solicita al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

#Los divisores a comprobar en este caso son: 2, 3, 5, 7, 9, 10, 11.

# Se debe verificar si el número es múltiplo de cada divisor (2, 3, 5, 7, 9, 10, 11) y mostrar el resultado
#Para cada numero se hace la comprobación
if numero % 2 == 0:       
    print(f"¿Es {numero} múltiplo de 2? Sí")    #Si el número dividido 2 da resto 0 imprime Si. en caso contrario imprime No
else:
    print(f"¿Es {numero} múltiplo de 2? No")    #En caso contrario imprime No.

if numero % 3 == 0:                             #Se repite lo mismo para cada divisor a comprobar:  ...3,5,7,9,10, 11.
    print(f"¿Es {numero} múltiplo de 3? Sí")
else:
    print(f"¿Es {numero} múltiplo de 3? No")

if numero % 5 == 0:
    print(f"¿Es {numero} múltiplo de 5? Sí")
else:
    print(f"¿Es {numero} múltiplo de 5? No")

if numero % 7 == 0:
    print(f"¿Es {numero} múltiplo de 7? Sí")
else:
    print(f"¿Es {numero} múltiplo de 7? No")

if numero % 9 == 0:
    print(f"¿Es {numero} múltiplo de 9? Sí")
else:
    print(f"¿Es {numero} múltiplo de 9? No")

if numero % 10 == 0:
    print(f"¿Es {numero} múltiplo de 10? Sí")
else:
    print(f"¿Es {numero} múltiplo de 10? No")

if numero % 11 == 0:
    print(f"¿Es {numero} múltiplo de 11? Sí")
else:
    print(f"¿Es {numero} múltiplo de 11? No")