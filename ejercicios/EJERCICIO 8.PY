def hexadecimal_a_decimal(hexadecimal):
    try:
        decimal = int(hexadecimal, 16)
        return decimal
    except ValueError:
        print("Error: El número hexadecimal ingresado no es válido.")
        return None

if __name__ == "__main__":
    numero_hexadecimal = input("Ingresa un número en formato hexadecimal: ")

    decimal_resultado = hexadecimal_a_decimal(numero_hexadecimal)
    if decimal_resultado is not None:
        print("El número decimal equivalente es:", decimal_resultado)
