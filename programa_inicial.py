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

def leer_numero():
    valido = False
    while not valido:
        try:
            num= float(input())
            valido = True
        except ValueError:
            print("Eso no es un número válido! Ingrese un número válido: ")
    return num

print("Ingrese el primer operando: ")
num1= leer_numero()
print("Ingrese el segundo operando: ")
num2= leer_numero()
op = input("Ingrese su operación. Operaciones disponibles: + , - , / , * \n")

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