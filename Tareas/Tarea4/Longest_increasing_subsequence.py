def funcion_lis(arr):
    """
    Funcion que calcula la sub-secuencia mayor de la sucesion ingresada por parametro
    param arr: Arreglo de los valores a calcular su sub-secuencia mayor
    """
    n = len(arr)  # largo del arreglo a calcular lis
    tabla_d = [1] * n  # lista programacion dinamica del mayor largo de la secuencia
    tabla_p = [-1] * n

    for i in range(1, n):  # i<=>k
        # length[i] = 1 esto se usaba cuando no se inicializaba cada valor en 1
        for j in range(i):  # j<=>k+1
            if (arr[j] < arr[i] and tabla_d[i] < tabla_d[j] + 1):
                # tabla_d[i] = max(tabla_d[i],tabla_d[j] + 1)
                tabla_d[i] = tabla_d[j] + 1
                tabla_p[i] = j

    largo_lis = max(tabla_d)
    #    posicion = tabla_d.index(largo_lis)

    #    print(f"Tabla del largo es: {tabla_d}")
    #   print(f"Tabla de indice de las subsecuencias es: {tabla_d}")

    pos = tabla_p.index(max(tabla_p))  # Se obtiene el indice del mayor valor de la tabla_p de posiciones
    lis = []
    contador = 0  # contador para saber el numero de elementos agregados a la lista lis
    # Se agregan los elementos de la subsecuencia a la lista lis(longest increasing subsequence)
    while (pos != -1):
        # print(arr[pos])
        lis += [arr[pos]]
        lis = [arr[pos]] + lis
        # print(lis)
        pos = tabla_p[pos]
        contador += 1
    lis = lis[:contador]
    # print(lis)
    return (lis)  # se retorna el longest increasing subsequence


if __name__ == "__main__":
    secuencia1 = [0, 4, 12, 2, 10, 6, 9, 13, 3, 11, 7, 15]
    # secuencia1 =  [5, 2, 8, 6, 3, 6, 9, 7]
    # secuencia1 = [5,7,12,9,33,29,45]
    lis = funcion_lis(secuencia1)
    print(f"Lista a evaluar: {secuencia1}")
    print(f"Sub-secuencia mayor(Lis) es: {lis}")
    print(f"Largo del Lis: {len(lis)}")
    # funcion_lis(secuencia1)
