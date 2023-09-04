print("Ingresa numero:")
numero = int(input())

valor = str(numero)
valor_invertido = ""

for i in range(len(valor) - 1, -1, -1):
    valor_invertido += valor[i]

if int(valor_invertido) == numero:
    print("el numero es palindromo")
else:
    print("el numero no es palindromo")
