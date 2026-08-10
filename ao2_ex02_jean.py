v = [0]*6
maiorMedia = 0
menorMedia = 0

v[0] = float(input("Digite sua nota: "))
maior = v[0]
menor = v[0]


for i in range(1,6):
    v[i] = float(input("Digite sua nota: "))

    if v[i] >= maior:
        maior = v[i]

    if v[i] < menor:
        menor = v[i]

print ("A maior nota é:", maior)
print ("A menor nota é:", menor)

media = sum(v)/len(v)
print ("A média da turma é:", media)

for i in range(6):

    if v[i] >= media:
        maiorMedia += 1

    elif v[i] < media:
        menorMedia += 1

print ("A quantidade de alunos com nota maior ou igual a média é:", maiorMedia)
print ("A quantidade de alunos com nota menor que a média é:", menorMedia)
