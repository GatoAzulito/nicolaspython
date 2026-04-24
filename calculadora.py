num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
op=0
while op!=5:
    print("1- Suma")
    print("2- Resta")
    print("3- Multiplicacion")
    print("4- Division")
    print("5- Salir")
    op=int(input("Ingrese la operacion que desea realizar: "))
    match op:
        case 1:
            print("El resultado de la suma es:", num1 + num2)
        case 2:
            print("El resultado de la resta es:", num1 - num2)
        case 3:
            print("El resultado de la multiplicacion es:", num1 * num2)
        case 4:
            print("El resultado de la division es:", num1 / num2)
        case 5:
            print("Fin del programa")
