def show_menu():
    print("\nMenu calculadora:")
    print("1. Sumar dos numeros")
    print("2. Restar dos numeros")
    print("3. Multiplicar dos numeros")
    print("4. Dividir dos numeros")
    print("5. Salir")

def read_option():
    while True:
        option = input("Introduce una accion: ")
        if option in ["1", "2", "3", "4", "5"]:
            return option
        else:
           print("Accion no valida, por favor introduce un numero entre 1 y 5") 

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    # para multiplicar sin usar *, usaremos sumas repetidas
    resultado = 0
    for _ in range(abs(b)):  # repite b veces
        resultado += abs(a)  # suma el valor absoluto de a
    
    # si uno de los numeros es negativo, el resultado es negativo
    if (a < 0 and b > 0) or (a > 0 and b < 0): 
        resultado = -resultado
    return resultado  

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    resultado = 0
    a_abs, b_abs = abs(a), abs(b)
    
    # mientras el dividendo sea mayor o igual al divisor
    while a_abs >= b_abs:
        a_abs -= b_abs # resta el valor del divisor del dividendo
        resultado += 1 # incrementa el resultado para contar cuantas veces se resta el divisor
        
    if (a < 0 and b > 0) or (a > 0 and b < 0): 
        resultado = -resultado
    return resultado      

def request_numbers():
    while True:
        try:
            num1 = int(input("\nIntroduce el primer numero: "))
            num2 = int(input("Introduce el segundo numero: "))
            return num1, num2
        except ValueError:
            print("Por favor, introduce numeros (ni letras ni simbolos)")

def perform_option(option):
    if option in ["1", "2", "3", "4"]:
        num1, num2 = request_numbers()
        if option == "1":
            print(f"Resultado de la suma: {addition(num1, num2)}")
        elif option == "2":
            print(f"Resultado de la resta: {subtraction(num1, num2)}")
        elif option == "3":
            print(f"Resultado de la multiplicacion: {multiplication(num1, num2)}")
        elif option == "4":
            print(f"Resultado de la division: {division(num1, num2)}")

    
def start_calculator():
    while True:
            show_menu()
            option = read_option()
            if option == "5":
                print("Saliendo del programa...")
                break
            else:
                perform_option(option)

start_calculator()            