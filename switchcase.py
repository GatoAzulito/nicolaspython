
op=0
total=0
while op!=4:
    print("1- PC Ryzen $800k")
    print("2- LGTV $450k")
    print("3- Parlante $90k")
    op=int(input("Ingrese la opcion que desea comprar: "))
    match op:
        case 1:
            total += 800000 * 1.19
            print("Tiene que pagar", total)
        case 2:
            total += 450000 * 1.19
            print("Tiene que pagar", total)
        case 3:
            total += 90000 * 1.19
            print("Tiene que pagar", total)
        case 4:
            print("Total acumulado:", total)
        case _:
            print("Opcion no valida")

print("Fin del programa")