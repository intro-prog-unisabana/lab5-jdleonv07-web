def list_shift(numeros, valor):
    for i in range(len(numeros)):
        numeros[i] += (valor)
def calc_avg(numeros):
    return sum(numeros) / len(numeros)
def print_normalized(lista):
    print(lista)