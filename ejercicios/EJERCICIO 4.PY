def decimal_to_hexadecimal(decimal_num):
    hexadecimal_chars = "0123456789ABCDEF"
    result = ""

    if decimal_num == 0:
        return "0"

    while decimal_num > 0:
        remainder = decimal_num % 16
        result = hexadecimal_chars[remainder] + result
        decimal_num //= 16

    return result


if __name__ == "__main__":
    try:
        decimal_input = int(input("Ingrese un número decimal: "))
        if decimal_input < 0:
            raise ValueError("El número debe ser un entero positivo.")
        
        hexadecimal_output = decimal_to_hexadecimal(decimal_input)
        print("El número en hexadecimal es:", hexadecimal_output)

    except ValueError as e:
        print("Error:", e)
