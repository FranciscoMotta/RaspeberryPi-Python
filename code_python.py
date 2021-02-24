print("This is my first script")
string1 = "hola"
string2 = "mundo"

# Cadenas con operadores y multiplicadores

print(string1 + " " + string2 + '!'*4)
division = 2/3

import math #Importamos la libreria de matematicas

print("2 entre 3 es: {}" .format(division))
print("2 entre 3 es: {: f}" .format(division)) # Secoloca como flotante

string3 = "mas"
print("Se puede imprimir {0} de una variable, pi: {1}, eso hace {2} varaibles" .format(string3,math.pi,3))

for num in range(2,10,1):
    print("El numero es: ", num)

for numero2 in range(0, 10, 1):
    print("Las potencias de 2 son: ", 2**numero2)

a = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1] #Creamos un array

for elemento in a:
    if elemento == max(a):
        print(elemento*'=')
        print("Encontramos el número más grande")
    print(elemento*'=')