def decimal_a_octal(numero_decimal):
    if numero_decimal == 0:
        return '0'

    numero_octal = ''
    while numero_decimal > 0:
        residuo = numero_decimal % 8
        numero_decimal //= 8
        numero_octal = str(residuo) + numero_octal

    return numero_octal

try:
    numero_decimal = int(input("Ingresa un número en base decimal: "))
    if numero_decimal < 0:
        raise ValueError("El número debe ser positivo.")
    
    numero_octal = decimal_a_octal(numero_decimal)
    print(f"El número en base octal es: {numero_octal}")

except ValueError as e:
    print("Error:", e)
