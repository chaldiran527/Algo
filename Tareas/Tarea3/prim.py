#Se retorna el minimo indice asociado a la llave
def buscar_min_llave(llave, booleanos_mst, vertices):
    # Se inicializa el valor minimo
    min_llave = 2**31 - 1
    #Se itera en base a la cantidad de vertices del grafo
    for ver in range(vertices):
        if llave[ver] < min_llave and booleanos_mst[ver] == False:
            min_llave = llave[ver]
            min_indice = ver
    return(min_indice)#Se retorna el minimo indice de la llave


def funcion_prim(grafo):
    #Valores de los pesos minimos de las aristas
    llave = [2**31 - 1] * len(grafo)
    mst = [0] * len(grafo)
    #El vertice cero es el primero en elegirse
    llave[0] = 0
    #Se inicializa la lista en la que se determina si el vertice pertenece al mst
    booleanos_mst = [False] * len(grafo)

    #Se inicializa el primer elemento en -1 para indicar que el vertice cero es la raiz del minimmum spanning tree
    mst[0] = -1
    for i in range(len(grafo)):
        #Escoger la minima distancia para el vertice
        n = buscar_min_llave(llave,booleanos_mst,len(grafo))

        #Ingresar el vertice minimo al conjunto de booleanos del mst
        booleanos_mst[n] = True;
        for m in range(len(grafo)):
        #Se verifica y agrega si el vertice adyacente mas cercano no se encuentra en el mst
            if(grafo[n][m] > 0 and booleanos_mst[m] == False and llave[m] > grafo[n][m]):
                llave[m] = grafo[n][m]
                mst[m] = n
    #Se retorna el mst
    return mst


if __name__ == "__main__":
    #Se inicializa el grafo del mst a calcular ysando prim
    grafo1 = [[0, 5, 7, 0]
             ,[5, 0, 6, 8]
             ,[7, 6, 0, 9]
             ,[0, 8, 9, 0]]

    mst = funcion_prim(grafo1)
    #Se imprimen las aristas y pesos del mst
    print("El mst resultante del grafo 1 es: ")
    for i in range(1, len(grafo1)):
        #Se imprime el vertice respectivo mas cercano a cada vertice del mst con su peso
        print(f"\t\t{mst[i]} -> {i}:  {grafo1[i][mst[i]]}  ")

    grafo2 = [[0, 2, 0, 0]
             ,[2, 0, 24, 32]
             ,[0, 24, 0, 0]
             ,[0, 32, 0, 0]]

    mst = funcion_prim(grafo2)
    #Se imprimen las aristas y pesos del mst
    print("\nEl mst resultante del grafo 2 es: ")
    for i in range(1, len(grafo2)):
        #Se imprime el vertice respectivo mas cercano a cada vertice del mst con su peso
        print(f"\t\t{mst[i]} -> {i}:  {grafo2[i][mst[i]]}  ")