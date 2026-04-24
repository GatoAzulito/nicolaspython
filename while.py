# cont=1
# while cont<4:
#     print(f"Contador = {cont}")
#     cont+=1

# pin=3535
# code=int(input("Ingrese el pin: "))
# while code!=pin:
#     print("Pin incorrecto, intente de nuevo")
#     code=int(input("Ingrese el pin: "))

num=int(input("Ingrese un numero: "))
cont=1
while cont<=10:
    print(f"{num} x {cont} = {num*cont}")
    cont+=1
print("Con +")
print(str(num) + " x " + str(cont) + " = " + str(num * cont))
print("Con ,")
print(num, "x", cont, "=", num*cont)
