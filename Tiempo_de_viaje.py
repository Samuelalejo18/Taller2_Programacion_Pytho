print("Cuantos tramos de viaje realizo? ")
Tramos = int(input())
Duracion = []

suma = 0
for i in range(Tramos):
    print("Ingrese el valor " + str(i + 1) + ": ")
    Duracion.append(int(input()))
    suma += Duracion[i]

horas = suma // 60
minutos = suma % 60

if minutos >= 10:
    print("El tiempo total de viaje : " + str(horas) + ":" + str(minutos) + " horas")
else:
    print("El tiempo total de viaje : " + str(horas) + ": 0" + str(minutos) + " horas")
