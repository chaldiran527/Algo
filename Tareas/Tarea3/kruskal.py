#Funcion para encontrar al vertice padre usando recursion
def buscar_vertice_padre(vertice_padre, indice):
    if vertice_padre[indice] != indice:
        vertice_padre[indice] = buscar_vertice_padre(vertice_padre, vertice_padre[indice])
    return vertice_padre[indice]


#Union de ambos conjuntos de los dos vertices enviados por parametro
def union(vertice_padre, nivel, vertice1, vertice2):
    #Se define la raiz de los conjuntos que se van a unir de los vertices
    vertice1_raiz = buscar_vertice_padre(vertice_padre, vertice1)
    vertice2_raiz = buscar_vertice_padre(vertice_padre, vertice2)

    #Se unen los conjuntos en base al nivel de la altura del vertice
    if nivel[vertice1_raiz] < nivel[vertice2_raiz]:#Se verifica el caso del vertice 1 cuando es menor
        vertice_padre[vertice1_raiz] = vertice2_raiz
    elif nivel[vertice1_raiz] > nivel[vertice2_raiz]:#vertice 1 es mayor
        vertice_padre[vertice2_raiz] = vertice1_raiz
    else:#sino se incrementa en uno el nivel de la raiz del vertice
        vertice_padre[vertice2_raiz] = vertice1_raiz
        nivel[vertice1_raiz] += 1

def funcion_kruskal(graph):
    #Se inicializan la variable del numero de vertices basado en el largo del grafo
    vertices = len(graph)
    #Se define a vertice_padre y el nivel en base al numero de vertices
    vertice_padre = []
    nivel = [0] * len(graph)
    for i in range(vertices):
        vertice_padre += [i]#Se agrega cada indice en el rango de los vertices del grafo
    mst = []#Se inicializa el mst vacio
    #Variables e,i sirven para iterar como contadores
    i = 0
    e = 0
#Mientras sea menor que el numero de vertices menos uno
    while (e < vertices - 1):
        #Se inicializa la arits minima como un float infinito
        min_arista = float('inf')
        u, v = -1, -1
        #Se itera sobre los vertices del grafo
        for i in range(vertices):
            for j in range(vertices):
                #Si el peso de la arista de los vertices actuales es menor que la arista minima
                if graph[i][j] < min_arista:
                    min_arista = graph[i][j]#Se actualiza el valor de la arista minima
                    u, v = i, j#U y v se igualan a los contadores i,j

    #Se busca a los vertices padre de los vertices de la arista minima
        vertice1 = buscar_vertice_padre(vertice_padre, u)
        vertice2 = buscar_vertice_padre(vertice_padre, v)

    #Si son diferentes los vertices
        if (vertice1 != vertice2):
            e += 1#Se incrementa en uno al contador e y se agrega la arista al mst con su peso minimo
            mst.append((u, v, min_arista))
            union(vertice_padre, nivel, vertice1, vertice2)
        graph[u][v] = graph[v][u] = float('inf')
    #Se retorna el mst con las aristas y su peso respectivo
    return mst


if __name__ == "__main__":
#Se inicializa el primer grafo
    grafo1 = [[0, 5, 7, 0]
        , [5, 0, 6, 8]
        , [7, 6, 0, 9]
        , [0, 8, 9, 0]]

#Se calcula el mst del primer grafo con el algoritmo de kruskal
    mst1 = funcion_kruskal(grafo1)
    print(f"Minimum spanning tree resultante del grafo 1 es: {mst1}")

#Se inicializa el segundo grafo
    grafo2 = [[0, 2, 0, 0]
        , [2, 0, 24, 32]
        , [0, 24, 0, 0]
        , [0, 32, 0, 0]]
#Se calcula el mst del segundo grafo con el algoritmo de kruskal
    mst2 = funcion_kruskal(grafo2)
    print(f"\nMinimum spanning tree resultante del grafo 2 es: {mst2}")
