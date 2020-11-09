import random

def promedio(numeros):
    promedio_re = sum(numeros) / len(numeros)
    promedio = promedio_re
    return promedio

def ordenar(numeros):
    orden = numeros.sort()
    orden = ordenar
    return orden

def lista_aleatoria(inicio, fin, cantidad):
    lista = []
    for i in range(inicio, cantidad+1):
        numero = random.randrange(inicio, fin+1)
        lista.append(numero)
    return lista

def count(numeros):
    contador = numeros.count()
    contar = contador
    return contar

def contar(lista_numeros, valor):
    contador = lista_numeros.count(valor)
    return contador
