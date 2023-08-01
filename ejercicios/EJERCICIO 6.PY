def decimal_to_base_seven(decimal_num):
    if decimal_num == 0:
        return '0'  # Caso especial cuando el número es cero

    base_seven_num = ''
    is_negative = False

    if decimal_num < 0:
        is_negative = True
        decimal_num = abs(decimal_num)

    while decimal_num > 0:
        remainder = decimal_num % 7
        base_seven_num = str(remainder) + base_seven_num
        decimal_num = decimal_num // 7

    if is_negative:
        base_seven_num = '-' + base_seven_num

    return base_seven_num


if __name__ == "__main__":
    try:
        decimal_input = int(input("Ingresa un número decimal: "))
        base_seven_result = decimal_to_base_seven(decimal_input)
        print(f"El número en base siete es: {base_seven_result}")
    except ValueError:
        print("Error: Ingresa un número decimal válido.")
