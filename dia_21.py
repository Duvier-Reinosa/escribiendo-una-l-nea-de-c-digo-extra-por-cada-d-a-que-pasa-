def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convertir_temperaturas(lista, tipo):
    if tipo == "C":
        return [celsius_a_fahrenheit(temp) for temp in lista]
    elif tipo == "F":
        return [fahrenheit_a_celsius(temp) for temp in lista]
    else:
        raise ValueError("Tipo debe ser 'C' o 'F'.")

temperaturas = [0, 10, 20, 30, 40, 50]
tipo_conversion = "C"

resultado = convertir_temperaturas(temperaturas, tipo_conversion)
unidad = "Fahrenheit" if tipo_conversion == "C" else "Celsius"

print(f"Temperaturas convertidas a {unidad}: {resultado}")