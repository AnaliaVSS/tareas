# Temperatura en Celsius. Variable celsius. Ingresa el valor solicitado al usuario.
celsius = float(input("Ingrese un valor correspondiente a la temperatura en °C (grados celsius): " ))
# Conversión de Celsius a Fahrenheit. Utilizamos la formula correspondiente: °F = (°C * 9/5) +32. °F=(18 * 1.8) + 32
fahrenheit = (celsius * 9/5) + 32

# Conversión de Celsius a Kelvin. Utilizamos el valor ingrgesado por el usuario en grados Celsius  y le sumamos 273.15.
kelvin = celsius + 273.15

# Salida. Imprimir los resultados.
print(f"{celsius} °C equivalen a {fahrenheit} °F")
print(f"{celsius} °C equivalen a {kelvin} °K")