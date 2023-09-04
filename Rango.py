print("Cuantos valores ingresara ? ")
valores = int(input())
valor = []

for i in range(valores):
    print("Ingrese el valor " + str(i+1) + ": ")
    valor.append(int(input()))

mayor = menor = valor[0]

for i in range(len(valor)):
    if valor[i] > mayor:
        mayor = valor[i]
    if valor[i] < menor:
        menor = valor[i]

rango = mayor - menor
print("El rango es: " + str(rango))
