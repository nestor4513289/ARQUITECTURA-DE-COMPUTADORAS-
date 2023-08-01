def base_nueve_a_decimal(numero_nueve):
    decimal = 0
    base = 9
    potencia = 0

    # Invertimos el número para facilitar la conversión
    numero_nueve = numero_nueve[::-1]

    for digito in numero_nueve:
        decimal += int(digito) * (base ** potencia)
        potencia += 1

    return decimal

def main():
    try:
        numero_nueve = input("Ingresa el número en base nueve: ")

        # Validamos que el número ingresado sea válido para base nueve (0-8)
        if not all(digito.isdigit() and 0 <= int(digito) < 9 for digito in numero_nueve):
            raise ValueError("El número ingresado no es válido para base nueve.")

        decimal = base_nueve_a_decimal(numero_nueve)
        print(f"El número en base decimal es: {decimal}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
