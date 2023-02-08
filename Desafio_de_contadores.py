"""
0 10
1  9
2  8
3  7
4  6
5  5
6  4
7  3
8  2
9  1
10 0
"""

lista = list(range(0,9))
print(lista)

contador_crescente = 0
contador_decrescente = 10

for numero in lista:
    print(contador_crescente, contador_decrescente)
    contador_crescente += 1
    contador_decrescente -= 1

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)