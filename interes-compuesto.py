import math

#input

C=int(input("Digite el valor de la capital inicial: "))

#processing

N = 0

d = 2 * C

while (C<=d):
    C=1.05 * C
    N=N + 1

#output
print("Los meses serian: " + str(N))

#FIN
