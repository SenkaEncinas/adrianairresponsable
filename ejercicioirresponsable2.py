palabra = input("Ingrese una palabra: ")

# Recorrer la palabra desde la ultima letra hasta la primera
invertida = ""
for i in range(len(palabra) - 1, -1, -1):
    invertida += palabra[i]

print("Al reves:", invertida)

# Extra: ver si es palindromo
if palabra.lower() == invertida.lower():
    print("Es palindromo")
else:
    print("No es palindromo")