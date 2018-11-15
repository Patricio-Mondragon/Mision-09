#Autor Patricio Mondragon
#misión 9
def extraerPares(lista):
    listanueva = []
    for k in range(len(lista)):
        if lista[k] % 2 == 0:
            pass
        else:
            listanueva.append(lista[k])
    return listanueva


def extraerMayoresPrevio(lista1):
    listanueva = []
    for k in range(1, len(lista1)):
        if lista1[k] > lista1[k - 1]:
            listanueva.append(lista1[k])
    return listanueva


def intercambiarParejas(lista2):
    listanueva2 = []
    for k in range(len(lista2)):
        if k == 0:
            continue

        elif lista2[k] % 2 == 0:
            listanueva2.append(lista2[k])
            listanueva2.append(lista2[k - 1])
    if len(lista2) % 2 != 0:
        listanueva2.append(lista2[len(lista2) - 1])
    return listanueva2


def promediarCentro(lista5):
    listanueva5 = []

    for k in range(0, len(lista5)):
        listanueva5.append(lista5[k])
    listanueva5.remove(min(listanueva5))
    listanueva5.remove(max(listanueva5))

    promedio = sum(listanueva5) / len(listanueva5)

    return promedio


def intercambiarparejas(lista3):
    mayor = list.index(lista3, max(lista3[]))
    menor = list.index(lista3, min(lista3[]))
    lista3.insert(min(lista3),mayor)
    lista3.insert(max(lista3),menor)
    return lista3



def main():
    print("Ejercicio 1")
    lista = [1, 2, 3, 4, 5]
    listanueva = extraerPares(lista)
    print("La lista [1,2,3,4,5] regresa", listanueva)

    print("Ejercicio 2")
    lista1 = [6, 7, 8, 5, 4, 2]
    listanueva1 = extraerMayoresPrevio(lista1)
    print("La lista [6,7,8,5,4,2] regresa",listanueva1)
    print("Ejercicio 3")
    lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    listanueva2 = intercambiarParejas(lista2)
    print("La lista [1,2,3,4,5,6,7,8,9] regresa", listanueva2)
    print("Ejercicio 4")
    lista3 = [1,3,54,6,7,89]
    nuevalista3 = intercambiarparejas(lista3)
    print("La lista [1,3,54,6,7,89] regresa",nuevalista3 )
    print("Ejercicio 5")


    lista5 = [1, 2, 3, 56, 6, 4, 4]
    listanueva5 = promediarCentro(lista5)
    print("La lista [1,2,3,56,6,4,4] regresa",listanueva5)


main()
