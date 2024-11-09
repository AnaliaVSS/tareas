# Función para verificar si un número es primo
def es_primo(numero):
    if numero < 2:    # Si el número es menor que 2, no puede ser primo
        return False
    for i in range(2, int(numero ** 0.5) + 1): # Itera desde 2 hasta la raíz cuadrada del número para buscar divisores
        if numero % i == 0: # Si el número es divisible por 'i', no es primo
            return False
    return True  # Si no encontró ningún divisor, el número es primo

# Función para contar la cantidad de números primos en una lista
def contar_primos(lista):
    contador = 0 # Inicializa el contador de números primos
    
    for numero in lista:  # Recorre cada número de la lista
        if es_primo(numero):
            contador += 1
    return contador

# Función main que integra las anteriores y permite ingresar un número
def main():
    # Solicitar al usuario que ingrese un número para verificar si es primo
    try:
        numero_verificar = int(input("Ingresa un número para verificar si es primo: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return

    if es_primo(numero_verificar):
        print(f"El número {numero_verificar} es primo.")
    else:
        print(f"El número {numero_verificar} no es primo.")

    # Ejemplo de lista de números
    lista_numeros = [2, 3, 4, 5, 10, 11, 13, 17, 18, 19, 20, 23,56, 34, 7]

    # Contar la cantidad de números primos en la lista
    cantidad_primos = contar_primos(lista_numeros)
    print(f"La lista contiene {cantidad_primos} números primos.")

# Ejecutar el main
if __name__ == "__main__":
    main()