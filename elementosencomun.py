# Función que verifica si dos listas tienen al menos un elemento en común
def tienen_elemento_comun(lista1, lista2):
    # Convierte la primera lista en un conjunto para una búsqueda eficiente
    conjunto_lista1 = set(lista1)

    # Recorre cada elemento en la segunda lista
    for elemento in lista2:
        # Verifica si el elemento está en el conjunto de la primera lista
        if elemento in conjunto_lista1:
            return True  # Si encuentra un elemento en común, retorna True

    # Si no encuentra elementos en común, retorna False
    return False

# Función principal que solicita al usuario las dos listas
def main():
    # Solicitar al usuario que ingrese la primera lista de números
    entrada_lista1 = input("Ingresa los números de la primera lista separados por espacios: ")

    # Solicitar al usuario que ingrese la segunda lista de números
    entrada_lista2 = input("Ingresa los números de la segunda lista separados por espacios: ")

    try:
        # Convierte las entradas del usuario en listas de números enteros
        lista1 = list(map(int, entrada_lista1.split()))
        lista2 = list(map(int, entrada_lista2.split()))
    except ValueError:
        # Maneja el caso en que el usuario no ingrese números válidos
        print("Por favor, ingresa solo números enteros separados por espacios.")
        return  # Termina la función si hay un error en la conversión

    # Llama a la función tienen_elemento_comun y guarda el resultado
    resultado = tienen_elemento_comun(lista1, lista2)

    # Imprime el resultado
    print(f"Las listas tienen al menos un elemento en común: {resultado}")

# Ejecutar la función principal si el archivo se ejecuta directamente
if __name__ == "__main__":
    main()