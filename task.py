# for i in "Gatoazulito":
#     print(i)
c_vowels=0
c_consonants=0
name=str(input("Ingrese su nombre: "))
for i in name:
    if i.lower() in "aeiouáéíóúü":
        print(i)
        c_vowels=c_vowels+1
    elif i==" ":
        print("")
    else:
        c_consonants=c_consonants+1
print("La cantidad de vocales es: ", c_vowels)
print("La cantidad de consonantes es: ", c_consonants)