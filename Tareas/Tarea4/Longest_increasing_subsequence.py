def funcion_lis(arr):
    """
    Funcion que calcula la sub-secuencia mayor de la sucesion ingresada por parametro
    param arr: Arreglo de los valores a calcular su sub-sucesion mayor
    """
    n = len(arr)  # largo del arreglo a calcular
    tabla_d = [1] * n  # lista programacion dinamica donde se obtendra el mayor largo de la secuencia
    tabla_p = [-1] * n #tabla de las posiciones previas de la lista de sub-sucesion mayor inicializadas con -1

    for i in range(1, n):  # itera sobre todos los elementos del arreglo
        # Se itera desde j<-1 hasta i, es decir el valor actual iterado de 1 a n
        for j in range(i):  # itera hasta la posicion actual que se esta iterando sobre el arreglo de tamaño n
            """
            Se verifica que el valor j actual del arreglo es menor que el i que se esta iterando en el primer ciclo for
            Tambien se valida al mismo tiempo que el valor de la posicion +1 es mayor que la posicion actual en la tabla de posiciones
            """
            if (arr[j] < arr[i] and tabla_d[i] < tabla_d[j] + 1):
                tabla_d[i] = tabla_d[j] + 1 #Se actualiza el valor de la tabla con posicion + 1
                tabla_p[i] = j #Se define el valor de la tabla posiciones como la actual posicion j

    pos = tabla_p.index(max(tabla_p))  # Se obtiene el indice del mayor valor de la tabla_p de posiciones
    lis = [] #Lista inicializada como vacia que contiene el longest increasing subsequence a retornar
    contador = 0  # contador para saber el numero de elementos agregados a la lista lis

    # Se agregan los elementos de la subsecuencia a la lista lis(longest increasing subsequence)
    while (pos != -1): # ciclo while mientras el valor de la posicion en la tabla_pos es diferente a -1
        lis += [arr[pos]] # Se concatena el valor del arreglo en base a la poscion actual que es el mayor valor
        lis = [arr[pos]] + lis # Se concatena el resto de la lista al valor de esta iteracion
        pos = tabla_p[pos] # Se actualiza la posicion

    #Se corta la lista hasta la mitad indicada por el largo del lis calculado en tabla_d
    lis = lis[:max(tabla_d)]
    return (lis)  # se retorna el longest increasing subsequence

#Main del programa
if __name__ == "__main__":
    #Secuencia a calcular su maxima sub-sucesion creciente
    secuencia1 = [5,7,12,9,33,29,45]
    lis = funcion_lis(secuencia1) #Se iguala lis al arreglo retornado por funcion_lis()
    #Se imprime en pantalla las listas correspondientes
    print(f"Lista a evaluar: {secuencia1}")
    print(f"Sub-sucesion mayor(Lis) es: {lis}")
    print(f"Largo del Lis: {len(lis)}")