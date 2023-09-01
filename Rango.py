print("Cuantos valores ingresara ? ")
valores = input()
valor = [valores]

for i in range(0, len(valor), 1):
    input("Ingrese el valor " + str(i + 1) + ": ")
    valor = input()
