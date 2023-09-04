print("Adivina un numero entre el 1 al 100")
from random import randrange

randomNumber = randrange(101)
numero_ingresado = 0
intentos = 1
while randomNumber != numero_ingresado:
    print("Intento  " + str(intentos))
    numero_ingresado = int(input())
    if numero_ingresado > randomNumber:
        print("El numero es menor a : " + str(numero_ingresado))
        intentos = intentos + 1
    else:
        print("El numero es mayor a : " + str(numero_ingresado))
        intentos = intentos + 1
print("Correcto. Adivinaste al intento " + str(intentos))
