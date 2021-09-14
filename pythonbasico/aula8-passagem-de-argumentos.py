import sys

argumentos = sys.argv


def soma(n1, n2):
    return float(n1) + float(n2)


def sub(n1, n2):
    return float(n1) - float(n2)


resp = "null"

if argumentos[1] == "soma":
    resp = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "sub":
    resp = sub(argumentos[2], argumentos[3])

print("Resultado:", resp)
