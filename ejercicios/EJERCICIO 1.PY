def decimal_to_base_three(decimal_num):
    if decimal_num == 0:
        return '0'
    
    base_three_num = ''
    while decimal_num > 0:
        remainder = decimal_num % 3
        base_three_num = str(remainder) + base_three_num
        decimal_num //= 3
    
    return base_three_num

def main():
    try:
        decimal_input = int(input("Ingresa un número en base decimal: "))
        if decimal_input < 0:
            raise ValueError("El número debe ser un entero positivo.")
        
        base_three_num = decimal_to_base_three(decimal_input)
        print(f"El número en base tres es: {base_three_num}")
    
    except ValueError as e:
        print(f"Error: {e}. Por favor, ingresa un número entero positivo.")

if __name__ == "__main__":
    main()
