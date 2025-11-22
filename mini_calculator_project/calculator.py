#AUTHOR: HARSH SINGH 
#ROLL NO: 2501730400
#SECTION: A

# A simple calculator module with basic arithmetic operations 

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

def main():
    print("=== Simple Calculator ===")
    while True:
        try:
            a = float(input("Enter first number (or 'q' to quit): ").strip())
        except ValueError:
            print("Exiting calculator. Goodbye.")
            break
        try:
            b = float(input("Enter second number: ").strip())
        except ValueError:
            print("Invalid number. Restarting.")
            continue
        op = input("Choose operation (+, -, *, /): ").strip()
        try:
            if op == "+":
                print("Result:", add(a, b))
            elif op == "-":
                print("Result:", subtract(a, b))
            elif op == "*":
                print("Result:", multiply(a, b))
            elif op == "/":
                print("Result:", divide(a, b))
            else:
                print("Invalid operation. Use +, -, *, or /.")
        except Exception as e:
            print("Error:", e)
        print("-" * 30)

if __name__ == '__main__':
    main()
