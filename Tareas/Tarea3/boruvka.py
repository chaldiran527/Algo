def inicializar_componentes(n):
    #Se inicializan los componentes como una lista vacia
    componentes = []
    for piv in range(n):#Se itera en el rango de n que es el numero de vertices del grafo
    #Se agrega a los componentes cada vertice como una lista individual
        componentes += [[piv]]
    return (componentes) #Se retorna los componentes inicializados con los valores de los vertices

def buscar_min_arista(grafo, componente, componentes):
    #Se inicializa la tupla de la arista minima en nulo
    min_arista = (None,None)
    #Se inicializa el peso minimo como un valor float en infinto
    min_peso = float('inf')
    #Se verifica si el componente es un componente individual y no un conjunto de componentes
    if (len(componente) == 1):
        vertice = componente[0]
        #Se hace un recorrido sobre los vertices adyacentes al vertice actual piv
        for piv in range(len(grafo[vertice])):
            #Se verifica si el vertice actual es mayor que cero y diferente al componente actual
            if ((grafo[vertice][piv] > 0)and (componentes[vertice] != componentes[piv])):
                #Se verifica que la arista tenga un peso menor al actual en min_peso
                if (grafo[vertice][piv] <= min_peso):
                    #Se actualiza el valor de min_peso
                    min_peso = grafo[vertice][piv]
                    #Se asigna el vertice y piv a la arista minima
                    min_arista = (vertice, piv)
    else:#En cado de que el componente sea una lista de componentes se itera sobre cada vertice del componente
        for vertice in componente:
        #Se hace un recorrido sobre los vertices adyacentes al vertice actual piv
            for piv in range(len(grafo[vertice])):
                if ((grafo[vertice][piv] > 0) and (componentes[vertice] != componentes[piv])):
                    # Se verifica que la arista tenga un peso menor al actual en min_peso
                    if (grafo[vertice][piv] < min_peso):
                        min_peso = grafo[vertice][piv]
                        min_arista = (vertice, piv)
    return min_arista #Se retorna la arista de peso minimo que conecta al vertice del componente en el grafo

def unir_componentes(arista, componentes,mst,grafo):
    #Se verifica que esta arista al reves no se encuentre en el mst
    if (arista[1], arista[0],grafo[arista[1]][arista[0]]) in mst:
        return componentes #Se retorna inmediatamente los componentes
    componente1 = []
    #Se itera sobre los componentes para buscar el primer vertice
    for componente in componentes:
        if arista[0] in componente:
            componente1 = componente
            break#Se rompe la iteracion
    if(componente1 == []):#Si no se encontro el vertice 1 en los compo se retorna inmediatamente
        return componentes

    componente2 = []
    #Se itera sobre los componentes para buscar el segundo vertice
    for componente in componentes:
        if arista[1] in componente:
            componente2 = componente
            break#Se rompe la iteracion
    if(componente2 == []):#Si no se encontro el vertice 2 en los compo se retorna inmediatamente
        return componentes
    #Se define al nuevo componente a agregar como la combinacion de los 2 componentes que se han encontrado
    nuevo_componente = componente1 + componente2
    #Se remueven de la lista de componentes los componentes del vertice 1 y 2 de la arista minima
    componentes.remove(componente1)
    componentes.remove(componente2)
    #Se agrega el nuevo componente a la lista
    componentes.append(nuevo_componente)
    return componentes#Se retorna la nueva lista de componentes.


def funcion_boruvka(grafo):
    #se incializa vacio el minimmum spanning tree
    mst = []
    componentes = inicializar_componentes(len(grafo))#Se inicializan la lista de los componentes
    while len(componentes) > 1:
        #Se inicializa vacia la lista de aristas que se van a agregar
        aristas = []
        #Iterar sobre los componentes
        for componente in componentes:
            #Se busca la arista de menor peso de el componente actual
            min_arista = buscar_min_arista(grafo, componente, componentes)

            #Verificar si se encontro la arista de peso minimo
            if(min_arista != (None, None)):
                #Se agrega la arista de menor peso a la lista de aristas
                aristas.append(min_arista)

        #Se itera sobre las aristas que se van a agregar
        for arista in aristas:
            #Se unen los componentes que se estan siendo conectados por la arista
            componentes = unir_componentes(arista, componentes,mst,grafo)
            #Se agrega esta arista con su peso respectivo al mst solo si no se encuentra en esta lista
            if(arista[1],arista[0],grafo[arista[1]][arista[0]]) not in mst:
                #se verifica si el vertice origen es mayor que el destino
                if(arista[0] > arista[1]):
                 arista = (arista[1],arista[0])
                 mst.append(arista + (grafo[arista[0]][arista[1]],))
                else:
                    mst.append(arista + (grafo[arista[0]][arista[1]],))
    return(mst)#Se retorna el arbol de recorrido minimo

if __name__ == "__main__":
    #Se inicializa el grafo no dirgido al cual se le calculara el mst
    grafo1 = [[0, 5, 7, 0]
             ,[5, 0, 6, 8]
             ,[7, 6, 0, 9]
             ,[0, 8, 9, 0]]
    #Se llama a la funcion para calcular el mst basado en el algoritmo de boruvka
    mst1 = funcion_boruvka(grafo1)
    #Se imprime el primer grafo y su mst respectivo
    print("Grafo 1:")
    for grafo in grafo1:
        print(f"\t{grafo}")
    print(f"Minimmum spanning tree del grafo 1 es: {mst1}")

    #Se realiza lo mismo con un segundo grafo
    grafo2 = [[0, 2, 0, 0]
             ,[2, 0, 24, 32]
             ,[0, 24, 0, 0]
             ,[0, 32, 0, 0]]
    mst2 = funcion_boruvka(grafo2)
    print("\nGrafo 2:")
    for grafo in grafo2:
        print(f"\t{grafo}")
    print(f"Minimmum spanning tree del grafo 2 es: {mst2}")