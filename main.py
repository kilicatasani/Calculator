import math

def calculate_trig():
    print("\n--- Scientific Calculator Mode ---")
    print("Supported operations:")
    print("  Arithmetic: +, -, *, /, %, **")
    print("  Trigonometry: sin, cos, tan (requires degree input)")
    print("  Inverse Trig: asin, acos, atan (result is in degrees)")
    print("  Other: sqrt (square root)")
    
    expression = input("Enter the calculation: ").lower().strip()
    parts = expression.split()
    
    if len(parts) == 2:
        operator = parts[0]
        try:
            value = float(parts[1])
        except ValueError:
            print("Error: Invalid number input.")
            return
        if operator in ('sin', 'cos', 'tan'):
            rad_value = math.radians(value)
            
            if operator == 'sin':
                result = math.sin(rad_value)
            elif operator == 'cos':
                result = math.cos(rad_value)
            elif operator == 'tan':
                if value % 180 == 90:
                     print(f"Result: {operator}({value}) is Undefined (or very large).")
                     return
                result = math.tan(rad_value)
                
            print(f"Result: {operator}({value}°) = {result:.4f}")

        elif operator in ('asin', 'acos', 'atan'):
            if operator == 'asin':
                if not -1 <= value <= 1:
                    print("Error: asin input must be between -1 and 1.")
                    return
                result_rad = math.asin(value)
            elif operator == 'acos':
                if not -1 <= value <= 1:
                    print("Error: acos input must be between -1 and 1.")
                    return
                result_rad = math.acos(value)
            elif operator == 'atan':
                result_rad = math.atan(value)
      
            result = math.degrees(result_rad)
            print(f"Result: {operator}({value}) = {result:.2f}°")
        elif operator == 'sqrt':
            if value < 0:
                print("Error: Cannot calculate the square root of a negative number.")
                return
            result = math.sqrt(value)
            print(f"Result: sqrt({value}) = {result:.4f}")
            
        else:
            print("Error: Invalid single-operand function or command.")
            
    elif len(parts) == 3:
        try:
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
        except ValueError:
            print("Error: Invalid number input.")
            return

        result = 0
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero!")
                return
        elif operator == '%':
            result = num1 % num2
        elif operator == '**':
            result = num1 ** num2
        else:
            print("Error: Invalid arithmetic operator.")
            return

        print(f"Result: {num1} {operator} {num2} = {result:.4f}")

    else:
        print("Error: Invalid expression format. Use 'sin 90' or '5 + 3'.")

if __name__ == "__main__":
    calculate_trig()
