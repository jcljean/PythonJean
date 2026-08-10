m = [[0]*3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        m[i][j] = int(input("Digite um número: "))

somaLinha = 0
for i in range(3):
    for j in range(3):
        somaLinha += m[i][j]
        print(m[i][j], end=" ")

    print("A soma da linha", i+1, "é:", somaLinha)
    somaLinha = 0

print("A soma total da matriz é:", sum(sum(m, [])))