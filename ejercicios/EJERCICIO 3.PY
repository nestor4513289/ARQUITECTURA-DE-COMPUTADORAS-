def decimal_a_base_nueve(numero_decimal):
    if numero_decimal == 0:
        return "0"

    numero_base_nueve = ""
    while numero_decimal > 0:
        residuo = numero_decimal % 9
        numero_base_nueve = str(residuo) + numero_base_nueve
        numero_decimal //= 9

    return numero_base_nueve

if __name__ == "__main__":
    try:
        numero_decimal = int(input("Ingresa un número decimal: "))
        if numero_decimal < 0:
            print("Por favor, ingresa un número decimal positivo.")
        else:
            numero_base_nueve = decimal_a_base_nueve(numero_decimal)
            print(f"El número en base 9 es: {numero_base_nueve}")
    except ValueError:
        print("Error: Ingresa un número decimal válido.")
