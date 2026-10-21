import math

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def division(a, b):
  return a / b

def floor_division(a, b):
  return a // b

def power(base, exponent):
  return base ** exponent

def sqrt(a):
  return math.sqrt(a)


def get_numbers():
  a = int(input("Enter the first number: "))
  b = int(input("Enter the second number: "))
  return a, b

def get_number():
  return int(input("Enter a number: "))


def main():
  while True:
    choice = int(input("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Floor division
6. Power
7. Square root
8. Exit

Enter your choice: """))

    match choice:
      case 1:
        a, b = get_numbers()
        print(f"Addition: {add(a, b)}")

      case 2:
        a, b = get_numbers()
        print(f"Subtraction: {subtract(a, b)}")

      case 3:
        a, b = get_numbers()
        print(f"Product: {multiply(a, b)}")

      case 4:
        a, b = get_numbers()
        if b == 0:
          print("Cannot divide by zero.")
        else:
          print(f"Quotient: {division(a, b)}")

      case 5:
        a, b = get_numbers()
        if b == 0:
          print("Cannot divide by zero.")
        else:
          print(f"Floor division: {floor_division(a, b)}")

      case 6:
        base, exponent = get_numbers()
        print(f"power:{power(base, exponent)}")

      case 7:
        a = get_number()
        if a < 0:
          print("Cannot calculate a real square root of a negative number.")
        else:
          print(f"Square root: {sqrt(a)}")

      case 8:
        print("Thank you for using the calculator!")
        break

      case _:
        print("Enter a valid option.")


if __name__ == "__main__":
    main()
