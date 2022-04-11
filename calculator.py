def calculator():
  print("RUNNING: Calculator")
  prompt = input("OPTIONS (choose one):\nAddition (1)\nSubtraction (2)\nMultiplication (3)\nDivision (4)\nExponent (5)\nInt. Division (6)\nModulus (7)\n\n")
  if prompt == "1":
    print("ADDITION\n")
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
    result = num1 + num2
    print(f"\n{num1} + {num2} = {result}")
    
  elif prompt == "2":
    print("SUBTRACTION\n")
    num1 = float(input("Subtrahend: "))
    num2 = float(input("Minus: "))
    result = num1 - num2
    print(f"\n{num1} - {num2} = {result}")

  elif prompt == "3":
    print("MULTIPLICATION\n")
    num1 = float(input("Factor 1: "))
    num2 = float(input("Factor 2: "))
    result = num1 * num2
    print(f"\n{num1} * {num2} = {result}")

  elif prompt == "4":
    print("DIVISION\n")
    num1 = float(input("Dividend: "))
    num2 = float(input("Divisor: "))
    result = num1 / num2
    print(f"\n{num1} / {num2} = {result}")

  elif prompt == "5":
    print("EXPONENTIATION\n")
    num1 = float(input("Number: "))
    num2 = int(input("Power: "))
    result = num1 ** num2
    print(f"\n{num1} ** {num2} = {result}")

  elif prompt == "6":
    print("INTEGER DIVISION\n")
    num1 = float(input("Dividend: "))
    num2 = float(input("Divisor: "))
    result = num1 // num2
    print(f"\n{num1} // {num2} = {result}")

  elif prompt == "7":
    print("MODULUS (finds the remainder of a division)")
    num1 = float(input("Dividend: "))
    num2 = float(input("Divisor: "))
    result = num1 % num2
    print(f"\n{num1} / {num2} = {result} (remainder: {result})")
    
