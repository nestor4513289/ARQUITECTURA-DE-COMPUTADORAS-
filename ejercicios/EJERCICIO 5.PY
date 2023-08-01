def decimal_to_base_six(decimal_number):
    if decimal_number == 0:
        return '0'

    base_six_digits = ''
    while decimal_number > 0:
        remainder = decimal_number % 6
        base_six_digits = str(remainder) + base_six_digits
        decimal_number //= 6

    return base_six_digits

def main():
    try:
        decimal_input = int(input("Ingresa un número decimal: "))
        if decimal_input < 0:
            raise ValueError("El número decimal debe ser no negativo.")
        
        base_six_number = decimal_to_base_six(decimal_input)
        print(f"El número en base seis es: {base_six_number}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
