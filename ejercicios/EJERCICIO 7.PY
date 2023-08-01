def octal_to_decimal(octal_number):
    decimal_number = int(octal_number, 8)
    return decimal_number

if __name__ == "__main__":
    try:
        octal_input = input("Ingresa un número en base octal: ")
        decimal_output = octal_to_decimal(octal_input)
        print("El número en decimal es:", decimal_output)
    except ValueError:
        print("Error: Ingresa un número válido en base octal.")
