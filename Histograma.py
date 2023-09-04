print("Ingrese valores enteros (terminará cuando ingrese '0')")
positivos = 0
negativos = 0

while True:
    valor = int(input())
    if valor == 0:
        break
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1

resultados_positivos = "positivos: " + "*" * positivos
resultados_negativos = "negativos: " + "*" * negativos

print(resultados_positivos)
print(resultados_negativos)
