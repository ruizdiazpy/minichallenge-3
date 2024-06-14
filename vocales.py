def contar_vocales(cadena):
    # Definimos las vocales
    vocales = "aeiouAEIOU"
    # Inicializamos el contador
    contador = 0
    # Recorremos cada carácter en la cadena
    for caracter in cadena:
        # Si el carácter es una vocal, incrementamos el contador
        if caracter in vocales:
            contador += 1
    return contador

# Solicitamos la cadena al usuario
cadena = input("Introduce una cadena: ")
# Contamos las vocales
numero_vocales = contar_vocales(cadena)
# Mostramos el resultado
print(f"El número de vocales en la cadena es: {numero_vocales}")
