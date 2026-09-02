def suma(num1,num2):
    return str(num1 + num2)

def resta(num1,num2):
    return str(num1 - num2)

def divide(num1,num2):
    match num2:
        case 0:
            return "Error: División por cero!"
        case _:
            return str(num1 / num2)

def mul(num1,num2):
    return str(num1 * num2)

num1= float(input("Ingrese el primer operando"))
num2= float(input("Ingrese el segundo operando"))
op = str(input("Ingrese su operación. Operaciones disponibles: + , - , / , *"))

match op:
    case "+":
        print(suma(num1,num2))
    case "-":
        print(resta(num1,num2))
    case "/":
        print(divide(num1,num2))
    case "*":
        print(mul(num1,num2))
    case _:
        print("Operación Inválida!")