def sumar(arreglo, izq, der):
    #Funcion que calcula la suma de una porcion del arreglo desde el indice izq al indice der
    if (izq == 0):# si el límite izquierdo es cero, la suma es el elemento en la posición del límite derecho
        return arreglo[der]
    else:
    #sino la suma es la diferencia entre los elementos en las posiciones del límite derecho y del límite izquierdo - 1
        return arreglo[der] - arreglo[izq - 1]


def tiempo_minimo(arr, n, k):
    ##param arr: arreglo con los tiempos que tarda cada pintor en pintar la tabla
    ##param n: numero de particiones de la tabla
    ##param k: numero maximo de pintores que se pueden contratar
    pref = [0] * n  #crear un arreglo de n elementos, inicializado con ceros, que representará la suma acumulada de cada subarreglo
    #pref se refiere a prefijo que en este contexto representa la suma de un sub arreglo del arreglo
    pref[0] = arr[0]  #el primer elemento de la suma de prefijos es igual al primer elemento del arreglo original

    for i in range(1, n):  # se recorre el arreglo original a partir del segundo elemento 1-n
        #cada elemento de la suma de prefijos es igual a la suma acumulativa del elemento actual y el elemento anterior
        pref[i] = pref[i-1] + arr[i]

    # se crea una tabla de programación dinámica de tamaño  inicializada en ceros
    tabla_dp = [[0 for i in range(n + 1)] for j in range(k + 1)]

    for i in range(1, n + 1):
        tabla_dp[1][i] = sumar(pref, 0, i - 1) #se llena la primera fila de la tabla con las sumas de prefijos de los tiempos de pintura de las tablas

    for i in range(1, k + 1):
        tabla_dp[i][1] = arr[0] #se llena la primera columna de la tabla con el tiempo que tarda un único pintor en pintar todas las tablas

    for i in range(2, k + 1):
        #recorrer la tabla programación dinámica a partir de la segunda fila y columna
        for j in range(2, n + 1):
            tiempo_minimo = 2 ** 63 - 1  #se inicializa el tiempo mínimo con un valor masivo
            for particion in range(1, j + 1):  #se recorre cada posible partición de las tablas
            #se calcula el tiempo mínimo entre el máximo de las sumas de prefijos de las particiones y el tiempo mínimo de la partición anterior
                tiempo_minimo = min(tiempo_minimo, max(tabla_dp[i - 1][particion], sumar(pref, particion,j - 1)))#barometro
            tabla_dp[i][j] = tiempo_minimo #se guarda el tiempo mínimo en la tabla de programación dinámica

    return tabla_dp[k][n]  #se retorna el tiempo mínimo necesario para pintar todas las tablas con k pintores

#Main del programa
if __name__ ==  "__main__":
    arreglo1 = [10,30,40,50]
    n1 = 4
    k1 = 2
    print(f"Arreglo 1 {arreglo1} con {n1} pintores y {k1} particiones")
    print(f"\tTiene un tiempo minimo de: {tiempo_minimo(arreglo1,n1,k1)}")

    arreglo2 = [10,20,60,30,40,50]
    n2 = 6
    k2 = 3

    print(f"\nArreglo 2 {arreglo2} con {n2} pintores y {k2} particiones")
    print(f"\tTiene un tiempo minimo de: {tiempo_minimo(arreglo2,n2,k2)}")