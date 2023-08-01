def decimal_a_base(num_decimal, base):
    # Función para convertir un número decimal a una base específica
    if num_decimal == 0:
        return '0'
    cifras = "0123456789ABCDEF"
    num_base = ""
    while num_decimal > 0:
        resto = num_decimal % base
        num_base = cifras[resto] + num_base
        num_decimal = num_decimal // base
    return num_base

def base_a_decimal(num_base, base):
    # Función para convertir un número de una base específica a decimal
    cifras = "0123456789ABCDEF"
    num_decimal = 0
    exp = len(num_base) - 1
    for digito in num_base:
        num_decimal += cifras.index(digito) * (base ** exp)
        exp -= 1
    return num_decimal

def main():
    try:
        # Paso 1: Obtener el número y la base de origen del usuario
        numero = input("Ingrese el número que desea convertir: ")
        base_origen = int(input("Ingrese la base de origen del número (2-16): "))

        # Paso 2: Obtener la base a la que se quiere convertir el número
        base_destino = int(input("Ingrese la base a la que desea convertir el número (2-16): "))

        # Paso 3: Convertir el número de la base de origen a decimal
        decimal = base_a_decimal(numero, base_origen)

        # Paso 4: Convertir el número decimal a la base deseada
        resultado = decimal_a_base(decimal, base_destino)

        print(f"El número {numero} en base {base_origen} es igual a {resultado} en base {base_destino}.")
    except ValueError:
        print("Error: Asegúrese de ingresar un número válido y bases entre 2 y 16.")

if __name__ == "__main__":
    main()
