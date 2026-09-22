N = 6
v = []

print("Ingrese 6 valores: ")
for i in range(N):
    v.append(int(input()))

# Mostrar el arreglo del ultimo al primero
for i in range(N - 1, -1, -1):
    print(v[i], end="")
    if i > 0:
        print(" ", end="")
print()