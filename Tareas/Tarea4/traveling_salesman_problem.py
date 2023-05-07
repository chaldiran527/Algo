def funcion_tsp(grafo, ver, pos, n, cont, costo, recorrido):
    #Cont tiene la cantidad de vertices visitados
    #Se verifica en cont si se han visitado todos los vertices y si la posicion del vertice actual esta conectado al vertice inicial
    if (cont == n and grafo[pos][0]):
        recorrido.append(0) #Se agrega el vertice inicial al recorrido
        #Se retorna el costo y el recorrido
        return (costo + grafo[pos][0], recorrido)

    #Se inicializa el costo minimo con un valor masivo
    costo_min = float('inf')
    #Se itera sobre todos los vertices del grafo
    for i in range(n):#n es el largo del grafo, es decir el numero de vertices
       #Se verifica si el vertice no ha sido recorrido y si esta conectado al vertice de la posicion actual
        if (ver[i] == False and grafo[pos][i]):
            #Se marca este vertice como visitado
            ver[i] = True
            recorrido.append(i)#Se agrega al recorrido actual el vertice
            #Se llama recursivamente en backtracking a esta funcion con el vertice actual
            #Esta funcion recursiva devuelve el costo y recorrido minimo desde el vertice nuevo hasta el final del recorrido
            costo_nuevo, recorrido_nuevo = funcion_tsp(grafo, ver, i, n, cont + 1, costo + grafo[pos][i], recorrido)
            #Se actualiza el costo minimo y el recorrido
            if (costo_nuevo < costo_min):#Se verifica que el costo nuevo sea menor que el costo minimo anterior
                costo_min = costo_nuevo
                recorrido_final = recorrido_nuevo
            #Se marca este vertice como no visitado
            ver[i] = False
            recorrido.pop()#Se quita el vertice del recorrido
    #Se retorna el costo y recorrido minimo
    return (costo_min, recorrido_final)

#Main del programa
if __name__ == '__main__':
    grafo = [[0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]]
    n = len(grafo)

    # Arreglo booleano de los vertices que han sido visitados
    ver = [False for i in range(n)]
    ver[0] = True #El primer vertice se marca como visitado


    #Se llama a la funcion para calcular el recorrido minimo y el costo minimo
    costo, recorrido = funcion_tsp(grafo, ver, 0, n, 1, 0, [0])

    print(f"Grafo: ")
    for i in range(len(grafo)):
        print(f"\t{grafo[i]}")
    print(f"Costo minimo: {costo}")
    print(f"Recorrido: {recorrido}")
